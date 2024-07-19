from flask import Blueprint, jsonify
from models import User
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_list), 200
