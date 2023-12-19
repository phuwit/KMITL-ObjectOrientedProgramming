# ให้เขียนโปรแกรมรับข้อมูล 1 บรรทัด ประกอบด้วยตัวเลข 1 หลัก จํานวนไม่เกิน 10 ตัว คั่นด้วยช่องว่าง
# จากนั้นให้นําตัวเลขที่รับเข้ามาเรียงกัน และหาลําดับการเรียงที่ทําให้มีค่าน้อยที่สุด โดยต้องไม่ขึ้นต้นด้วย 0
# Input : 9 4 6 2 คําตอบ 2469, Input : 3 0 8 1 3 3 คําตอบ : 103338


def swap_zero_with_first_non_zero(list_to_swap):
    # if the first letter is zero
    if (list_to_swap[0] == '0'):
        for i in range(1, len(list_to_swap)):
            if (list_to_swap[i] != '0'):
                # swap it
                list_to_swap[0], list_to_swap[i] = list_to_swap[i], list_to_swap[0]
                return


sorted_input_list = sorted(n for n in input().split())
swap_zero_with_first_non_zero(sorted_input_list)

print(''.join(sorted_input_list))


