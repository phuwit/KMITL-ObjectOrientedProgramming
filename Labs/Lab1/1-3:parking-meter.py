# ให้รับเวลาเข้าและออกของรถให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้น
# คํานวณค่าที่จอดรถที่ต้องจ่าย โดยหลักเกณฑ์การคํานวณมีดังนี้
# 1) จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
# 2) จอดรถเกิน 15 นาที แต่ไม่เกิน 4 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
# 3) จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
# 4) จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
# 
# ข้อมูลนําเข้า
# มี 1 บรรทัด แต่ละบรรทัดมีจํานวนเต็ม 4 จํานวนคั่นด้วย Space
# โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก
# ข้อมูลส่งออก
# มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจํานวนเต็ม
# |    Input   | Output |
# |------------|--------|
# |  7 0 7 15  |   0    |
# |  7 0 7 16  |  10    |
# | 7 30 10 30 |  30    |
# | 7 30 10 31 |  50    |
# | 7 30 13 31 |  200   |

input_string = input('')
start_hour, start_minute, stop_hour, stop_minute = [int (i) for i in input_string.split()]

start_epoch = (start_hour * 60) + start_minute
stop_epoch = (stop_hour * 60) + stop_minute
parking_time = stop_epoch - start_epoch
print(parking_time)

if  not (0 <= start_hour <= 23) or \
    not (0 <= stop_hour <= 23) or \
    not (0 <= start_minute <= 60) or \
    not (0 <= stop_minute <= 60):
    print('invalid time')
    quit()
    
if ((start_epoch > (23 * 60)) or (stop_epoch > (23 * 60)) or \
    (start_epoch < (5 * 60)) or (stop_epoch < (5 * 60)) or \
    (parking_time < 0)):
    print('overnight parking is not allowed')
    quit()

cost = 0

if (parking_time > (6 * 60)) :
    cost = 200
elif (parking_time <= 15) :
    cost = 0
else:
    while (parking_time > 0):
        if (parking_time > (3 * 60)) :
            cost += 20
        else :
            cost += 10
            
        parking_time -= 60

print(cost)