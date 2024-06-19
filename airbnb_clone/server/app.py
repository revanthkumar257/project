from flask import Flask, render_template, jsonify, redirect, url_for
from config import Config
from models import db, Booking
from auth import auth_blueprint
from hotel import hotel_blueprint
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import os
import requests

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(hotel_blueprint, url_prefix='/api')

# Routes
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/mybookings')
@jwt_required()
def my_bookings():
    current_user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=current_user_id).all()
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/stays')
def stays1():
    return render_template('stays1.html')

if __name__ == '__main__':
    app.run(debug=True)
