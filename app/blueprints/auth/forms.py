from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp, EqualTo

from app.models import User


with open("banned_usernames.txt", "r") as f:
	banned_usernames = f.read().split("\n")


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	remember_me = BooleanField("Remember me")
	submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
	username = StringField(
		"Username", 
		validators=[
			DataRequired(),
			Length(3, 24),
			Regexp(
			    "^[A-Za-z][A-Za-z0-9_]*$", 
			    0,
			    "Usernames may only contain letters, numbers or underscores."
			)
		]
    )
	password = PasswordField(
		"Password",
		validators=[
			DataRequired(),
			Length(6, 32),
			EqualTo("password2", message="Passwords do not match!")
		]
	)
	password2 = PasswordField("Confirm password", validators=[DataRequired()])
	submit = SubmitField("Register")

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first() \
				or field.data.lower() in banned_usernames:
			raise ValidationError("Username unavailable!")