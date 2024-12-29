from .db import db, environment, SCHEMA

class Article(db.Model):
  __tablename__ = 'articles'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  title = db.Column(db.String, nullable=False, default='Untitled Article')
  text = db.Column(db.Text, nullable=False)
  slug = db.Column(db.Text, nullable=False)

  def to_dict(self):
    return{
      'id': self.id,
      'title': self.title,
      'user_id': self.user_id,
      'slug': self.slug,
      'text': self.text,
    }