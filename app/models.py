from .database import db
from werkzeug.security import check_password_hash, generate_password_hash


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(40), nullable=True, unique = True)
    password = db.Column(db.String(40), nullable=True)

    def set_password(self, matkhau):
        self.password = generate_password_hash(matkhau)

    def check_password(self, matkhau):
        return check_password_hash(self.password, matkhau)