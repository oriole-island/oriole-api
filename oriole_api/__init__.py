"""Process sso.  """

import re
import logging
from pyramid.settings import asbool, aslist
from nameko.standalone.rpc import ClusterRpcProxy
from pyramid.renderers import render_to_response


_err = "Error: need amqp."
_tag = "Access-Control-Allow-Methods"
_js = (("Content-Type", "application/json"),
       ("Access-Control-Allow-Origin", "*"),
       ("Access-Control-Allow-Credentials", "true"),
       ("Access-Control-Allow-Headers", "Origin, Content-Type, Accept"),
       ("Access-Control-Allow-Methods", "POST,GET,PUT,OPTIONS,PATCH"))


def set_json(req):
    for header in req.response.headerlist:
        if header[0] == _tag:
            return
    req.response.headerlist.extend(_js)


def error_response(req, detail):
    set_json(req)
    return render_to_response(
        "json", {"success": False, "detail": detail, "result": {}},
        request=req, response=req.response)


def main(req, handler):
    req.json_result = {"success": False, "detail": "", "result": {}}
    uri = req.settings.get("amqp")
    if not uri:
        raise ValueError(_err)
    timeout = int(req.settings.get("TMOUT", "5"))
    with ClusterRpcProxy({"AMQP_URI": uri}, timeout=timeout) as srv:
        req.srv = srv
        return handler(req)


def check_auth(req):
    """Check sso."""

    sso_token = req.params.get("sso_token")
    if not sso_token:
        return False

    from ssoclient.login import sso_check_login
    from ssoclient.sso_status_code import SSO_OK
    result = sso_check_login(sso_token)
    if result["status"] == SSO_OK:
        return True

    return False


def check_url(req):
    """Check protected api."""

    open_apis = aslist(req.settings.get("openapi", []))
    url = req.environ.get("PATH_INFO")

    if not url:
        return True

    for open_api in open_apis:
        if re.compile(open_api).match(url):
            return False

    return True


def check_factory(handler, registry):
    """Add check function."""

    def check_login(req):
        """Check login."""

        req.settings = registry.settings
        sso = asbool(req.settings.get("SSO"))
        set_json(req)

        if check_url(req) and sso and not check_auth(req):
            return error_response(req, "auth_fail")

        return main(req, handler)

    return check_login


def success(req, result):
    return {"success": True, "detail": "", "result": result}


def fail(req, detail):
    return {"success": False, "detail": detail, "result": {}}


def includeme(config):
    config.add_tween("oriole_api.check_factory")
    config.add_request_method(success, "success")
    config.add_request_method(fail, "fail")
