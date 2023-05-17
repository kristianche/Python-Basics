import math
serial_name = input()
episode_time = int(input())
break_time = int(input())
lunch_time = break_time / 8
relax_time = break_time / 4
time = break_time - lunch_time - relax_time
diff = abs(episode_time - time)
rounded = math.ceil(diff)
if time >= episode_time:
    print(f"You have enough time to watch {serial_name} and left with {rounded}minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {rounded} more minutes.")