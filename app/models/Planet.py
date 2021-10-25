from app import db

class Planet(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    biggest_moon = db.Column(db.String)