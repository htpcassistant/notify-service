from flask import Blueprint

from web.index import IndexView, CounterAPI
from web.notify import WxMsgSendAPI


def register_urls(app):
    # Create the blueprint for this app
    mod = Blueprint("payment_methods", __name__, url_prefix="/someapp/", template_folder="templates")

    # 路由
    app.add_url_rule('/', view_func=IndexView.as_view('main'))
    app.add_url_rule('/counter', view_func=CounterAPI.as_view('counter'))

    # 微信通知
    app.add_url_rule('/notify/wechat', view_func=WxMsgSendAPI.as_view('notify_wechat'))
