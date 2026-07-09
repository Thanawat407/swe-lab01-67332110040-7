def calculate_grade(scores):
    total = 0
    for score in scores:
        total = total + score
        
    average = total / len(scores)
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

# ขั้นที่ 2: รันกรณีปกติที่มีคะแนน
scores = [85, 92, 78, 88, 95]
print(calculate_grade(scores))

# ขั้นที่ 4: ลองกรณีที่ไม่มีคะแนนเลย (จะเกิด Error สีแดง พังตรง len(scores) เป็น 0)
# print(calculate_grade([])) 
