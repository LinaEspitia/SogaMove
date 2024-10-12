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
