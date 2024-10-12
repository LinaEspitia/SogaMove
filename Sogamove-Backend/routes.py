from flask import Blueprint, jsonify, request
from models import db, TravelHistory

main_routes = Blueprint('main', __name__)

@main_routes.route('/travel_history', methods=['POST'])
def add_travel():
    data = request.get_json()
    new_travel = TravelHistory(
        start_location=data['start_location'],
        end_location=data['end_location'],
        timestamp=data['timestamp']
    )
    db.session.add(new_travel)
    db.session.commit()
    return jsonify(new_travel.to_dict()), 201

@main_routes.route('/travel_history', methods=['GET'])
def get_travel_history():
    travels = TravelHistory.query.all()
    return jsonify([travel.to_dict() for travel in travels])
