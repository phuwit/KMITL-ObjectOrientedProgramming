# 4.2 : Student
# • โดยใช้กลุม ่ เดิ ม ใช้ระบบ Pair Programmer คือ คนที่ 1 บอก Code ให้คนที่ 2 เขี ยนตามคําบอก
# โดยหากไม่เห็นด้วย สามารถทักท้วงได้
# • ให้เขียนโปรแกรม เพื่อสร้างคลาสต่อไปนี้
# – นักศึกษา (Student) โดยมี attribute : student_id, student_name
# – รายวิชา (Subject) โดยมี attribute : subject_id, subject_name, section, credit
# – ผู้สอน (Teacher) โดยมี attribute : teacher_id, teacher_name
# – สามารถเพิ่ม attribute อืน ่ ๆ ได้
# ให้สร้าง Instance ของทุกคลาส และ สร้างความสัมพันธ์ (สามารถเพิ่ม attribute ได้)
# – ให้สร้าง instance ของนักศึกษา 5 คนขึ้นไป
# – ให้สร้าง instance ของอาจารย์ 2 คน
# – ให้สร้าง instance ของวิชา object oriented programming 2 instance 2 section โดยแต่ละ
# section มีผ ส ู้ อนคนละคน และแต่ละ section มีคนเรียนอย่ างน้อย 2 คน
# – ข้อมูลใน Instance ให้เป็นข้อมูลที่จริงจังสักหน่อย
# ให้เขียนฟั งก์ชัน #1 โดยเมื่อใส่ รหัสผู ส ้ อน แล้วสามารถบอกได้ว่ามี นศ. คนไหนบ้างที่เรียนกับผู้สอนนี้
# โดยให้บอกเป็นชื่อนักศึกษา
# ให้เขียนฟั งก์ชัน #2 โดยเมื่อใส่ รหัส นศ. แล้วบอกว่าเรียนวิ ชาอะไรบ้าง โดยให้บอกเป็นชื่อวิชา
# ข้อมูลทัง ้ หมดต้ องอยู่ในคลาสเท่านั้น ยกเว้น List ที่เก็บ นศ. ทั้งหมด วิชาทั้งหมด อาจารย์ทง ั้ หมด ให้
# อยู่ข้างนอกได้ และห้ามใช้ dictionary ในการเก็บข้อมูล


class Student:

    def __init__(self, student_id, student_name):
        self.id = student_id
        self.name = student_name


class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.id = subject_id
        self.name = subject_name
        self.section = section
        self.credit = credit
        self.students = []
        self.teachers = []

    def add_student(self, student_instance):
        self.students.append(student_instance)

    def add_teacher(self, teacher_instance):
        self.teachers.append(teacher_instance)


class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.id = teacher_id
        self.name = teacher_name


def get_object_from_list_by_id(id, list):
    for element in list:
        if (element.id == id):
            return element


def get_students_from_teacher(teacher):
    matched_students = []
    for subject in subjects:
        if teacher in subject.teachers:
            matched_students.extend(subject.students)
    return matched_students


def get_subjects_from_student(student):
    matched_subjects = []
    for subject in subjects:
        if student in subject.students:
            matched_subjects.append(subject)
    return matched_subjects


students = [
    Student(1, "John"),
    Student(2, "Jane"),
    Student(3, "Alice"),
    Student(4, "Bob"),
    Student(5, "Eve"),
    Student(6, "Wilson")
]

teachers = [
    Teacher(1, "Professor X"),
    Teacher(2, "Professor Y")
]

subjects = [
    Subject(101, "Object Oriented Programming", 1, 3),
    Subject(101, "Object Oriented Programming", 2, 3)
]


subjects[0].add_teacher(teachers[0])
subjects[1].add_teacher(teachers[1])

subjects[0].add_student(students[0])
subjects[0].add_student(students[1])
subjects[0].add_student(students[2])
subjects[1].add_student(students[3])
subjects[1].add_student(students[4])
subjects[1].add_student(students[5])


def student_names_from_teacher_id(teacher_id):
    teacher = get_object_from_list_by_id(teacher_id, teachers)
    matched_students = get_students_from_teacher(teacher)
    student_names = []
    for student in matched_students:
        student_names.append(student.name)
    return student_names


# print(student_names_from_teacher_id(int(input("student_name_from_teacher_id : "))))
print(student_names_from_teacher_id(1))
print(student_names_from_teacher_id(2))


def subject_names_from_student_id(student_id):
    student = get_object_from_list_by_id(student_id, students)
    matched_subjects = get_subjects_from_student(student)
    subject_names = []
    for subject in matched_subjects:
        subject_names.append(f"{subject.name} {subject.section}")
    return subject_names


print(subject_names_from_student_id(1))
print(subject_names_from_student_id(4))
# print(subject_names_from_student_id(int(input("subject_names_from_student_id : "))))
