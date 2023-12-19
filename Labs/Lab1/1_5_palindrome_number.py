# ตัวเลข palindrome คือตัวเลขที่อ่านได้ทั้ง 2 ทาง แล้วมีค่าเท่ากัน เช่น 9009 โดย 9009 คือ palindrome
# ที่เกิดจากการคูณของตัวเลข 2 หลักที่มากที่สุด คือ 91x99 จงหา palindrome ที่มากที่สุดของตัวเลข 3 หลัก

palindrome = 0
components = []

for i in range(2, 1000):
    for j in range(i, 1000):
        product = i * j
        if not (100000 <= product <= 1000000):
            break
        
        if (((product // 100000) % 10 == (product // 1) % 10) and \
            ((product // 10000) % 10 == (product // 10) % 10) and \
            ((product // 1000) % 10 == (product // 100) % 10)):
            # print('istrue')
            if (product > palindrome):
                palindrome = product
                components = [j, i]

print(palindrome)
for i in components:
    print(i)