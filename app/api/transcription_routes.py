from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Transcription, User, db

transcription_routes = Blueprint('transcription', __name__)

@transcription_routes.route('/')
@login_required
def transcriptions():
  """
  Query to get all the transcriptions of the current user
  """
  transcriptions = Transcription.query.all()
  return [transcription.to_dict() for transcription in transcriptions]


@transcription_routes.route('/', methods=['POST'])
@login_required
def createTranscriptions():
  """
  Creates a new transcription
  """

  data = request.get_json()
  title = data.get('title')
  text = data.get('text')

  try:
      # Create a new transcription
      transcription = Transcription(user_id=current_user.id,title=title,text=text)
      db.session.add(transcription)
      db.session.commit()

      return jsonify({
        'Message': 'Succesfully created trancription',
        'id': transcription.id
      })

  except Exception as e:
    db.session.rollback()
    return jsonify({"error": f"Failed to create transcription: {e}"}), 500


  


@transcription_routes.route('/<int:id>')
@login_required
def transcription(id):
  transcription = Transcription.query.filter(Transcription.id == id).first()
  return transcription.to_dict()


@transcription_routes.route('/<int:id>', methods=['PUT'])
@login_required
def updateTranscription(id):
  """
  Update the name and title of a transcription
  """
  data = request.get_json()
  title = data.get('title')
  text = data.get('text')

  transcription = Transcription.query.filter(Transcription.id == id).first()

  if not transcription:
        return jsonify({"error": "Transcription not found"}), 404

  if title:
    transcription.title = title
  if text:
    transcription.text = text

  try:
    db.session.commit()
    return jsonify({
        "message": "Transcription updated successfully",
        "transcription": {
            "id": transcription.id,
            "title": transcription.title,
            "text": transcription.text
        }
    }), 200
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": f"Failed to update transcription: {e}"}), 500


@transcription_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def deleteTranscription(id):
  """
  Deletes a specified transcription
  """
  transcription = Transcription.query.filter(Transcription.id == id).first()

  if (transcription.user_id == current_user.id):
    db.session.delete(transcription)
    db.session.commit()
    return jsonify({"Mesage": "Succesfully Deleted"})
