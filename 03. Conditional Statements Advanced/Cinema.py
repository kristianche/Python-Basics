screen_type = input()
rows = int(input())
columns = int(input())
seats = rows * columns
if screen_type == "Premiere":
    ticket = 12.00
elif screen_type == "Normal":
    ticket = 7.50
elif screen_type == "Discount":
    ticket = 5.00
total_profit = seats * ticket
print(f"{total_profit:.2f} leva")
