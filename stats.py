# Однопроходные статистики

N = int(input())

# Инициализация:
n = 0 # Для количества
s = 0 # Для суммы
p = 1 # Для произведения
is_any_negative = False # Для поиска (any)
is_all_even = True # Для инспекции (all)

for i in range(N):
    x = int(input())
    # Обработка:
    n += 1
    s += x
    p *= x
    is_any_negative |= (x < 0)
    # if x < 0:
    #     is_any_negative = True
    is_all_even &= (x % 2 == 0)
    # if not (x % 2 == 0):
    #     is_all_even = False

print(n, s, p)
print(is_any_negative)
print(is_all_even)

# Последовательность с терминальным элементом:

# Инициализация:
n = 0 # Для количества
s = 0 # Для суммы
p = 1 # Для произведения

x = int(input()) # !
while x != 0:
    # Обработка
    n += 1
    s += x
    p *= x

    # Считывание x для следующей итерации:
    x = int(input())

print(n, s, p)


# Экстремумы:

is_vacant = True # Флаг вакантности места для потенциального максимума

for i in range(N):
    x = int(input())
    # Обработка
    if is_vacant or x > m: # is_vacant вычисляется быстрее (or - ленивый оператор)
        m = x
        is_vacant = False

if is_vacant:
    print('Последовательность пуста')
else:
    print(m)

# Поиск с подсчётом равных экстремуму:

# Инициализация:

mn = 0 # Количество равных максимуму

for i in range(N):
    x = int(input())
    # Обработка
    if mn == 0 or x > m:
        m = x
        mn = 1
    elif x == m:
        mn += 1

if mn == 0:
    print('Последовательность пуста')
else:
    print(m, mn)

# Поиск местоположения экстремума:

mindex = -1 # Индекс максимума в последовательности

for i in range(N):
    x = int(input())
    # Обработка
    if mindex == -1 or x > m:
        m = x
        mindex = i
    elif x == m:
        mn += 1

if mindex == -1:
    print('Последовательность пуста')
else:
    print(m, mindex)

# Поиск n максимумов за один проход

# Инициализация (желательно реализовать без инициализации):

m1 = -10000000
m2 = -10000000
m3 = -10000000

for i in range(N):
    x = int(input())
    # Обработка
    if x > m3:
        m3 = x
    if m3 > m2:
        m2, m3 = m3, m2
    if m2 > m1:
        m1, m2 = m2, m1

print(m1, m2, m3)
