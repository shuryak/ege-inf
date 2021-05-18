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
a = [randint(160, 200) for i in range(0, n)]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

x = 201
for i in range(0, n):
    if a[i] >= 180 and a[i] < x:
        x = a[i]
print(x)
