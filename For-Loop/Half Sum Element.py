import sys
n = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(1, n + 1):
    number = int(input())
    sum = sum + number
    if number > max_num:
        max_num = number
others_num_sum = sum - max_num
if others_num_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - others_num_sum)
    print("No")
    print(f"Diff = {diff}")