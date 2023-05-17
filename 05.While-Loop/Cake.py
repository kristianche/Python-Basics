lenght = int(input())
width = int(input())
pieces = lenght * width
pieces_left = pieces
take = 0
while pieces_left > 0:
    take = input()
    if take == "STOP":
        print(f"{pieces_left} pieces are left.")
        break
    take = int(take)
    pieces_left = pieces_left - take
else:
    needed_pieces = abs(pieces_left)
    print(f"No more cake left! You need {needed_pieces} pieces more.")