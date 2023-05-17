x = float(input())
y = float(input())
h = float(input())
front_back_walls_size = ((x * x) * 2) - (1.2 * 2)
side_walls_size = ((x * y) * 2) - (2 * (1.5 * 1.5))
walls_size = front_back_walls_size + side_walls_size
green_paint = walls_size / 3.4
roof_rectangles = 2 * (x * y)
roof_triangles = 2 * ((x * h)/2)
roof_size = roof_triangles + roof_rectangles
red_paint = roof_size / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")