goal = 10000
steps = 0
sum = 0
while sum < 10000:
    steps = input()
    if steps != "Going home":
      steps = int(steps)
      sum += steps
    if steps == "Going home":
        steps_to_home = int(input())
        sum += steps_to_home
        if sum < 10000:
            needed_steps = abs(10000 - sum)
            print(f"{needed_steps} more steps to reach goal.")
            break
        else:
            over = sum - 10000
            print("Goal reached! Good job!")
            print(f"{over} steps over the goal!")
            break
else:
    over = sum - 10000
    print("Goal reached! Good job!")
    print(f"{over} steps over the goal!")

