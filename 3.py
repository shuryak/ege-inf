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

m = a[0]
m2 = a[1]

if m2 > m:
    m, m2 = m2, m

for i in range(2, n):
    if a[i] > m2:
        m2 = a[i]
        if m2 > m:
            m, m2 = m2, m

print(m2)
