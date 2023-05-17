import math
record = float(input())
distance = float(input())
meter_in_second = float(input())
time = distance * meter_in_second
delay = math.floor(distance / 15) * 12.5
total_time = time + delay
if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_slower = total_time - record
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")