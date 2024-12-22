from .db import db, environment, SCHEMA

class Connection(db.Model):
  __tablename__ = 'connections'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  text = db.Column(db.Text, nullable=False)

  def to_dict(self):
    return{
      'id': self.id,
      'user_id': self.user_id,
      'text': self.text
    }