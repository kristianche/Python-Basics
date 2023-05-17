
the_best_player = 0
most_goals = 0
made_a_hat_trick = False
name = input()
while name != "End":
    goals = int(input())
    if goals >= 10:
        break
    if most_goals < goals:
        most_goals = goals
        the_best_player = name
    if goals >= 3:
        made_a_hat_trick = True
        name = the_best_player
    name = input()
if made_a_hat_trick:
    print(f"{the_best_player} is the best player!")
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"{the_best_player} is the best player!")
    print(f"He has scored {most_goals} goals.")