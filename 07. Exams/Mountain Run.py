record_in_seconds = float(input())
distance = float(input())
time_in_sec_per_1meter = float(input())
slow_count = distance // 50
slow = slow_count * 30
new_time = distance * time_in_sec_per_1meter
time = new_time + slow
if time >= record_in_seconds:
    seconds_slower = abs(record_in_seconds - time)
    print(f"No! He was {seconds_slower:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {time:.2f} seconds.")