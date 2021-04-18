from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreatePortfolioForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(3, 64)])
    submit = SubmitField("Create")


class CreateAssetForm(FlaskForm):
    symbol = StringField("Symbol", validators=[DataRequired(), Length(3, 12)])
    price = DecimalField("Price", validators=[DataRequired()])
    volume = DecimalField("Volume", validators=[DataRequired()])
    submit = SubmitField("Add")
