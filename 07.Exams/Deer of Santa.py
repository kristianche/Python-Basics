import math
days = int(input())
leaved_food = int(input())
food_for_first_deer_per_day = float(input())
food_for_second_deer_per_day = float(input())
food_for_third_deer_per_day = float(input())
food_for_first_deer = days * food_for_first_deer_per_day
food_for_second_deer = days * food_for_second_deer_per_day
food_for_third_deer = days * food_for_third_deer_per_day
total_food = food_for_first_deer + food_for_second_deer + food_for_third_deer
if total_food <= leaved_food:
    left_food = math.floor(leaved_food - total_food)
    print(f"{left_food} kilos of food left.")
else:
    needed_food = math.ceil(total_food - leaved_food)
    print(f"{needed_food} more kilos of food are needed.")