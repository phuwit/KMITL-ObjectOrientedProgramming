# เขียนฟังก์ชัน char_count(str) โดยรับพารามิเตอร์ 1 ตัว เป็นข้อมูลชนิด string และให้ส่งคืนเป็น
# dictionary ที่มี key เป็นตัวอักษรแต่ละตัวของ string นั้น และ value คือ จํานวนครั้งที่ตัวอักษรนั้นปรากฏ
# ใน string เช่น
# Input : 'language'
# return : {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1}


def char_count(string):
    character_count = {}
    for character in string:
        if not(character_count.get(character)):
            character_count[character] = 0
        character_count[character] += 1
    return character_count
