destination = input()
while destination != "End":
    needed_money = float(input())
    money = 0
    while money < needed_money:
        current_money = float(input())
        money += current_money
    print(f"Going to {destination}!")
    destination = input()