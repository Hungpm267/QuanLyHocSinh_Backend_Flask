

---

# 🚀 Hướng Dẫn Chạy Dự Án

## 🛠️ Cài đặt môi trường

```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🗄️ Khởi tạo và nâng cấp CSDL (Database)

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## ▶️ Chạy ứng dụng

```bash
python run.py
```

---

# 🔄 Flask-Migrate là gì?

**Flask-Migrate** giúp tự động hóa việc thay đổi cấu trúc cơ sở dữ liệu (database migration) dựa trên thay đổi trong mô hình Python.
Tương tự như Git quản lý mã nguồn, Flask-Migrate giúp bạn:

* Tránh lỗi do thay đổi thủ công.
* Dễ dàng làm việc nhóm và theo dõi lịch sử thay đổi.

---

# 🧩 Blueprint là gì?

**Blueprint** trong Flask là một "bản thiết kế" cho các phần của ứng dụng. Nó giúp bạn:

* Tách biệt các chức năng của app thành từng module.
* Tổ chức route, template, static files và logic một cách gọn gàng.

➡️ Hữu ích khi ứng dụng lớn dần hoặc làm việc theo nhóm.

---

# 🗃️ ORM (Object-Relational Mapping)

**ORM** cho phép bạn làm việc với database bằng cách thao tác object trong Python thay vì viết SQL thủ công.

Ví dụ:

```python
user = User.query.filter_by(id=1).first()
```

✅ Giúp code ngắn gọn, dễ bảo trì và ít lỗi hơn.

---

# 🧪 Marshmallow là gì?

**Marshmallow** là thư viện hỗ trợ:

* ✅ **Serialize**: Chuyển object Python → JSON
* ✅ **Deserialize**: Chuyển JSON → object Python
* ✅ **Validation**: Kiểm tra dữ liệu đầu vào hợp lệ

➡️ Hữu ích khi xây dựng API với Flask.

---

Dưới đây là phần bổ sung lý thuyết về **CORS** được viết theo cùng phong cách với phần còn lại của README của bạn:

---

# 🌐 CORS là gì?

**CORS** (*Cross-Origin Resource Sharing*) là cơ chế bảo mật trên trình duyệt, cho phép hoặc chặn **giao tiếp giữa các nguồn khác nhau** (ví dụ: frontend chạy ở `localhost:3000` gọi API từ `localhost:5000`).

Trong Flask, nếu bạn xây dựng API để frontend (React, Vue, v.v.) gọi tới, thì gần như **bắt buộc phải bật CORS**, nếu không sẽ bị lỗi như:

```text
Access to fetch at 'http://localhost:5000' from origin 'http://localhost:3000' has been blocked by CORS policy
```

### ✅ Giải pháp: dùng `flask-cors`

Cài đặt:

```bash
pip install flask-cors
```

Sử dụng trong `run.py` hoặc file cấu hình chính:

```python
from flask_cors import CORS

# Áp dụng cho toàn bộ app
CORS(app)
```

Bạn cũng có thể giới hạn cho từng blueprint hoặc route, hoặc chỉ cho phép một số domain cụ thể:

```python
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
```

---

📌 **Tóm lại:**

* CORS **không phải bug**, mà là bảo mật trình duyệt.
* CORS rất quan trọng khi backend và frontend **chạy ở các port khác nhau**.

---

Bạn có muốn mình cập nhật luôn phần code mẫu `run.py` để bật CORS đúng cách không?


---

> 💡 *Tip:* Hãy giữ README này được cập nhật khi dự án thay đổi 

---


