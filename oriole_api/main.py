#
#                __   _,--="=--,_   __
#               /  \."    .-.    "./  \
#              /  ,/  _   : :   _  \/` \
#              \  `| /o\  :_:  /o\ |\__/
#               `-'| :="~` _ `~"=: |
#                  \`     (_)     `/
#           .-"-.   \      |      /   .-"-.
#    .-----{     }--|  /,.-'-.,\  |--{     }-----.
#     )    (_)_)_)  \_/`~-===-~`\_/  (_(_(_)    (
#    (                                           )
#     )                Oriole-MAIN              (
#    (                  Eric.Zhou                )
#    '-------------------------------------------'
#

import re
from pyramid.settings import asbool, aslist
from nameko.standalone.rpc import ClusterRpcProxy
from oriole_api.json import success, fail, set_json, error_response


def check_auth(req):
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
    open_apis = aslist(req.settings.get("openapi", []))
    url = req.environ.get("PATH_INFO")

    if not url:
        return True

    for open_api in open_apis:
        if re.compile(open_api).match(url):
            return False

    return True


def main(req, handler):
    uri = req.settings.get("amqp")
    if not uri:
        raise ValueError("Error: need amqp.")

    timeout = int(req.settings.get("TMOUT", "5"))
    with ClusterRpcProxy({"AMQP_URI": uri}, timeout=timeout) as srv:
        req.json_result = fail()
        req.srv = srv
        return handler(req)


def check_factory(handler, registry):
    def check_login(req):
        req.settings = registry.settings
        sso = asbool(req.settings.get("SSO"))
        set_json(req)

        if check_url(req) and sso and not check_auth(req):
            return error_response(req, "auth_fail")
        else:
            return main(req, handler)

    return check_login


def run(cfg):
    cfg.add_tween("oriole_api.check_factory")
    cfg.add_request_method(success, "success")
    cfg.add_request_method(fail, "fail")
