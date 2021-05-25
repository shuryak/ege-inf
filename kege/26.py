# https://inf-ege.sdamgia.ru/problem?id=35484

import time

start_time = time.time()

def bin_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

file = open('26.txt', 'r')

x = []

is_n = False
for line in file:
    if is_n == False:
        N = int(line)
        is_n = True
        continue
    x.append(int(line))

file.close()

x.sort()

max_average = 0
pairs_count = 0

for i in range(0, N):
    if x[i] % 2 == 0:
        for t in range(i + 1, N):
            if x[t] != x[i] and x[t] % 2 == 0:
                average = (x[t] + x[i]) // 2
                # Поиск среднего арифметичского в наборе
                # for p in range (0, N):
                #     if x[p] == average:
                #         pairs_count += 1
                #         max_average = max(max_average, average)
                if(bin_search(x, average) != None):
                    pairs_count += 1
                    max_average = max(max_average, average)

print('Кол-во подходящих пар:', pairs_count)
print('Наибольшее среднее арифметическое:', max_average)

print("\nВремя выполнения программы: %.3f секунд" % (time.time() - start_time))
