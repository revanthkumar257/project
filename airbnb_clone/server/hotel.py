from flask import Blueprint, request, jsonify, render_template
from models import db, Booking
from flask_jwt_extended import jwt_required, get_jwt_identity

hotel_blueprint = Blueprint('hotel', __name__)

@hotel_blueprint.route('/book', methods=['POST'])
@jwt_required()
def book_hotel():
    data = request.json
    current_user_id = get_jwt_identity()
    new_booking = Booking(
        user_id=current_user_id,
        image=data['image'],
        name=data['name'],
        details=data['details'],
        price=data['price'],
        rating=data['rating']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'success': True})

@hotel_blueprint.route('/booking')
@jwt_required()
def booking():
    current_user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=current_user_id).all()
    return render_template('booking.html', bookings=bookings)
