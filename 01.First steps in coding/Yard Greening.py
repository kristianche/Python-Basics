kw_meters = float(input())
price = kw_meters * 7.61
discount = 0.18 * price
final_price = price - discount
print(f"Your final price is: {final_price}")
print(f"Your discount is: {discount}")