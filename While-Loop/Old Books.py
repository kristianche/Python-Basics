fav_book = input()
books_count = 0
current_book = input()
is_found_book = False
while current_book != "No More Books":
    books_count += 1
    current_book = input()
    if current_book == fav_book:
        is_found_book = True
        print(f"You checked {books_count} books and found it.")
        break
if not is_found_book:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
