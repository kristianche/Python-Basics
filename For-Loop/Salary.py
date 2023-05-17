tabs_open = int(input())
salary = int(input())
get_money = 0
salary_two = 0
for i in range(1, tabs_open + 1):
    website = input()
    if website == "Facebook":
        get_money = get_money + 150
    elif website == "Instagram":
        get_money = get_money + 100
    elif website == "Reddit":
        get_money = get_money + 50
end = salary - get_money
if end <= 0:
    print("You have lost your salary.")
else:
    salary_two = abs(salary - get_money)
    print(f"{salary_two}")