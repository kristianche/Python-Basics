import random
import time

print('### Welcome to Dice Roll Simulator!                                  ###')

time.sleep(1.5)

print('### In this console app you can simulate a dice roll.                ###')

time.sleep(1.5)

print('### You can choose the amount of dices which will be thrown (1 or 2) ###')

time.sleep(1)

command = input('Select the number of dices ("Stop" -> if you want to stop the program): ')


def roll_dice():
    print(random.randint(1, 6))


while True:

    if command == 'Stop':
        break

    number_of_dices = int(command)

    if number_of_dices == 2:
        roll_dice()
        roll_dice()

    elif number_of_dices == 1:
        roll_dice()

    else:
        print('Invalid Input (0, 1 or "Stop")')

    command = input('Select the number of dices ("Stop" -> if you want to stop the program): ')

print('Thank you for using my app! :)')