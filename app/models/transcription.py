from .db import db, environment, SCHEMA

class Transcription(db.Model):
  __tablename__ = 'transcriptions'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  title = db.Column(db.String(255), nullable=False)
  text = db.Column(db.Text, nullable=False)

  def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'text': self.text
        }