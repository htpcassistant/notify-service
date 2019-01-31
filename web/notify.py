from flask import request
from flask.views import MethodView
from wechatpy.enterprise import WeChatClient

from bootstrap import app

CORP_ID = app.config['WX_CORP_ID']
AGENT_ID = app.config['WX_AGENT_ID']
SECRET = app.config['WX_SECRET']
PARTY_ID = app.config['WX_PARTY_ID']


def _ma_client():
    client = WeChatClient(CORP_ID, SECRET)
    return client


class WxMsgSendAPI(MethodView):
    """
    企业微信通知
    """

    def post(self):
        data = request.get_json()
        if not data:
            return "ARGS NULL"

        title = data['title'] or '通知'
        msg = data['msg']
        url = data['url'] or 'https://126.com'
        party_ids = data['party_ids'] or PARTY_ID

        client = _ma_client()
        resp = client.message.send_text_card(agent_id=AGENT_ID,
                                             party_ids=party_ids,
                                             title=title, description=msg, user_ids=None, url=url)
        return str(resp)
