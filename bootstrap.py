#!flask/bin/python
from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings.DevelopmentConfig)

# app.register_blueprint(urls.mod)
import urls

urls.register_urls(app)

if __name__ == '__main__':
    app.run()
