hours = int(input())
minutes = int(input())
new_minutes = 15 + minutes
if new_minutes >= 60:
    hours = hours + 1
    new_minutes = new_minutes - 60

if hours >= 24:
    hours = 0

if new_minutes <= 9:
    print(f"{hours}:0{new_minutes}")
else:
    print(f"{hours}:{new_minutes}")
