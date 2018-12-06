# coding: utf8
from flask import Flask
from config.settings import settings
from apps.evaluation import evaluation as evaluation_app


app = Flask(__name__, static_url_path='/statics',root_path=settings.STATIC_ROOT)
app.register_blueprint(evaluation_app)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')