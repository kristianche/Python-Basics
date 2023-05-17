bags_price_above_20kg = float(input())
bags_kg = float(input())
days = int(input())
bags_count = int(input())
bags_price = 0

if bags_kg < 10:
    bags_price = 0.2 * bags_price_above_20kg
elif 10 <= bags_kg <= 20:
    bags_price = bags_price_above_20kg * 0.5
elif bags_kg > 20:
    bags_price = bags_price_above_20kg

if days > 30:
    bags_price = bags_price + bags_price * 0.1
elif 7 <= days <= 30:
    bags_price = bags_price + bags_price * 0.15
else:
    bags_price = bags_price + bags_price * 0.4

total_price = bags_price * bags_count
print(f"The total price of bags is: {total_price:.2f} lv.")

