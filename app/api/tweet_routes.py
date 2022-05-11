from flask import Blueprint, jsonify
from app.models import Tweet, User

tweet_routes = Blueprint('tweets', __name__)

@tweet_routes.route('/')
def get_tweets():
  tweets = Tweet.query.join(User).all()
  return {'tweets': [tweet.to_dict() for tweet in tweets]}
