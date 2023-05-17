count_joinery = int(input())
size = input()
delivery = input()
price = 0
if size == "90X130":
    price = count_joinery * 110
    if 30 < count_joinery <= 60:
        price = price - 0.05 * price
    elif count_joinery > 60:
        price = price - 0.08 * price
elif size == "100X150":
    price = count_joinery * 140
    if 40 < count_joinery <= 80:
        price = price - 0.06 * price
    elif count_joinery > 80:
        price = price - 0.1 * price
elif size == "130X180":
    price = count_joinery * 190
    if 20 < count_joinery <= 50:
        price = price - 0.07 * price
    elif count_joinery > 50:
        price = price - 0.12 * price
elif size == "200X300":
    price = count_joinery * 250
    if 25 < count_joinery <= 50:
        price = price - 0.09 * price
    elif count_joinery > 50:
        price = price - 0.14 * price

if delivery == "With delivery":
    price += 60
if count_joinery > 99:
    price = price - 0.04 * price

if count_joinery < 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")