days = int(input())
type = input()
grade = input()
nights = days - 1
total_price = 0
if type == "room for one person":
    total_price = 18.00 * nights
elif type == "apartment":
    total_price = 25.00 * nights
    if days < 10:
        total_price = total_price - 0.30 * total_price
    elif 10 <= days <= 15:
        total_price = total_price - 0.35 * total_price
    elif days > 15:
        total_price = total_price - 0.50 * total_price
elif type == "president apartment":
    total_price = 35.00 * nights
    if days < 10:
        total_price = total_price - 0.10 * total_price
    elif 10 <= days <= 15:
        total_price = total_price - 0.15 * total_price
    elif days > 15:
        total_price = total_price - 0.20 * total_price
if grade == "positive":
    total_price = total_price + 0.25 * total_price
elif grade == "negative":
    total_price = total_price - 0.10 * total_price
print(f"{total_price:.2f}")