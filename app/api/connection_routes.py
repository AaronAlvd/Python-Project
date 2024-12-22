from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app.models import User, Connection, db

connection_routes = Blueprint('connection', __name__)

@connection_routes.route('/')
@login_required
def connection():
  """
  Get all of a users connections
  """

  connections = Connection.query.filter(Connection.user_id == current_user.id).all()
  return [connection.to_dict() for connection in connections]


@connection_routes.route('/', methods=['CREATE'])
@login_required
def createConnection():
  """
  Create a new connection
  """

  data = request.get_json()
  connection = data.get('connection')
  
  try: 
      # Create a new connection
      new_connection = Connection(user_id=current_user.id,text=connection)
      db.session.add(new_connection)
      db.session.commit()


      return jsonify({
            "message": "Connection created successfully",
            "connection_id": new_connection.id
        }), 201

  except Exception as e:
      db.session.rollback()
          return jsonify({"error": f"Failed to update connection: {str(e)}"}), 500


@connection_routes.route('/<int:id>', methods=['PUT'])
@login_required
def updateConnection(id):
  """
  Update a connection
  """

  data = request.get_json()
  connection = data.get('connection')

  data = Connection.query.filter(Connection.id == id).first()

  if not data:
    return jsonify({'error': 'Connection not found'}), 404

  if (data.user_id != current_user.id):
    return jsonify({'error': 'Unauthorized to delete this connection'}), 403

  try: 
      # Update the connection
      data.text = connection
      db.session.commit()

      return jsonify({
            "message": "connection updated successfully",
            "connection": {
                "id": connection.id,
                "text": connection.text,
            }
        }), 200
  except Exception as e:
    db.session.rollback()
        return jsonify({"error": f"Failed to update connection: {str(e)}"}), 500


@connection_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def deleteConnection(id):
  """
  Delete a connection
  """

  connection = Connection.query.filter(Connection.id == id).first()

  if not connection:
    return jsonify({'error': 'Connection not found'}), 404
  
  if (connection.user_id != current_user.id):
    return jsonify({'error': 'Unauthorized to delete this connection'}), 403

  try:
        # Delete the connection and commit the transaction
        db.session.delete(connection)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Connection deleted successfully"}), 200
    except Exception as e:
        # Rollback in case of an error
        db.session.rollback()
        return jsonify({"error": f"Failed to delete connection: {e}"}), 500



