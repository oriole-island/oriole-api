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
#     )                Oriole-JSON              (
#    (                  Eric.Zhou                )
#    '-------------------------------------------'
#

from pyramid.renderers import render_to_response

_tag = "Access-Control-Allow-Methods"
_js = [
    ("Content-Type", "application/json"),
    ("Access-Control-Allow-Origin", "*"),
    ("Access-Control-Allow-Credentials", "true"),
    ("Access-Control-Allow-Headers", "Origin, Content-Type, Accept, Content-Disposition"),
    ("Access-Control-Allow-Methods", "POST,GET,PUT,OPTIONS,PATCH")
]


def set_json(req):
    for header in req.response.headerlist:
        if header[0] == _tag:
            return
    req.response.headerlist.extend(_js)


def error_response(req, detail):
    set_json(req)
    return render_to_response(
        "json", fail(detail=detail),
        request=req, response=req.response)


def success(req="", result=""):
    if not result:
        result = {}
    return {"success": True, "detail": "", "result": result}


def fail(req="", detail=""):
    return {"success": False, "detail": detail, "result": {}}
