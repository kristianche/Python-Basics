number_for_beggining = int(input())
number_for_end = int(input())
first_number_first_digit = number_for_beggining // 1000 % 100
first_number_second_digit = number_for_beggining // 100 % 10
first_number_third_digit = number_for_beggining // 10 % 10
first_number_fourth_digit = number_for_beggining % 10
second_number_first_digit = number_for_end // 1000 % 100
second_number_second_digit = number_for_end // 100 % 10
second_number_third_digit = number_for_end // 10 % 10
second_number_fourth_digit = number_for_end % 10
for i in range(first_number_first_digit, second_number_first_digit + 1):
    if i % 2 != 0:
      for j in range(first_number_second_digit, second_number_second_digit + 1):
           if j % 2 != 0:
            for h in range(first_number_third_digit, second_number_third_digit + 1):
             if h % 2 != 0:
                for f in range(first_number_fourth_digit, second_number_fourth_digit + 1):
                  if f % 2 != 0:
                   print(f"{i}{j}{h}{f}", end= " ")
