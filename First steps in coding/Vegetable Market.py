N = float(input())
M = float(input())
kilo_vegetables = float(input())
kilo_fruits = float(input())
vegetables_price = kilo_vegetables * N
fruits_price = kilo_fruits * M
total_price_lv = fruits_price + vegetables_price
total_price_eu = total_price_lv / 1.94
print(f"{total_price_eu:.2f}")