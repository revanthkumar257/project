from flask import Blueprint, request, jsonify, render_template
from models import db, Booking , Property
from flask_jwt_extended import jwt_required, get_jwt_identity


hotel_blueprint = Blueprint('hotel', __name__)

@hotel_blueprint.route('/book', methods=['POST'])
@jwt_required()
def book_hotel():
    data = request.json
    current_user_id = get_jwt_identity()
    new_booking =Property(
        user_id=current_user_id,
        title=data['name'],
        description=data['details'],
        price=data['price'],
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'success': True})

@hotel_blueprint.route('/get_hotel')
@jwt_required()
def booking():
    hotel = Property.query.all()
    hotel_data = []

    for vehicle in hotels:
        if not vehicle.sold:
            hotel_data.append(to_dict_vehicles(vehicle))

    return jsonify(vehicles_data), 200
