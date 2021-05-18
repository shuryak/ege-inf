N = int(input())

scope = 12
counters = [0] * (scope + 1) # Список длины 13 (по факту - 12, c[0] не учитываем)

for i in range(N):
    x = int(input())
    counters[x] += 1

tasknums = list(range(scope + 1))

# Синхронно сортируем частоты задач и их номера

for bypass in range(scope + 1):
    for i in range(0, scope): # scope + 1 - 1
        if counters[i] > counters[i+1]:
            counters[i], counters[i+1] = counters[i+1], counters[i]
            tasknums[i], tasknums[i+1] = tasknums[i+1], tasknums[i]

# Теперь все счётчики идут по возрастанию. Нулевые - в начале

for i in range(0, scope + 1):
    if counters[i] == 0: continue
    print(tasknums[i], counters[i])
