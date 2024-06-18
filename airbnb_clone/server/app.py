from flask import Flask, render_template, jsonify, request, redirect, url_for
from config import Config
from models import db, bcrypt, migrate, User, Property, Booking
from auth import auth_blueprint
from hotel import hotel_blueprint
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import os
import requests

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)
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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/mybookings')
@jwt_required()
def my_bookings():
    current_user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=current_user_id).all()
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Fetch hotel images from Google
def fetch_hotel_images(query, num_images=5):
    API_KEY = os.getenv('GOOGLE_API_KEY')
    CX = os.getenv('GOOGLE_CX')
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&num={num_images}&searchType=image&key={API_KEY}&cx={CX}"
    response = requests.get(url)
    data = response.json()
    images = [item['link'] for item in data.get('items', [])]
    return images[:num_images]

# Predefined categories and their queries for hotel images
categories = {
    'Near to Sea': 'hotels near sea',
    'City View': 'city view hotels',
    'Rural View': 'hotels with rural view',
    'Mountain View': 'mountain view hotels',
    'Pool View': 'hotels with pool view'
}

@app.context_processor
def inject_categories():
    return dict(categories=categories)

# Preload hotel images from Google for each category
hotel_images = {category: fetch_hotel_images(query) for category, query in categories.items()}

@app.route('/get_hotel_images/<category>')
def get_hotel_images(category):
    return jsonify({'images': hotel_images.get(category, [])})

if __name__ == '__main__':
    app.run(debug=True)
