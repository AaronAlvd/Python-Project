from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User, Transcription, Article, Prompt

user_routes = Blueprint('user', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/transcription')
@login_required
def userTranscriptions():
    """
    Query all the transcriptions of a user
    """

    transcriptions = Transcription.query.filter(Transcription.user_id == current_user.id)
    return [transcription.to_dict() for transcription in transcriptions]


@user_routes.route('/article')
@login_required
def userArticles():
    """
    Query all the articles of a user
    """

    articles = Articles.query.filter(Article.user_id == current_user.id)
    return [article.to_dict() for article in articles]


@user_routes.route('/prompt')
@login_required
def userPrompts():
    """
    Query all the prompts of a user
    """

    prompts = Prompt.query.filter(Prompt.user_id == current_user.id)
    return [prompt.to_dict() for prompt in prompts]

@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()
