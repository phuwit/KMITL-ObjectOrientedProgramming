# ให้เขียน function ชื่อ day_of_year(day, month ,year)
# โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year
# – ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน
# – ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year เรียกใช้ is_leap อีกที

# จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
# – รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น
# date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
# date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
# – ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ป– ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
# – ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ

# จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff เพิ่มเติม โดยให้มีการตรวจสอบ
# – วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ
# – เดือนต้องอยู่ระหว่าง 1-12
# – เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้
# – หากข้อมูล Input ผิดพลาด ให้ Return -1

days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def validate_input(day, month, year):
    if not (1 <= month <= 12):
        return True
    if (month != 2) and not (1 <= day <= days_in_month[month - 1]):
        return True
    if (not is_leap(year) and month == 2 and day >= 29):
        return True


def is_leap(year):
    # Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
    # but these centurial years are leap years if they are exactly divisible by 400.
    # For example, the years 1700, 1800, and 1900 are not leap years, but the year 2000 is.
    if (year % 4 == 0):
        if (year % 400 == 0):
            return True
        elif (year % 100 == 0):
            return False
        else:
            return True

    else:
        return False


def day_of_year(day, month, year):
    total_days = day
    for i in range(month - 1):
        total_days += days_in_month[i]

    if (is_leap(year) and month >= 3):
        total_days += 1

    return total_days


def split_date_string(date_string):
    day, month, year = (int(n) for n in date_string.split('-'))
    return (day, month, year)


def day_in_year(year):
    days = 365
    if (is_leap(year)):
        days += 1
    return days


def date_diff(date1_string, date2_string):
    date1_day, date1_month, date1_year = split_date_string(date1_string)
    date2_day, date2_month, date2_year = split_date_string(date2_string)

    if ((validate_input(date1_day, date1_month, date1_year))
            or (validate_input(date2_day, date2_month, date2_year))):
        return -1

    date1_days_since_newyear = day_of_year(date1_day, date1_month, date1_year)
    date2_days_since_newyear = day_of_year(date2_day, date2_month, date2_year)
    years_difference = date2_year - date1_year

    if (years_difference):
        # days until end of year
        days_difference = (date2_days_since_newyear + (day_in_year(date1_year) - date1_days_since_newyear))
        # days between years
        for year in range(date1_year + 1, date2_year):
            days_difference += day_in_year(year)

    else:
        days_difference = date2_days_since_newyear - date1_days_since_newyear

    return (days_difference + 1)
