import time

from flask import session
from flask.views import View, MethodView


class IndexView(View):
    def dispatch_request(self):
        return 'Now Time is: %s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


class CounterAPI(MethodView):
    def get(self):
        counter = session.get('counter', 0)
        return 'counter: %s' % counter

    def post(self):
        session['counter'] = session.get('counter', 0) + 1
        return 'OK'
