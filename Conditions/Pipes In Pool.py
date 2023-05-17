V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())
P1_filled = P1 * H
P2_filled = P2 * H
water_amount = P1_filled + P2_filled
if water_amount <= V:
    percent_water = (water_amount / V) * 100
    percent_P1 = (P1_filled / water_amount) * 100
    percent_P2 = (P2_filled / water_amount) * 100
    print(f"The pool is {percent_water:.2f}% full. Pipe 1: {percent_P1:.2f}%. Pipe 2: {percent_P2:.2f}%.")
else:
    overflows = water_amount - V
    print(f"For {H} hours the pool overflows with {overflows:.2f} liters.")