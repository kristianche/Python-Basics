num = int(input())

bonus_points = 0
if num <= 100:
    bonus_points = 5
elif num <= 1000:
    bonus_points = num * 0.20
else:
    bonus_points = num * 0.10

if num % 2 == 0:
    bonus_points = bonus_points + 1

if num % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(num + bonus_points)