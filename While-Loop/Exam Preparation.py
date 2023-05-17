bad_grades = int(input())
name = input()
grades_count = 0
number_of_problems = 0
bad_grades_counter = 0
last_problem = 0
sum = 0
average_score = 0
while name != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1
    if bad_grades_counter == bad_grades:
        print(f"You need a break, {bad_grades_counter} poor grades.")
        break
    grades_count += 1
    number_of_problems += 1
    sum += grade
    last_problem = name
    name = input()
else:
    average_score = sum / grades_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")