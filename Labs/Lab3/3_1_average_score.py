# เขียนฟังก์ชัน add_score(subject_score, subject, score) โดยมีพารามิเตอร์ 3 ตัว ได้แก่ subject_score
# เป็น dictionary ที่มีคู่ key : value เป็น subject : score พารามิเตอร์ตัวที่ 2 และ 3 เป็น subject และ
# score โดย subject เป็น string และ score เป็น integer โดยให้นํา subject และ score ไปเพิ่มใน
# dictionary เช่น
# Input : subject_score = { }, subject = ‘python’, score = 50
# return : { ‘python’ : 50 }
# input : subject_score = { ‘python’ : 50 }, subject = ‘calculus’, score = 60
# return : { ‘python’ : 50, ‘calculus : 60 }
# จากนั้นให้เขียนฟังก์ชัน calc_average_score หาค่าเฉลี่ยของคะแนนในทุกรายวิชาใน dictionary ที่ได้จาก
# ฟังก์ชัน add_score โดยให้ส่งค่าคืนมาเป็น string ที่มีทศนิยม 2 ตําแหน่ง


# test_subject_score = {
#     'math':  0,
#     'physics': 1,
#     'python': 2
# }


def add_score(score_list, subject_name, subject_score):
    score_list[subject_name] = subject_score


def calc_average_score(score_list):
    total_subject, total_score = [len(score_list), sum(score for (subject, score) in score_list.items())]
    return f'{total_score / total_subject:.2f}'

# print(calc_average_score(test_subject_score))
