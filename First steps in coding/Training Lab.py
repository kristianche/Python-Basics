w = float(input())
h = float(input())
w_cent = w * 100
h_cent = h * 100
zala_bez_koridor = h_cent - 100
desks_count = zala_bez_koridor // 70
rows_count = w_cent // 120
places_count = rows_count * desks_count - 3
print(places_count)