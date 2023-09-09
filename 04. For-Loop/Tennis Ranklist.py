
import math
tournament_count = int(input())
init_points = int(input())
win_count = 0
total_sum = init_points
for i in range(1, tournament_count + 1):
    level = input()
    if level == "W":
        win_count = win_count + 1
        total_sum = total_sum + 2000
    elif level == "F":
        total_sum = total_sum + 1200
    elif level == "SF":
        total_sum = total_sum + 720
print(f"Final points: {total_sum}")
points_without_init = total_sum - init_points
avg_points = math.floor(points_without_init / tournament_count)
print(f"Average points: {avg_points}")
percent_win = win_count / tournament_count * 100
print(f"{percent_win:.2f}%")