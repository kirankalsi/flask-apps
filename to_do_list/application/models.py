from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))
    is_complete = db.Column(db.Boolean)
