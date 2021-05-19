N = int(input())

infinity = 1000*1000 + 1

m = 1001
m2 = infinity
mp = infinity

Q = [int(input()) for i in range(0, 6)]

for i in range(0, N-6):
    x = int(input())

    y = Q[i % 6]
    Q[i % 6] = x

    m = min(m, y) # Минимум среди всех, прошедших очередь
    if y % 2 == 0:
        m2 = min(m2, y) # Минимум среди чётных, прошедших очередь

    if x % 2 == 0:
        mp = min(mp, x * m)
    else:
        mp = min(mp, x * m2)

if mp == infinity:
    print(-1)
else:
    print(mp)
