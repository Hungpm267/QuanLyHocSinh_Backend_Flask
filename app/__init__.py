from flask import request # cho middleware
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .database import db
from .routes import user_bp
from app.config import Config
from flask_jwt_extended import JWTManager 
from flask_cors import CORS  # Import thư viện CORS


def log_request():
    """Middleware để log thông tin request."""
    print(f"Request method: {request.method}, URL: {request.url}")

def create_app():
    appcuatoi = Flask(__name__)
    appcuatoi.config.from_object(Config)

    db.init_app(appcuatoi)
    migrate = Migrate(appcuatoi, db)

    jwt = JWTManager(appcuatoi)

    # Thêm CORS vào ứng dụng
    CORS(appcuatoi)

    # Đăng ký middleware
    appcuatoi.before_request(log_request)

    appcuatoi.register_blueprint(user_bp, url_prefix="/users")

    return appcuatoi