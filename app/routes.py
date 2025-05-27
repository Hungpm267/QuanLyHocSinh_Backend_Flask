from flask import Blueprint, request, jsonify
from .models import Student
from .database import db
from .schemas import serialize_student

student_bp = Blueprint(
    'students',      # Tên blueprint
    __name__         # Tên module (Flask dùng để tìm static và template liên quan)
)


@student_bp.route('/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([serialize_student(s) for s in students])

@student_bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(serialize_student(student))

@student_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'], grade=data['grade'], username = data['username'], password = data['password'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(serialize_student(new_student)), 201

@student_bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    student.grade = data.get('grade', student.grade)
    db.session.commit()
    return jsonify(serialize_student(student))

@student_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

@student_bp.route('/login', methods=['POST'])
def student_login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    student = Student.query.filter_by(username=username).first()

    if student and student.password == password:
        return jsonify({"message": "Đăng nhập thành công!"}), 200
    else:
        return jsonify({"error": "Tên đăng nhập hoặc mật khẩu không đúng"}), 401


