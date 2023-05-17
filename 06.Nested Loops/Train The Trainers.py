number_of_jury = int(input())
number_of_presentations = 0
final_grade = 0
command = input()
while command != "Finish":
    number_of_presentations += 1
    current_presentation_name = command
    current_presentation_grade = 0
    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        current_presentation_grade += current_grade
    current_presentation_average_grade = current_presentation_grade / number_of_jury
    print(f"{current_presentation_name} - {current_presentation_average_grade:.2f}.")
    final_grade += current_presentation_average_grade
    command = input()
final_average_grade = final_grade / number_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")