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

k = 0

for j in range(n):
    if a[j] > 100 and a[j] % 4 != 0:
        k += 1
        a[j] = -1
for j in range(n):
    if a[j] == -1:
        a[j] = k
    print(a[j])
