# a = []
# n = 30
# for i in range(0, n):
#     a.append(int(input()))

# Проще можно записать так:
# n = 30
# a = [int(input()) for i in range(0, n)]

# Чтобы вручную не вводить числа, для тестирования алгоритма, можно записать:
from random import randint
n = 30
a = [randint(0, 10000) for i in range(0, n)]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

s = 0

for i in range(n):
    if a[i] < 200 and a[i] % 5 == 0:
        s += a[i]
        a[i] = -1
for i in range(n):
    if a[i] == -1:
        a[i] = s
    print(a[i])
