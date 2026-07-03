def calculate_grade(scores):
    # 1. แก้ไข Bug การหารด้วยศูนย์: เช็คก่อนว่าลิสต์ว่างหรือไม่
    if not scores:
        return "No Grade", 0  # หรือส่งค่าที่เหมาะสมกลับไป
    
    total = 0
    # 2. แก้ไข Bug การย่อหน้า: ทุกอย่างในฟังก์ชันต้องย่อหน้าเข้ามา
    for score in scores:
        total = total + score
    
    average = total / len(scores)
    
    # 3. แก้ไขการย่อหน้าในส่วนของเงื่อนไข If-Else
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบการใช้งาน
scores_list = [85, 92, 78, 88, 95]
print(f"ผลลัพธ์คะแนนปกติ: {calculate_grade(scores_list)}")

# ทดสอบกรณีลิสต์ว่าง (ป้องกัน ZeroDivisionError)
print(f"ผลลัพธ์ลิสต์ว่าง: {calculate_grade([])}")
