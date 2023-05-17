product = input()
city = input()
amount = float(input())
price = 0
if city == "Sofia":
    if product == "coffee":
        price = 0.50
        total_sum = amount * price
        print(total_sum)
    elif product == "water":
        price = 0.80
        total_sum = amount * price
        print(total_sum)
    elif product == "beer":
        price = 1.20
        total_sum = amount * price
        print(total_sum)
    elif product == "sweets":
        price = 1.45
        total_sum = amount * price
        print(total_sum)
    elif product == "peanuts":
        price = 1.60
        total_sum = amount * price
        print(total_sum)
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
        total_sum = amount * price
        print(total_sum)
    elif product == "water":
        price = 0.70
        total_sum = amount * price
        print(total_sum)
    elif product == "beer":
        price = 1.15
        total_sum = amount * price
        print(total_sum)
    elif product == "sweets":
        price = 1.30
        total_sum = amount * price
        print(total_sum)
    elif product == "peanuts":
        price = 1.50
        total_sum = amount * price
        print(total_sum)
elif city == "Varna":
    if product == "coffee":
        price = 0.45
        total_sum = amount * price
        print(total_sum)
    elif product == "water":
        price = 0.70
        total_sum = amount * price
        print(total_sum)
    elif product == "beer":
        price = 1.10
        total_sum = amount * price
        print(total_sum)
    elif product == "sweets":
        price = 1.35
        total_sum = amount * price
        print(total_sum)
    elif product == "peanuts":
        price = 1.55
        total_sum = amount * price
        print(total_sum)