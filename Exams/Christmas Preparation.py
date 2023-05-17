wrapping_paper_count = int(input())
cloth_count = int(input())
glue_litres = float(input())
discount = int(input())
wrapping_paper_price = wrapping_paper_count * 5.80
cloth_price = cloth_count * 7.20
glue_price = glue_litres * 1.20
total_price = wrapping_paper_price + cloth_price + glue_price
total_price = total_price - ((discount * total_price) / 100)
print(f"{total_price:.3f}")