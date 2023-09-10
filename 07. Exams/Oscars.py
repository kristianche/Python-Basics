actor_name = input()
points_from_academy = float(input())
counts_judges = int(input())
points = points_from_academy
for great in range(counts_judges):
    name = input()
    great_points = float(input())
    current_points = (len(name) * great_points) / 2
    points += current_points
    if points >= 1205.05:
        break
if points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    needed_points = 1250.5 - points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")