pens_bags_count = int(input())
markers_bags_count = int(input())
preparation = int(input())
percent_discount = int(input())
price_p = pens_bags_count * 5.80
price_m = markers_bags_count * 7.20
price_pr = preparation * 1.20
sum = price_p + price_m + price_pr
discount = (percent_discount * sum) / 100
total_sum = sum - discount
print(total_sum)

