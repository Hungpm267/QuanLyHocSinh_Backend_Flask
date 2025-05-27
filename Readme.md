

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

> 💡 *Tip:* Hãy giữ README này được cập nhật khi dự án thay đổi nhé!

---

Bạn có muốn thêm phần **Mô tả dự án** hoặc **Tác giả / Thông tin liên hệ** không?
