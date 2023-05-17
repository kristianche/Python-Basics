computers_count = int(input())
total_rating = 0
total_sold = 0
for i in range(computers_count):
    current_model = int(input())
    rating = current_model % 10
    possible_sells = current_model // 10
    if rating == 2:
        sold = 0
    elif rating == 3:
        sold = 0.50 * possible_sells
    elif rating == 4:
        sold = 0.70 * possible_sells
    elif rating == 5:
        sold = 0.85 * possible_sells
    elif rating == 6:
        sold = possible_sells
    total_sold += sold
    total_rating += rating
average_rating = total_rating / computers_count
print(f"{total_sold:.2f}")
print(f"{average_rating:.2f}")