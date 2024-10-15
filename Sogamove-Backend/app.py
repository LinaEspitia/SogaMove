from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, TravelHistory
from routes import main_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main_routes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
