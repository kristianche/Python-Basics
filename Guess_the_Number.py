import random
import time

print('### Welcome to this simple console game!                                                             ###')

time.sleep(2)

print('### Here are the rules:                                                                              ###')

time.sleep(1)

print('### Every time the computer will generate a random number (1 - 100)                                  ###')

time.sleep(1)

print('### Then you need to choose between the difficulty you want to play (Normal or Hard)                 ###')

time.sleep(2)

print('### Normal: After each one of your guesses you will get a hint whether the number is lower or higher ###')
print('### Hard: You play the game without any hints.                                                       ###')

time.sleep(1)

print('### Created by kristianche/2025                                                                      ###')

print()

time.sleep(1)


def hard_mode():
    number = random.randint(1, 100)
    guesses_counter = 0

    guess = int(input('Take a guess: '))

    while True:

        guesses_counter += 1

        if number == guess:
            print(f'Congratulations! You have guessed the number: {number}')
            print(f'Total guesses: {guesses_counter}')
            break

        guess = int(input('Take a guess: '))


def normal_mode():
    number = random.randint(1, 100)
    guesses_counter = 0

    guess = int(input('Take a guess: '))

    while True:

        guesses_counter += 1

        if guess == number:
            print(f'Congratulations! You have guessed the number: {number}')
            print(f'Total guesses: {guesses_counter}')
            break

        if guess > number:
            print('Lower ↓')

        else:
            print('Higher ↑')

        guess = int(input('Take a guess: '))


command = input('Choose game mode (Normal, Hard) -> Type "End" if you wish to stop the game: ')

while True:

    if command == 'End':
        print()
        break

    if command == 'Hard':
        hard_mode()
        print()

    elif command == 'Normal':
        normal_mode()
        print()

    command = input('Choose game mode (Normal, Hard) -> Type "End" if you wish to stop the game: ')


print('Thanks for playing! I hope you enjoyed it!')





