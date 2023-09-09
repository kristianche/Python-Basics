money = float(input())
year_to_live = int(input())
years_old = 17
spend_money = 0
new_money = 0
for year in range(1800, year_to_live + 1):
    years_old += 1
    if year % 2 == 0:
        spend_money = spend_money + 12000
        new_money = money - spend_money
    else:
        spend_money = spend_money + 12000 + 50 * years_old
        new_money = money - spend_money
if new_money <= money:
    needed_money = abs(money - new_money)
    print(f"He will need {needed_money:.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {new_money:.2f} dollars left.")

