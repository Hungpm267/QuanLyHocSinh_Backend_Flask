===========================================================
🚀 Cách chạy project:

# Cài đặt môi trường
python -m venv venv
source venv/bin/activate  # Windows dùng venv\Scripts\activate
pip install -r requirements.txt

# Khởi tạo database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Chạy app
python run.py
===========================================================

# migrate
Flask-Migrate giúp bạn tự động hóa và quản lý quá trình cập nhật cấu trúc cơ sở dữ liệu theo các thay đổi trong code Python, giống như Git quản lý code vậy – giúp tránh lỗi và tiện làm việc nhóm.

===========================================================

# Blueprint
Blueprint là một "bản thiết kế" cho các phần của ứng dụng Flask – nó đóng gói các route, template, static files và logic liên quan vào từng module riêng biệt.
===========================================================

# ORM

ORM là kỹ thuật lập trình giúp bạn tương tác với cơ sở dữ liệu bằng đối tượng (object) thay vì viết câu lệnh SQL thủ công.

===========================================================

# Marshmallow là thư viện giúp bạn:
•	Chuyển đổi object Python → JSON (serialize)
•	Chuyển đổi JSON → object Python (deserialize)
•	Xác thực dữ liệu (validation)

===========================================================
===========================================================
