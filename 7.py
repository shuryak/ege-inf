n = int(input())
a = [int(input()) for i in range(n)]

c = 0
for i in range(0, n):
    # for k in range(0, i): # for k in range(i+1, n):
    #     if i - k >= 4 and ...
    for k in range(0, i - 3): # for k in range(i+1, n):
        if a[i] * a[k] % 29 == 0:
            c += 1

print(c)
