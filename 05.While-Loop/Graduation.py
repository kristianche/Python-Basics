name = input()
class_count = 1
bad_grades_count = 0
sum = 0
average_sum = 0
excluded = 0
while class_count <= 12:
    grade = float(input())
    sum = sum + grade
    if grade <= 4.00:
        bad_grades_count += 1
    if bad_grades_count > 1:
        excluded = class_count - 1
        print(f"{name} has been excluded at {excluded} grade")
        break
    class_count += 1
else:
    average_sum = sum / 12
    print(f"{name} graduated. Average grade: {average_sum:.2f}")
