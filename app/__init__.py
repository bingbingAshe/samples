import os
from flask.ext.login import loginManager
from flask.ext.openid import OpenID
from app.config import basedir
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app.views import helloworld,login

