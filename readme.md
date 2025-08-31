# 📚 Quản Lý Học Sinh Backend (Flask)

Hệ thống quản lý học sinh và giáo viên, xây dựng bằng Flask, SQLAlchemy, Flask-Migrate, JWT, hỗ trợ xác thực, phân quyền, và quản lý lớp học, bài tập.

## 🚀 Tính năng

- Quản lý 2 loại người dùng: **học sinh** và **giáo viên**
- Giáo viên có thể: đăng ký, đăng nhập, tạo/xóa học sinh, thay đổi mật khẩu, quên mật khẩu, chat với học sinh
- Học sinh có thể: đăng nhập, quên mật khẩu, thay đổi mật khẩu, xem/cập nhật thông tin cá nhân, chat với giáo viên/học sinh
- Quản lý lớp học, phân công giáo viên, thêm học sinh vào lớp
- Quản lý bài tập, giao bài tập cho lớp
- Xác thực và phân quyền bằng JWT
- API RESTful, dễ dàng tích hợp với frontend

## 🛠️ Công nghệ sử dụng

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)
- [PyJWT](https://pyjwt.readthedocs.io/)
- [Marshmallow](https://marshmallow.readthedocs.io/) (tuỳ chọn cho serialize/validate)

## 📦 Cài đặt & chạy dự án

### 1. Tạo môi trường ảo và cài đặt thư viện

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Khởi tạo và nâng cấp database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Chạy ứng dụng

```bash
python run.py
```

Ứng dụng sẽ chạy tại `http://localhost:5000`.

## 🗂️ Cấu trúc thư mục

```
app/
    __init__.py
    config.py
    database.py
    models.py
    routes.py
    schemas.py
migrations/
    versions/
    env.py
    alembic.ini
run.py
requirements.txt
describe.txt
Knowledge.txt
```

## 📖 Tài liệu & hướng dẫn

- Xem file [`Knowledge.txt`](Knowledge.txt) để biết thêm về Flask-Migrate, Blueprint, ORM, Marshmallow, CORS, JWT.
- Xem file [`describe.txt`](describe.txt) để biết các chức năng của từng loại người dùng.

## 💡 Ghi chú

- Đảm bảo cấu hình kết nối database trong `app/config.py` phù hợp với môi trường của bạn.
- Nếu dùng SQL Server, cần cài đặt driver `pyodbc`.

---

Made with ❤️ by Hung