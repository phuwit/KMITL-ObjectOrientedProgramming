# จงเขียนโปรแกรมที่คํานวณค่าของ a+aa+aaa+aaaa เมื่อรับข้อมูลเป็นตัวเลข 1 หลัก
# Input : 9
# Output : 11106 (=9+99+999+9999)

number = int(input('Enter number : '))
calculation = (1 + 11 + 111 + 1111) * number

print(calculation)