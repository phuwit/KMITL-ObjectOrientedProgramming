# กําหนดให้ List x เก็บ String และตัวแปร c เก็บตัวอักษร
# ให้สร้าง List d ที่เก็บจํานวนครั้งที่ตัวอักษรใน c ปรากฏในแต่ละ String ของ List x โดยใช้ List
# comprehension
# – เช่น x = [‘abba’, ‘babana’, ‘ann’]; c = ‘a’
# – จะได้ d = [2, 3, 1]
# ให้สร้างเป็น function count_char_in_string(x,c) แล้ว return เป็น List คําตอบ

def count_char_in_string(x, c):
    return [sum(1 for matched_char in string if matched_char == c) for string in x]


print(count_char_in_string(input(), input()))
