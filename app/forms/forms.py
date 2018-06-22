'''from flask_wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired

from wtforms import *
from wtforms import validators
from wtforms.validators import *
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
'''

from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import Form


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=True)