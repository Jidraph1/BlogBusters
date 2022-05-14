# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, Email, Length
# from wtforms.widgets import TextAreaField

# class RegisterForm(FlaskForm):
#     email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email')])
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('Password', validators=[InputRequired()])

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
#     password = PasswordField('Password', validators=[InputRequired()])
#     remember = BooleanField('Remember me')
