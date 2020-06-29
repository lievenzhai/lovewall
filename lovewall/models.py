from lovewall import db
from datetime import datetime



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

