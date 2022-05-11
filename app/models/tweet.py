from .db import db
from sqlalchemy.sql import func

class Tweet(db.Model):
  __tablename__ = 'tweets'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  content = db.Column(db.String(500), nullable=False)
  created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

  user = db.relationship('User', back_populates="tweets")
  replies = db.relationship('Reply', backref="replies", cascade='all,delete')


  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'content': self.content,
      'created_at': self.created_at,
      'user': self.user.to_dict()
    }
