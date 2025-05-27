
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .database import db
from .routes import student_bp
from app.config import Config





def create_app():
    appcuatoi = Flask(__name__)
    appcuatoi.config.from_object(Config)

    db.init_app(appcuatoi)
    migrate = Migrate(appcuatoi, db)

    appcuatoi.register_blueprint(student_bp, url_prefix="/students")

    return appcuatoi