n = int(input())

print('+', end=' ')

for i in range(n - 2):
    print('-', end=' ')

print('+')

for k in range(n - 2):
    print('|', end=' ')
    for h in range(n - 2):
        print('-', end=' ')
    print('|', end=' ')
    print()

print('+', end=' ')

for j in range(n - 2):
    print('-', end=' ')

print('+', end='')


