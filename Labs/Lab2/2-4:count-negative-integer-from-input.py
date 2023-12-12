# ให้เขียนโปรแกรมเพื่อรับข้อมูล 1 บรรทัด ที่ประกอบด้วยจํานวนเต็มหลายจํานวน (คั่นด้วยช่องว่าง)
# ให้ส่งคืนว่ามีจํานวนที่เป็นลบกี่จํานวน โดยใช้ List comprehension
# ให้เขียนใน2-4ฟังก์ชัน count_minus(str) แล้ว return เป็นคําตอบ

def count_minus(string):
    integer_list = convert_string_to_integer_list(string)
    return sum(1 for negative_integer in integer_list if negative_integer < 0)


def convert_string_to_integer_list(string):
    return [int(n) for n in string.split()]


print(count_minus(input()))
