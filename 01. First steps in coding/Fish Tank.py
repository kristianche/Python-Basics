lenght = int(input())
width = int(input())
height = int(input())
percent = int(input())
size = lenght * width * height
total_litres = size / 1000
occupied_space = (total_litres * percent) /100
litres = total_litres - occupied_space
print(litres)