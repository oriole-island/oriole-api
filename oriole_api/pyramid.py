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
#     )               Oriole-Pyramid            (
#    (                  Eric.Zhou                )
#    '-------------------------------------------'
#

import sys
from os.path import basename, splitext
from pyramid.view import view_config, view_defaults


def web(name='webapi'):
    return view_defaults(route_name=name)


def _conf(name, action, renderer):
    return {
        'match_param': ('service=%s' % name, 'action=%s' % action),
        'renderer': renderer,
        'request_method': ('GET', 'POST')
    }


def service(name):
    return splitext(basename(name))[0]


def act(action, renderer='json'):
    filename = sys._getframe().f_back.f_code.co_filename
    return view_config(
        **_conf(service(filename), action, renderer))


def api(name, action, renderer='json'):
    return view_config(**_conf(name, action, renderer))
