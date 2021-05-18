n = int(input())
a = [int(input()) for i in range(n)]

m1 = 0
m2 = 0

for i in range(0, n):
    for k in range(0, i): # for k in range(i+1, n):
        if (a[i] - a[k]) % 2 == 0 and (a[i] % 17 == 0 or a[k] % 17 == 0):
            if a[i] + a[k] > m1 + m2:
                m1 = a[i]
                m2 = a[k]

print(m1, m2)
