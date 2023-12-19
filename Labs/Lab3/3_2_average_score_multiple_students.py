# From 3-1

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

# ให้นําโปรแกรมตามข้อ 1 มาขยายความสามารถให้รองรับนักศึกษาหลายคน โดยให้ refactor ฟังก์ชัน
# add_score ให้รับพารามิเตอร์เป็น add_score(subject_score, student, subject, score) โดย student
# เป็นข้อมูลของนักศึกษาเป็น string (ในที่นี้เป็น id) และ return เป็น dictionary
# Input : subject_score = { }, student = '65010001', subject = 'python', score = 50
# return : { '65010001' : { 'python' : 50 } }
# input : subject_score = { '65010001' : { 'python' : 50 } },
# student = '65010001', subject = ‘calculus’, score = 60
# return : {'65010001': {'python’: 50, 'calculus', 60} }
# โดยหากชื่อมีข้อมูล key ใดที่มีใน dictionary อยู่แล้ว ให้ถือเป็นการ update ข้อมูลนั้น
# ให้ refactor ฟังก์ชัน calc_average_score โดยให้ส่งคืนเป็น dictionary ของนักศึกษาและคะแนนเฉลี่ย
# ของนักศึกษาคนนั้น เช่น {'65010001': '55.00' }