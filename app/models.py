from .database import db
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import validates
from datetime import date

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student' or 'teacher'
    username = db.Column(db.String(40), unique=True, nullable=True)
    password = db.Column(db.String(200), nullable=True)

    # Relationships
    classes_taught = db.relationship('Classes', backref='teacher', lazy=True)
    assignments_created = db.relationship('Assignment', backref='creator', lazy=True)
    student_classes = db.relationship('StudentClass', backref='student', lazy=True)

    def set_password(self, matkhau):
        self.password = generate_password_hash(matkhau)

    def check_password(self, matkhau):
        return check_password_hash(self.password, matkhau)


class Classes(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationships
    assignments = db.relationship('Assignment', backref='class_', lazy=True)
    students = db.relationship('StudentClass', backref='class_', lazy=True)


class Assignment(db.Model):
    __tablename__ = 'assignment'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date, default=date.today)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @validates('created_by')
    def validate_teacher(self, key, created_by_id):
        teacher = User.query.get(created_by_id)
        if not teacher or teacher.role != 'teacher':
            raise ValueError("Only teachers can create assignments.")
        return created_by_id


class StudentClass(db.Model):
    __tablename__ = 'student_class'

    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), primary_key=True)
