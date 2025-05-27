"""
optional nếu ko dùng marshmallow, nhưng hữu ích để validate dữ liệu

"""
def serialize_student(student):
    return {
        "hocsinh_id": student.id,
        "hocsinh_name": student.name,
        "hocsinh_age": student.age,
        "hocsinh_grade": student.grade
    }