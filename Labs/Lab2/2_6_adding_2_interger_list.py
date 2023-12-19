# กําหนดให้ list x และ y เป็น list ของจํานวนเต็ม โดยมีขนาดเท่ากัน
# ให้ return list ที่เป็นผลบวกของ list x และ y โดยใช้ list comprehension
# ให้เขียนในฟังก์ชัน function ชื่อ add2list(lst1,lst2)

def add2list(lst1, lst2):
    if (len((lst1)) != len(lst2)):
        return 'list length not equal'
    return [lst1[i] + lst2[i] for i in range(len(lst1))]


x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

print(add2list(x, y))
