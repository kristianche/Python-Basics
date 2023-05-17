fruit = input()
day = input()
amount = float(input())
price = 0
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.50
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "apple":
        price = 1.20
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "orange":
        price = 0.85
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "kiwi":
        price = 2.70
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "pineapple":
        price = 5.50
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "grapes":
        price = 3.85
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.70
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "apple":
        price = 1.25
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "orange":
        price = 0.90
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "kiwi":
        price = 3.00
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "pineapple":
        price = 5.60
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    elif fruit == "grapes":
        price = 4.20
        total_sum = amount * price
        print(f"{total_sum:.2f}")
    else:
        print("error")
else:
    print("error")
