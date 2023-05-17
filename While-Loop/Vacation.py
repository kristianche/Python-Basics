excursion_price = float(input())
money_in_hand = float(input())
counter_spend = 0
days = 0
while money_in_hand != excursion_price:
    data = input()
    money = float(input())
    days += 1
    if data == "spend":
        counter_spend += 1
        money_in_hand = money_in_hand - money
        if money_in_hand < 0:
            money_in_hand = 0
    else:
        money_in_hand = money_in_hand + money
    if counter_spend == 5:
        print("You can't save the money.")
        print(f"{days}")
        break
else:
    print(f"You saved the money for {days} days.")