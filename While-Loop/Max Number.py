num = input()
max = -10000000000000
while num != "Stop":
    num = int(num)
    if num > max:
        max = num
    num = input()
print(max)

