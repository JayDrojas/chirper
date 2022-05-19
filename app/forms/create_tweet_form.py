from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class Create_tweet_form(FlaskForm):
  content = StringField('content', validators=[DataRequired(message="Must have Content.")])
  user_id = IntegerField('user_id', validators=[DataRequired(), Length(max=255, message="The character limit for content is 255.")])
