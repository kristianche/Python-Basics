company_name = input()
adults_tickets_count = int(input())
child_tickets_count = int(input())
adults_tickets_price = float(input())
on_your_own_price = float(input())
adults_tickets_price_two = adults_tickets_price + on_your_own_price
adults_tickets_total_price = adults_tickets_count * adults_tickets_price_two
child_tickets_price = adults_tickets_price - (0.7 * adults_tickets_price)
child_tickets_price_two = child_tickets_price + on_your_own_price
child_tickets_total_price = child_tickets_price_two * child_tickets_count
total_price = 0.2 * (child_tickets_total_price + adults_tickets_total_price)
print(f"The profit of your agency from {company_name} tickets is {total_price:.2f} lv.")
