print('####                    Welcome to Calculator!                      ####')
print('####            This is a simple calculator console app.            ####')
print('####                   Created by kristianche/2025                  ####')
print('####       When you wish to stop using it just type: "End"          ####')

command = input('Insert operation( + - * / ) or type "End":  ')

while True:

    if command == 'End':
        break

    operation = command

    if operation == '+':
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))

        result = first_number + second_number

        print(result)

    elif operation == '-':
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))

        result = first_number - second_number

        print(result)

    elif operation == '*':
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))

        result = first_number * second_number

        print(result)

    elif operation == '/':
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))

        if second_number == 0.0:
            print('Division by ZERO is not possible!!!')
        else:
            result = first_number / second_number

            print(result)

    else:
        print('Invalid Operation. Try one from the valid ones ( + - * / )')

    command = input('Insert operation( + - * / ) or type "End":  ')

print('Thank you a lot for using my Calculator. I hope you enjoyed it! :)')


