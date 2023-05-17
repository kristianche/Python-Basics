first_letter = input()
second_letter = input()
useless_letter = input()
counter = 0
letters = ["first"]
for i in range(first_letter, second_letter + 1):
    for j in range(first_letter, second_letter + 1):
        for h in range(first_letter, second_letter + 1):
            counter += 1
            print(f"{i}{j}{h}")
            print(counter)