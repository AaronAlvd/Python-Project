from .db import db, environment, SCHEMA

class Prompt(db.Model):
  __tablename__ = 'prompts'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  title = db.Column(db.String, nullable=False, default='Untitled Prompt')
  prompt = db.Column(db.Text, nullable=False)

  def to_dict(self):
      return {
            'id': self.id,
            'user_id': self.user_id,
            'prompt': self.prompt
      }