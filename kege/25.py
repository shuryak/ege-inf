# https://inf-ege.sdamgia.ru/problem?id=35483

def find(number):
    if number % 2 != 0: # Если число number не делится на 2
        a = [1, number] # Значит 2 нечётных делителя: 1 и само число number
    else: a = [1] # Иначе 1 нечётный делитель: число 1

    d = 2
    while d * d <= number:
        if number % d == 0: # Проверяем делимость
            if d % 2 != 0: # Нечётный делитель
                a.append(d) # Добавляем нечётный делитель
            if number // d != d and (number // d) % 2 != 0: # Исключаем квадрат и проверяем на нечётность парный делитель
                a.append(number // d) # Добавляем нечетный парный делитель
        d += 1
    
    return a

result = []

for n in range(35000000, 2 * 40000000 + 1): 
    if int(n ** 0.5)**2 == n: # Действия ниже выполянем только для квадратов
        if len(find(n)) > 5:
            continue
        if n < 40000000 and len(find(n)) == 5:
            result.append(n)
        if n // 2 > 35000000 and n // 2 < 40000000 and len(find(n // 2)) == 5:
            result.append(n // 2)

print(sorted(result))
