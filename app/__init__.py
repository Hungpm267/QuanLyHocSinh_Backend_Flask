
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .database import db
from .routes import student_bp
from app.config import Config
from flask_jwt_extended import JWTManager 
from flask_cors import CORS  # Import thư viện CORS




def create_app():
    appcuatoi = Flask(__name__)
    appcuatoi.config.from_object(Config)

    db.init_app(appcuatoi)
    migrate = Migrate(appcuatoi, db)

    jwt = JWTManager(appcuatoi)

    # Thêm CORS vào ứng dụng
    CORS(appcuatoi)

    appcuatoi.register_blueprint(student_bp, url_prefix="/students")

    return appcuatoi