from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app.models import User, Article, db

article_routes = Blueprint('article', __name__)

@article_routes.route('/')
@login_required
def article():
  """
  Get all of a users articles
  """

  articles = Article.query.all()
  return [article.to_dict() for article in articles]


@article_routes.route('/', methods=['POST'])
@login_required
def createArticle():
  """
  Create a new article
  """

  data = request.get_json()
  article = data.get('article')
  title = data.get('title')
  slug = data.get('slug')
  
  try: 
      # Create a new article
      new_article = Article(user_id=current_user.id,text=article, slug=slug, title=title)
      db.session.add(new_article)
      db.session.commit()


      return jsonify({
          "message": "Article created successfully",
          "article_id": new_article.id
      }), 201

  except Exception as e:
      db.session.rollback()
      return jsonify({"error": f"Failed to create article: {str(e)}"}), 500


@article_routes.route('/<int:id>', methods=['PUT'])
@login_required
def updateArticle(id):
  """
  Update a article
  """

  data = request.get_json()
  article = data.get('article')

  data = Article.query.filter(Article.id == id).first()

  if not data:
    return jsonify({'error': 'Article not found'}), 404

  if (data.user_id != current_user.id):
    return jsonify({'error': 'Unauthorized to delete this article'}), 403

  try: 
      # Update the article
      data.text = article
      db.session.commit()

      return jsonify({
            "message": "Article updated successfully",
            "article": {
                "id": article.id,
                "text": article.text,
            }
        }), 200
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": f"Failed to update article: {str(e)}"}), 500


@article_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def deleteArticle(id):
  """
  Delete a article
  """

  article = Article.query.filter(Article.id == id).first()

  if not article:
    return jsonify({'error': 'Article not found'}), 404
  
  if (article.user_id != current_user.id):
    return jsonify({'error': 'Unauthorized to delete this article'}), 403

  try:
        # Delete the article and commit the transaction
        db.session.delete(article)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Article deleted successfully"}), 200
  except Exception as e:
      # Rollback in case of an error
      db.session.rollback()
      return jsonify({"error": f"Failed to delete article: {e}"}), 500

