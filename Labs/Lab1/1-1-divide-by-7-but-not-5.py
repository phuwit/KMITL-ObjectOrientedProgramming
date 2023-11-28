# จงเขียนโปรแกรมที่จะหาตัวเลขระหว่าง 2000-3200 ที่หารด้วย 7 ลงตัว แต่หารด้วย 5 ไม่ลงตัว
# การแสดงผลให้แสดงตัวเลขและคั่นด้วยเครื่องหมาย , ในบรรทัดเดียว

start_num = 2000
end_num = 3200

divisible_by_7_but_not_5 = []

while ((start_num % 7) != 0):
    start_num += 1

for i in range(start_num, end_num + 1, 7):
    if (i % 5 != 0):
        divisible_by_7_but_not_5.append(i);
        
for i in divisible_by_7_but_not_5:
    print(i, end=', ')