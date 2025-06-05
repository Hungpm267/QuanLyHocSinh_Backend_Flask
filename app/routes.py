from flask import Blueprint, request, jsonify
from .models import User
from .database import db
from .schemas import serialize_user
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity # bảo vệ route bằng jwt
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

user_bp = Blueprint(
    'users',      # Tên blueprint
    __name__         # Tên module (Flask dùng để tìm static và template liên quan)
)

# Middleware kiểm tra JWT cho mọi request
@user_bp.before_request
def jwt_middleware():
    # Những route không cần token
    public_routes = ['/users/login', '/users/register', '/users/']

    # Nếu route hiện tại nằm trong danh sách public thì bỏ qua kiểm tra token
    if request.path in public_routes:
        print("ko cần middleware")
        return

    try:
        # Kiểm tra token (nếu sai sẽ raise exception)
        verify_jwt_in_request()
    except NoAuthorizationError:
        return jsonify({"msg": "Thiếu hoặc token không hợp lệ rồi"}), 401

@user_bp.route('/', methods=['GET'])
def get_user():
    user = User.query.all()
    return jsonify([serialize_user(s) for s in user])

@user_bp.route('/<int:id>', methods=['GET'])
def get_user_id(id):
    user = User.query.get_or_404(id)
    return jsonify(serialize_user(user))

@user_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    new_user = User(name=data['name'], age=data['age'], grade=data['grade'], username = data['username'], password = data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(serialize_user(new_user)), 201

@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    current_user = int(get_jwt_identity())
    if current_user != id:
        return jsonify({'msg': 'ban ko co quyen thay doi id nay'}), 403
    else:
        print('dung roi')

    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.age = data.get('age', user.age)
    user.grade = data.get('grade', user.grade)
    db.session.commit()
    return jsonify(serialize_user(user), {'msg': 'ok da cap nhat'})

@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):

    current_user = get_jwt_identity()

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

"""================login và register================"""

@user_bp.route('/register', methods = ['POST'])
def user_register():
    data = request.get_json()
    user = User.query.filter_by(username = data['username']).first()

    if user:
        return jsonify({'msg': 'username da ton tai roi'}), 400
    
    user = User(name = data['name'], age = data['age'], grade = data['grade'], role = data['role'])
    user.username = data.get('username',user.username)
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': 'tao tai khoan thanh cong'}), 201



@user_bp.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username = username).first()

    if not user:
        return jsonify({'msg': 'username khong ton tai'}), 400
    else: 
        if user.check_password(password):
            mk = user.password
            token = create_access_token(identity=str(user.id))
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


