from math import pi
figure = input()
result = 0
if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif figure == "triangle":  # else
    side = float(input())
    height = float(input())
    result = side * height / 2
print(f"{result:.3f}")
