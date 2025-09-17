import time

print('### Welcome to Clock!                                     ###')

time.sleep(1.5)

print('### This is a console application which simulates a Timer ###')

time.sleep(2.5)

print('### Enjoy :)                                              ###')

time.sleep(1)


def timer():
    hours = int(input('Hours: '))
    minutes = int(input('Minutes: '))
    seconds = int(input('Seconds: '))

    total_seconds = (hours * 60) * 60 + minutes * 60 + seconds

    for s in range(total_seconds, 0, -1):
        hours_for_print = s // 3600
        minutes_for_print = (s % 3600) // 60
        seconds_for_print = s % 60

        print(f"{hours_for_print:02d}:{minutes_for_print:02d}:{seconds_for_print:02d}")
        time.sleep(1)

    print("Time's up! ⏰")


timer()