from app import db
class Counter(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    area = db.Column(db.String(255),nullable=False)
    count =db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=True)