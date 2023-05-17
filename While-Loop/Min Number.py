num = input()
min = 10000000000000
while num != "Stop":
    num = int(num)
    if num < min:
        min = num
    num = input()
print(min)