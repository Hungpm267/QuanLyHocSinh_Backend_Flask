from flask import Blueprint, request, jsonify
from .models import Student
from .database import db
from .schemas import serialize_student
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity # bảo vệ route bằng jwt
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

student_bp = Blueprint(
    'students',      # Tên blueprint
    __name__         # Tên module (Flask dùng để tìm static và template liên quan)
)

# Middleware kiểm tra JWT cho mọi request
@student_bp.before_request
def jwt_middleware():
    # Những route không cần token
    public_routes = ['/students/login', '/students/register', '/students/']

    # Nếu route hiện tại nằm trong danh sách public thì bỏ qua kiểm tra token
    if request.path in public_routes:
        print("ko cần middleware")
        return

    try:
        # Kiểm tra token (nếu sai sẽ raise exception)
        verify_jwt_in_request()
    except NoAuthorizationError:
        return jsonify({"msg": "Thiếu hoặc token không hợp lệ rồi"}), 401

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
@jwt_required()
def update_student(id):
    current_user = int(get_jwt_identity())
    if current_user != id:
        return jsonify({'msg': 'ban ko co quyen thay doi id nay'}), 403
    else:
        print('dung roi')

    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    student.grade = data.get('grade', student.grade)
    db.session.commit()
    return jsonify(serialize_student(student), {'msg': 'ok da cap nhat'})

@student_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_student(id):

    current_user = get_jwt_identity()

    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

"""================login và register================"""

@student_bp.route('/register', methods = ['POST'])
def student_register():
    data = request.get_json()
    student = Student.query.filter_by(username = data['username']).first()

    if student:
        return jsonify({'msg': 'username da ton tai roi'}), 400
    
    student = Student(name = data['name'], age = data['age'], grade = data['grade'])
    student.username = data.get('username',student.username)
    student.set_password(data['password'])
    db.session.add(student)
    db.session.commit()

    return jsonify({'msg': 'tao tai khoan thanh cong'}), 201



@student_bp.route('/login', methods=['POST'])
def student_login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    hocsinh = Student.query.filter_by(username = username).first()

    if not hocsinh:
        return jsonify({'msg': 'username khong ton tai'}), 400
    else: 
        if hocsinh.check_password(password):
            mk = hocsinh.password
            token = create_access_token(identity=str(hocsinh.id))
            """
            create_access_token:
            Đây là hàm từ thư viện flask-jwt-extended.
            Nó tạo ra một JWT access token.
            Tham số identity=user.id có nghĩa là:
            "Gắn ID của user này vào trong token – để sau này xác thực lại có thể biết ai đang gửi request."
            """
            return jsonify({'access_token': token, 
                           'msg': 'dang nhap thanh cong goi',
                           'matkhau da nhap la': password,
                           'mat khau sau khi ma hoa': mk}), 200
        else:
            return jsonify({'msg': 'mat khau sai'}), 401


