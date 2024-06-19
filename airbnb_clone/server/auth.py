from flask import Blueprint, request, jsonify, redirect, url_for,render_template
from models import db, bcrypt, User
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    username = request.form.get('fName') + " " + request.form.get('lName')
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists. Please sign in.'}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login_page'))

@auth_blueprint.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return redirect(url_for('home'))

@auth_blueprint.route('/login_page')
def login_page():
    return render_template('login.html')
