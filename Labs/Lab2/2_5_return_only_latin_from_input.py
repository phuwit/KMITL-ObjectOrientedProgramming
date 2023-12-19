# ให้เขียนโปรแกรมเพื่อรับ string 1 ตัว
# ให้ส่งคืนเฉพาะตัวอักษรที่เป็นภาษาอังกฤษ โดยใช้ List comprehension
# ให้เขียนในฟังก์ชัน only_english(string1) แล้ว return เป็นคําตอบเป็น string

def only_english(string):
    return ''.join(char for char in string if char.isascii() if char.isalpha())


print(only_english(input()))