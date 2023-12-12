# ให้เขียน function ชื่อ day_of_year(day, month ,year)
# โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year
# – ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน
# – ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year เรียกใช้ is_leap อีกที

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
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31)

    total_days = day
    for i in range(month - 1):
        total_days += days_in_month[i]

    if(is_leap(year) and month >= 3):
        total_days += 1

    return total_days


def split_date_string(date_string):
    return (int(n) for n in date_string.split('-'))


# print(day_of_year(9, 3, 2000))
day, month, year = split_date_string(input())
print(day_of_year(day, month, year))
