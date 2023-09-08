pages_count = int(input())
pages_per_hour = int(input())
days_count = int(input())
total_hours = pages_count // pages_per_hour
hours_per_day = total_hours // days_count
print(hours_per_day)
