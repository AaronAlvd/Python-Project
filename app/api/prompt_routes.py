from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Prompt, User, db

prompt_routes = Blueprint('prompt', __name__)

@prompt_routes.route('/')
@login_required
def prompts():
  """
  Returns all prompts owned by a specific user
  """

  prompts = Prompt.query.all()

  return [prompt.to_dict() for prompt in prompts]


@prompt_routes.route('/', methods=['POST'])
@login_required
def createPrompts():
    """
    Creates a new prompt
    """

    data = request.get_json()
    prompt = data.get('prompt')

    try: 
        # Create a new prompt
        newPrompt = Prompt(user_id=current_user.id, prompt=prompt)
        db.session.add(newPrompt)
        db.session.commit()

        return jsonify({
            'message': 'Prompt succesfully created',
            'id': newPrompt.id
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to create prompt: {str(e)}"}), 500
        

@prompt_routes.route('/<int:id>', methods=['PUT'])
@login_required
def editPrompts(id): 
    """
    Makes changes to the prompt
    """
    data = request.get_json()
    new_prompt = data.get('prompt')  # Retrieve new prompt text from the request

    # Fetch the prompt record from the database
    prompts = Prompt.query.filter(Prompt.id == id).first()

    if not prompts:
        return jsonify({"error": "Prompt not found"}), 404

    if prompts.user_id != current_user.id:
        return jsonify({"error": "Unauthorized to edit this prompt"}), 403

    try:
        # Update the prompt's content
        prompts.prompt = new_prompt  # Assuming `text` is the correct field name
        db.session.commit()
        
        return jsonify({
            "message": "Prompt updated successfully",
            "prompt": {
                "id": prompts.id,
                "prompt": prompts.prompt
            }
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to update prompt: {str(e)}"}), 500


@prompt_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def deletePrompt(id):
    """
    Deletes a prompt
    """
    # Find the prompt by ID
    prompt = Prompt.query.filter(Prompt.id == id).first()

    # Check if the prompt exists
    if not prompt:
        return jsonify({"error": "Prompt not found"}), 404

    # Check if the current user is authorized to delete the prompt
    if prompt.user_id != current_user.id:
        return jsonify({"error": "Unauthorized to delete this prompt"}), 403

    try:
        # Delete the prompt and commit the transaction
        db.session.delete(prompt)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Prompt deleted successfully"}), 200
    except Exception as e:
        # Rollback in case of an error
        db.session.rollback()
        return jsonify({"error": f"Failed to delete prompt: {e}"}), 500

