from flask import Flask

app = Flask(__name__)
#app.debug = False
app.debug = True
app.config.from_object('config')

if (app.debug):
    from werkzeug.debug import DebuggedApplication
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

baseurl = app.config['BASE_URL']

from .api.views import apiView as apiView
app.register_blueprint(apiView)

from .pages.views import pageView as pageView
app.register_blueprint(pageView)

