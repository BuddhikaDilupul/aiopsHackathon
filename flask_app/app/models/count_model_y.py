from app import db
class Counter_Y(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    count =db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=True)