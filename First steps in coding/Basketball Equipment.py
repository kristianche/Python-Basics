annual_fee = int(input())
shoes = annual_fee - ((40 * annual_fee)/100)
kit = shoes - ((20 * shoes)/100)
ball = kit / 4
accessories = ball / 5
total_sum = annual_fee + shoes + kit + ball + accessories
print(total_sum)