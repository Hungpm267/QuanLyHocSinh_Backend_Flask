import os


class Config:
    SECRET_KEY = os.environ.get('secretkeycuahung', 'default_secret_key') 
    # Dùng cho Flask session (ví dụ: bảo mật cookie, CSRF)
    JWT_SECRET_KEY = os.environ.get('jwtsecretkeycuahung', 'default_jwt_secret_key')
    # Dùng để ký và xác thực JWT token

    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False