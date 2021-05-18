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
a = [randint(0, 100) for i in range(0, n)]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

s = 0.0

for i in range(0, n):
    s += a[i]
s = s / n;

j = 0

for i in range(0, n):
    if a[i] > s:
        j += 1

print(j)
