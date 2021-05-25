# https://inf-ege.sdamgia.ru/problem?id=35485

file = open('27a.txt', 'r')

x = []
N = 0

is_n = False
for line in file:
    if is_n == False:
        N = int(line)
        is_n = True
        continue
    x.append(int(line))

file.close()

maxSum = 0

m0 = [0, 0, 0]
m1 = [0, 0, 0]
m2 = [0, 0, 0]

for i in range(0, N):
    if x[i] % 3 == 0:
        if x[i] > m0[0]:
            m0[2] = m0[1]
            m0[1] = m0[0]
            m0[0] = x[i]
        elif x[i] > m0[1]:
            m0[2] = m0[1]
            m0[1] = x[i]
        elif x[i] > m0[2]:
            m0[2] = x[i]
    if x[i] % 3 == 1:
        if x[i] > m1[0]:
            m1[2] = m1[1]
            m1[1] = m1[0]
            m1[0] = x[i]
        elif x[i] > m1[1]:
            m1[2] = m1[1]
            m1[1] = x[i]
        elif x[i] > m1[2]:
            m1[2] = x[i]
    if x[i] % 3 == 2:
        if x[i] > m2[0]:
            m2[2] = m2[1]
            m2[1] = m2[0]
            m2[0] = x[i]
        elif x[i] > m2[1]:
            m2[2] = m2[1]
            m2[1] = x[i]
        elif x[i] > m2[2]:
            m2[2] = x[i]

sum0 = sum(m0)
sum1 = sum(m1)
sum2 = sum(m2)
sum12 = m0[0] + m1[0] + m2[0]

print(max(sum0, sum1, sum2, sum12))
