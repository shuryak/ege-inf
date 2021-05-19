N = int(input())

t = int(input())

tA = 0 # Кратчайшее время до A_N
tB = t # Кратчайшее время до B_N

for i in range(N):
    a, b = [int(x) for x in input().split()]
    tA = tA + a
    tB = min(tA + t, tB + b)

print(tB)
