from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TravelHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(100), nullable=False)
    end_location = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'timestamp': self.timestamp.isoformat()
        }

class User(db.Model):
    __bind_key__ = 'postgres'  # Esto vincula este modelo a PostgreSQL
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    document_type = db.Column(db.String(20), nullable=False)
    number_Id = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    expedition_date = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)