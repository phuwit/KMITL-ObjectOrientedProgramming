from __future__ import annotations
from enum import Enum


class Grade(Enum):
    A = 4
    B = 3
    C = 2
    D = 1
    F = 0


class Student:
    def __init__(self, student_id, student_name):
        self.__id: str = student_id
        self.__name: str = student_name
        
    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    # def set_id(self, id):
    #     if (type(id) == int):
    #         self.__id = int(id)
    #         return True
    #     else:
    #         return False
    
    # def set_name(self, name):
    #     if(str(name).isalnum()):
    #         self.__stu_name = str(name)
    #         return True
    #     else:
            # return False


class Subject:
    def __init__(self, subject_id, subject_name, credit):
        self.__id: str = subject_id
        self.__name: str = subject_name
        self.__credit: int = credit

    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_teacher(self) -> Teacher:
        return self.__teacher
    
    def get_credit(self) -> int:
        return self.__credit
        
    # def get_student_list(self):
    #     return self.__student_list
    
    # def set_id(self, id):
    #     if (type(id) == int):
    #         self.__id = int(id)
    #         return True
    #     else:
    #         return False
    
    # def set_name(self, name):
    #     if(str(name).isalnum()):
    #         self.__name = str(name)
    #         return True
    #     else:
    #         return False
        
    def assign_teacher(self, teacher: Teacher) -> bool:
        if (isinstance(teacher, Teacher)):
            self.__teacher = teacher
            return True
        else:
            return False
        
    # def set_student_list(self, students):
    #     self.__student_list = students
        
    # # def extend_student_list(self, students):
    # #     self.__student_list = students

    # def add_student(self, student_instance):
    #     self.__student_list.append(student_instance)
        

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.__id: str = teacher_id
        self.__name: str = teacher_name
        
    # def get_id(self):
    #     return self.__id
    
    def get_name(self):
        return self.__name
    
    # def set_id(self, id):
    #     if (type(id) == int):
    #         self.__id = int(id)
    #         return True
    #     else:
    #         return False
    
    # def set_name(self, name):
    #     if(str(name).isalnum()):
    #         self.__name = str(name)
    #         return True
    #     else:
    #         return False
        
        
class Enrollment:
    def __init__(self, student, subject):
        self.__student: Student = student
        self.__subject: Subject = subject
        self.__grade: Grade | None = None
    
    def get_student(self) -> Student:
        return self.__student
    
    def get_subject(self) -> Subject:
        return self.__subject
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade: Grade) -> bool:
        if (self.__grade):
            return False
        
        if (isinstance(grade, Grade)):
            self.__grade = grade
            return True
        else: 
            return False
    

def get_objects_from_list_by_id(id, list):
    # objects = []
    for element in list:
        if (element.get_id() == id):
            return element
    # return objects

# def get_students_from_teacher(teacher):
#     matched_students = []
#     for subject in subject_list:
#         if (teacher == subject.get_teacher()):
#             matched_students.extend(subject.get_student_list())
#     return matched_students

# def get_subjects_from_student(student):
#     matched_subjects = []
#     for subject in subject_list:
#         if student in subject.get_student_list():
#             matched_subjects.append(subject)
#     return matched_subjects

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id: str):
    return get_objects_from_list_by_id(subject_id, subject_list)

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id: str):
    return get_objects_from_list_by_id(student_id, student_list)

def match_enrollment(student: Student, subject: Subject):
    for enrollment in enrollment_list:
        if (enrollment.get_student() == student) and (enrollment.get_subject() == subject):
            return enrollment
    return 

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(student: Student, subject: Subject):
    for enrollment in enrollment_list:
        if (enrollment.get_student() == student) and (enrollment.get_subject() == subject):
            return enrollment
    return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student: Student, subject: Subject):
    if not (isinstance(student, Student) or isinstance(subject, Subject)):
        return 'Error'
    
    matched_enrollment = search_enrollment_subject_student(student, subject);
    if (matched_enrollment):
        return 'Already Enrolled'
    else:
        enrollment_list.append(Enrollment(student, subject))

# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student: Student, subject: Subject):
    if not (isinstance(student, Student)) or not (isinstance(subject, Subject)):
        return 'Error'
    
    matched_enrollment = search_enrollment_subject_student(student, subject);
    if (matched_enrollment):
        enrollment_list.remove(matched_enrollment)
        return 'Done'
    else:
        return 'Not Found'

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject: Subject):
    matched_enrollments = []
    for enrollment in enrollment_list:
        if (enrollment.get_subject() == subject):
            matched_enrollments.append(enrollment)
    return matched_enrollments

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student: Student):
    matched_enrollments = []
    for enrollment in enrollment_list:
        if (enrollment.get_student() == student):
            matched_enrollments.append(enrollment)
    return matched_enrollments

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student: Student, subject: Subject, grade_string: str):
    matched_enrollment: Enrollment | None = search_enrollment_subject_student(student, subject)
    if matched_enrollment is None:
        return 'Not Found'
    
    if (matched_enrollment.set_grade(Grade[grade_string])):
        return 'Done'
    else:
        return 'Error'
        

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search: Subject):
    for subject in subject_list:
        if (subject == subject_search):
            return subject.get_teacher()
    return 'Not Found'

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject: Subject):
    matched_enrollments = search_student_enroll_in_subject(subject)
    return len(matched_enrollments)

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student: Student):
    record = {}
    matched_enrollments = search_subject_that_student_enrolled(student)
    for enrollment in matched_enrollments:
        record.update({\
            str(enrollment.get_subject().get_id()) : \
                [enrollment.get_subject().get_name(), enrollment.get_grade().name]
        })
    return record

# # แปลงจาก เกรด เป็นตัวเลข
# def grade_to_count(grade):
#     grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
#     return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student: Student):
    total_weight = 0
    weighted_sum = 0
    matched_enrollments = search_subject_that_student_enrolled(student)
    for enrollment in matched_enrollments:
        total_weight += enrollment.get_subject().get_credit()
        weighted_sum += enrollment.get_subject().get_credit() * enrollment.get_grade().value
        
    return weighted_sum / total_weight

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id: str):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.get_student().get_id()] = enrollment.get_student().get_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id: str):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.get_subject().get_id()] = enrollment.get_subject().get_name()
    return subject_dict

#######################################################################################

student_list: list[Student] = []
subject_list: list[Subject] = []
teacher_list: list[Teacher] = []
enrollment_list: list[Enrollment] = []

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()

### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_id()))
print("")

### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.get_student().get_id() for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject().get_id() for i in lst])
print("")

### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).get_name())
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(student_list[1], subject_list[0])
print(enroll.get_subject().get_id(),enroll.get_student().get_id())
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1]))