name = 0
the_best_player = 0
most_goals = 0
made_a_hat_trick = False
goals = 0
while goals < 10:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if most_goals < goals:
        most_goals = goals
        the_best_player = name
    if goals >= 3:
        made_a_hat_trick = True
        name = the_best_player
if made_a_hat_trick:
    print(f"{the_best_player} is the best player!")
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"{the_best_player} is the best player!")
    print(f"He has scored {most_goals} goals.")