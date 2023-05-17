total = 0
while True:
    money = input()
    if money == "NoMoreMoney":
        break

    money = float(money)
    if money < 0:
        print("Invalid operation!")
        break
    else:
        total += money
        print(f"Increase: {money:.2f}")
print(f"Total: {total:.2f}")

