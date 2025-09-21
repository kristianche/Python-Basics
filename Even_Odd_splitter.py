import time

print('### Welcome to Even and Odd Splitter!                                                                 ###')

time.sleep(1)

print('### In this console app you will give a numbers and the program will separate them into even and odd! ###')

time.sleep(2.5)

print('### Enjoy! Created by kristianche/2025')

time.sleep(1)


def check_and_separate(number, odd_nums, even_nums):
    if number % 2 == 0:
        even_nums.append(number)
        print(f'The number {number} was added successfully to the Even Numbers!')
    else:
        odd_nums.append(number)
        print(f'The number {number} was added successfully to the Odd Numbers!')


def main():
    amount_of_numbers = int(input('Enter the total amount of numbers: '))
    even_nums = []
    odd_nums = []

    for i in range(amount_of_numbers):
        number = int(input('Enter your number: '))

        if not((number in even_nums) or (number in odd_nums)):
            check_and_separate(number, odd_nums, even_nums)
        else:
            print('It looks like this number was already given!')
            number = int(input('Enter your number: '))

            while True:
                if not((number in even_nums) or (number in odd_nums)):
                    check_and_separate(number, odd_nums, even_nums)
                    break

                print('It looks like this number was already given!')
                number = int(input('Enter your number: '))

    print(f"Even Numbers: {(', ').join([str(num) for num in even_nums])}")
    print(f"Odd Numbers: {(', ').join([str(num) for num in odd_nums])}")



main()