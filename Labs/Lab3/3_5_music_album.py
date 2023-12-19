# ข้อมูลต่อไปนี้แทน music album แต่ละ album เก็บใน dictionary ซึ่งมีตัวเลข id เป็น key โดยแต่ละ album ไม่จําเป็นต้องมีข้อมูลครบ
# ให้เขียนฟังก์ชัน update_records โดยรับพารามิเตอร์ 4 ตัว คือ 1) dictionary record 2) id 3) property
# (เช่น artist หรือ tracks 4) value โดยหน้าที่ของฟังก์ชัน คือ ให้เพิ่ม/เปลี่ยน ค่า property และ value ของ
# album ของ id ที่ส่งค่าไปในฟังก์ชัน โดยมีรายละเอียดดังนี้
#     ฟังก์ชันจะต้องส่งคืนข้อมูล record ทั้งหมดกลับมา
#     ถ้า property ไม่ใช่ tracks และ value ไม่ใช่ empty string ให้ update หรือ set ข้อมูล property
#     กับ value ใน album นั้น
#     ถ้า property เป็น tracks แต่ album นั้นไม่มี tracks property ให้สร้าง List ใหม่และเพิ่มข้อมูลเข้าไป
#     ใน List นั้น
#     ถ้า property เป็น tracks และ value ไม่ใช่ empty string ให้เพิ่ม value ต่อท้ายใน List ของ tracks
#     ถ้า value เป็น empty string ให้ลบข้อมูล property นั้นออกจาก album

record_collection = {
    2548: {
        'albumTitle': 'Slippery When Wet',
        'artist': 'Bon Jovi',
        'tracks': ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
        'albumTitle': '1999',
        'artist': 'Prince',
        'tracks': ['1999', 'Little Red Corvette']
    },
    1245: {
        'artist': 'Robert Palmer',
        'tracks': []
    },
    5439: {
        'albumTitle': 'ABBA Gold'
    }
}


def create_key_if_not_found(dictionary, key, default_value):
    if not (dictionary.get(key)):
        dictionary[key] = default_value
    return dictionary


def update_records(record_dict, record_id, key, value):
    if not (record_dict.get(record_id)):
        return record_dict

    if (value == ''):
        record_dict[record_id] = create_key_if_not_found(record_dict[record_id], key, '')
        record_dict[record_id].pop(key)
    elif (key == 'tracks'):
        record_dict[record_id] = create_key_if_not_found(record_dict[record_id], key, [])
        record_dict[record_id][key].append(value)
    else:
        record_dict[record_id][key] = value

    return record_dict


print(update_records(record_collection, 2548, "artist", ""))
