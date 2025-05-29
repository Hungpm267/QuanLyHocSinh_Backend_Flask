

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


📌 **Tóm lại:**

* CORS **không phải bug**, mà là bảo mật trình duyệt.
* CORS rất quan trọng khi backend và frontend **chạy ở các port khác nhau**.

---

JWT (JSON Web Token) là một chuẩn mở (RFC 7519) dùng để truyền thông tin giữa các bên một cách an toàn dưới dạng một **đối tượng JSON** nhỏ gọn, tự chứa. JWT thường được sử dụng để xác thực người dùng và trao đổi thông tin giữa client và server.

---

## **1. Cấu trúc của JWT**

JWT gồm 3 phần, được nối với nhau bằng dấu chấm (`.`):

```
Header.Payload.Signature
```

### 🔹 a. **Header**

Thường gồm 2 thông tin:

```json
{
  "alg": "HS256",      // Thuật toán ký (ví dụ: HS256, RS256)
  "typ": "JWT"         // Kiểu token
}
```

### 🔹 b. **Payload**

Chứa dữ liệu (claims) mà bạn muốn truyền đi, gồm 3 loại:

* **Registered claims**: các trường chuẩn như:

  * `iss` (issuer) – người phát hành
  * `sub` (subject) – chủ thể
  * `aud` (audience) – đối tượng nhận
  * `exp` (expiration) – thời điểm hết hạn
  * `iat` (issued at) – thời điểm phát hành
* **Public claims**: có thể dùng chung, cần đăng ký tránh trùng lặp.
* **Private claims**: thông tin tùy chỉnh giữa các bên (ví dụ: userId, role...)

Ví dụ:

```json
{
  "sub": "1234567890",
  "name": "Nguyen Van A",
  "admin": true,
  "iat": 1516239022
}
```

### 🔹 c. **Signature**

Dùng để xác thực token không bị thay đổi. Tạo ra bằng cách:

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

---

## **2. Cách JWT hoạt động**

1. **Login**: Người dùng đăng nhập => Server xác thực => Tạo JWT => Gửi về client.
2. **Lưu trữ**: Client lưu JWT (thường trong localStorage hoặc cookie).
3. **Gửi yêu cầu**: Với mỗi request, client gửi JWT trong header:

```
Authorization: Bearer <token>
```

4. **Xác thực**: Server nhận token => kiểm tra chữ ký, thời hạn... => nếu hợp lệ thì cho phép truy cập.

---

## **3. Ưu điểm và Hạn chế**

### ✅ Ưu điểm:

* Gọn nhẹ, dễ truyền qua HTTP.
* Tự chứa: không cần lưu session phía server.
* Có thể dùng cho cả xác thực và phân quyền.

### ❌ Hạn chế:

* Không thể hủy token trước khi hết hạn (trừ khi dùng blacklist).
* Nếu bị lộ `secret key`, hệ thống sẽ bị tấn công.
* Payload có thể bị đọc nếu không mã hóa (dù không sửa được nếu không có `secret`).

---

> 💡 *Tip:* Hãy giữ README này được cập nhật khi dự án thay đổi 

---

