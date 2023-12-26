# 4.3 : พี่รหัส
# • ให้แก้ไขคลาส student โดยเพิม ่ ข้อมูล พี่รหัส (student_menter) หมายถึงนักศึกษาที่เป็นพีร ่ หัสขึ้นไป 1
# ชั้นปีเท่านั้น
# • ให้สร้าง instance ของ นศ. 4 คนขึ้นไป เช่น a เป็นปี 1, b เป็นปี 2 และเป็นพี่รหัสของ a
# c เป็นปี 3 และเป็นพี่รหัสของ b ส่วน d เป็นปี 4 และเป็นพี่รหัสของ c การสร้าง Instance ให้ใช้รหัส
# นักศึกษา 8 หลัก และเลข 2 ตัวแรกตามชั้นปีจริง
# – ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
# ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
# นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่ มพ ี ี่รหัสด้วย
# – ให้เขียนฟังก์ชัน #4 โดยเมือ ่ ป้อนรหัสนักศึกษา Student x และ student y ให้ตรวจสอบว่าเป็น
# สายรหัสกันหรือไม่ ให้ตอบเป็น True และ False
# • โปรแกรมอาจแยกเขียนจากโปรแกรม 4.2 ก็ได้


class Student:
    def __init__(self, student_id, student_name):
        self.id = student_id
        self.name = student_name
        self.mentors = []

    def add_mentor(self, mentor):
        self.mentors.append(mentor)


def get_student_instance_from_id(student_id):
    for student in students:
        if (student.id == student_id):
            return student


def get_mentors(student):
    if not student.mentors:
        return []

    mentors = []
    mentors.extend(student.mentors)
    for mentor in student.mentors:
        mentors.extend(get_mentors(mentor))
    return mentors


def display_student_id_name(student_list):
    if not student_list:
        print('Not found')
        return

    print("ID\t\t\tName")
    for student in student_list:
        print(student.id, student.name, sep='\t')


def is_mentor_of(student1_id, student2_id):
    if student1_id > student2_id:
        student1_id, student2_id = student2_id, student1_id

    student1_obj = get_student_instance_from_id(student1_id)
    student2_obj = get_student_instance_from_id(student2_id)

    student1_mentors = get_mentors(student1_obj)
    for object_student in student1_mentors:
        if object_student == student2_obj:
            return True
    return False


students = [
    Student(61000001, "Alice"),
    Student(62000001, "Bob"),
    Student(63000001, "Cereal"),
    Student(64000001, "Dannnnnnny"),
    Student(61000002, 'Elaine'),
    Student(62000002, "Frank"),
    Student(63000002, "Garnet"),
    Student(64000002, "Helpppp")
]

students[0].add_mentor(students[1])
students[0].add_mentor(students[4])
students[1].add_mentor(students[2])
students[2].add_mentor(students[3])

students[4].add_mentor(students[5])
students[5].add_mentor(students[6])
students[6].add_mentor(students[7])

display_student_id_name(get_mentors(get_student_instance_from_id(int(input('get_mentor_from_student_id : ')))))
# print(is_mentor_of(int(input("Student1_is_mentor : ")), int(input("Student2_is_mentor : "))))
