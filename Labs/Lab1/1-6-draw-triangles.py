# จงเขียนโปรแกรมแสดงรูปสามเหลื่ยม (ตามโปรแกรมใน Slide 5) แต่ปรับปรุงให้ใช้ Loop เพียง Loop เดียว
# 
# From slide #5
# 
# n = 10
# 
# for row in range(n):
#     for col in range(n):
#         if ((row + col) < n):
#             print(' ', end='')
#         else:
#             print('#', end='')
#     print('#')

n = 10
n += 1

for position in range(n + 2, (n ** 2) + n):
    if ((position % (n + 1) + position // (n + 1)) < (n + 1)):
        print(' ', end='')
    else:
        print('#', end='')
    
    if (position % (n + 1) == 0):
        print('')
        
# way way better solution by p'mew
    
# n = int(input("Type ur number :"))

# for i in range(1,n+1) :
#     print((" "*(n-i)) + ("*"*i))