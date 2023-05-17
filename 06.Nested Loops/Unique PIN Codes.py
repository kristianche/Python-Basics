first_number_end = int(input())
second_number_end = int(input())
third_number_end = int(input())
for first_digit in range(1, first_number_end + 1):
    if first_digit % 2 == 0:
      for second_digit in range(1, second_number_end + 1):
        if second_digit == 2 or second_digit == 3 or second_digit == 5 or second_digit == 7:
          for third_digit in range(1, third_number_end + 1):
            if third_digit % 2 == 0:
                print(f"{first_digit} {second_digit} {third_digit} ")




