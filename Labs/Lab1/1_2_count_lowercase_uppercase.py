# ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็ก หรือตัวอักษรพิมพ์ใหญ่ อย่างละกี่ตัว
# ให้ตอบ 2 บรรทัด จํานวนตัวพิมพ์เล็ก 1 บรรทัด จํานวนตัวพิมพ์ใหญ่ 1 บรรทัด

original_string = input('Enter a string : ')

uppercase_count = 0
lowercase_count = 0

for character in original_string:
    if (character.isupper()):
        uppercase_count += 1
    elif (character.islower()):
        lowercase_count += 1
        
print('Uppercase :', uppercase_count)
print('Lowercase :', lowercase_count)