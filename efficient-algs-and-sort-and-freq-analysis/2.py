N = int(input())
s = [0, None, None, None] # Максимальные s[остаток по модулю 4]

for i in range(N):
    numbers = [int(word) for word in input().split()]

    s_new = list(s) # Новые максимальные суммы по каждому остатку
    for x in numbers:
        for k in range(0, 4):
            if s[k] is None: continue
            
            # Если s[k] уже есть, то:
            radix = (k + x) % 4 # radix = (s[k] + x) % 4
            # Если новая сумма больше, то запомнить её
            if s_new[radix] is None or s[k] + x > s_new[radix]:
                s_new[radix] = s[k] + x

    for i in range(4):
        s[i] = s_new[i]

for i in range(4):
    if s[i] is None:
        s[i] = 0

print(max(s[1], s[2], s[3])) # Максимальная сумма, не кратная 4
