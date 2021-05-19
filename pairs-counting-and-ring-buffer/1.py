N = int(input())

# Массивы по критерию чётности
max_17_first = [0, 0] 
max_17_second = [0, 0]
max_not17 = [0, 0]

for i in range(N):
    x = int(input())

    k = x % 2 # Критерий чётности

    if x % 17 == 0:
        if x > max_17_first[k]:
            max_17_second[k] = max_17_first[k]
            max_17_first[k] = x
        elif x > max_17_second[k]:
            max_17_second[k] = x
    else:
        if x > max_not17[k]:
            max_not17[k] = x

a = [0, 0]
b = [0, 0]

for k in range(2):
    a[k] = max_17_first[k]
    b[k] = max(max_17_second[k], max_not17[k])

    if b[k] == 0: # Нет второго парного
        a[k] = 0

if a[0] + b[0] > a[1] + b[1]:
    print(a[0], b[0])
else:
    print(a[1], b[1])
