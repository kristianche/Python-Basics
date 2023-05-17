chicken_count = int(input())
fish_count = int(input())
vegetarian_count = int(input())
price_chicken = chicken_count * 10.35
price_fish = fish_count * 12.40
price_vegetarian = vegetarian_count * 8.15
total_price = price_chicken + price_fish + price_vegetarian
dessert = (20 * total_price)/100
total_sum = total_price + dessert + 2.50
print(total_sum)