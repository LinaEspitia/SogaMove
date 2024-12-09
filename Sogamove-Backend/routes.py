from flask import Blueprint, jsonify, request
from models import db, TravelHistory
from models import db, User

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


@main_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    try:
        # Crear un nuevo usuario basado en los datos recibidos
        new_user = User(
            document_type=data['document_type'],
            number_Id=data['number_Id'],
            birth_date=data['birth_date'],
            expedition_date=data['expedition_date'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']  # Considera hashear la contraseña.
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al registrar el usuario", "details": str(e)}), 400
