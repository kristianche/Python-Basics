rent = int(input())
statues = rent - 0.3 * rent
catering = statues - 0.15 * statues
sound = catering / 2
total_price = rent + statues + catering + sound
print(f"{total_price:.2f}")