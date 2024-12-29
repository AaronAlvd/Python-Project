from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Prompt, User, Transcription, Article, db
from sqlalchemy import or_

searchEngine_routes = Blueprint('searchEngine', __name__)

@searchEngine_routes.route('/<string:query>')
@login_required
def searchEngine(query):
    """
    Searches across Articles, Transcriptions, and Prompts tables for records 
    matching the query in title or text.

    Args:
        session: SQLAlchemy session.
        query (str): The search term.

    Returns:
        dict: A dictionary containing matched records by category (articles, transcriptions, prompts).
    """
    # Search Articles
    article_matches = Article.query.filter(or_(Article.title.ilike(f"%{query}%"), Article.text.ilike(f"%{query}%"))).all()

    # Search Transcriptions
    transcription_matches = Transcription.query.filter(or_(Transcription.title.ilike(f"%{query}%"), Transcription.text.ilike(f"%{query}%"))).all()

    # Search Prompts
    prompt_matches = Prompt.query.filter(Prompt.title.ilike(f"%{query}%"), Prompt.prompt.ilike(f'%{query}%')).all()

    return {
        "articles": [article.to_dict() for article in article_matches],
        "transcriptions": [transcription.to_dict() for transcription in transcription_matches],
        "prompts": [prompt.to_dict() for prompt in prompt_matches],
    }