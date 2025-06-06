from flask import Blueprint, request, jsonify
from app.models import users, check_user_password
from app.auth import generate_jwt, token_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users and check_user_password(username, password):
        token = generate_jwt(username)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected(user_id):
    return jsonify({'message': f'Welcome, User {user_id}'}), 200
