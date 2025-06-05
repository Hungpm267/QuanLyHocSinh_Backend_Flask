"""
optional nếu ko dùng marshmallow, nhưng hữu ích để validate dữ liệu

"""
def serialize_user(User):
    return {
        "User_id": User.id,
        "User_name": User.name,
        "User_age": User.age,
        "User_grade": User.grade,
        "User_username" : User.username,
        "User_password" : User.password
    }