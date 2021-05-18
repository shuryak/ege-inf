N = int(input())

# smin_even = 60001 # Наихудший случай - все числа = 30 000
# smin_odd = 60001
smin = [60001, 60001]
# m_even = 60001
# m_odd = 60001
m = [60001, 60001]

for i in range(N):
    x = int(input())

    # if x % 2 == 0: # x - чётный
    #     # Сумма x (чёт) + m_even (чёт) будет чётной
    #     smin_even = min(smin_even, x + m_even)
    #     # Сумма x (чёт) + m_odd (нечёт) будет нечётной
    #     smin_odd = min(smin_odd, x + m_odd)

    #     m_even = min(m_even, x)
    # else: # x - нечётный
    #     # Сумма x (нечёт) + m_odd (нечёт) будет чётной
    #     smin_even = min(smin_even, x + m_odd)
    #     # Сумма x (нечёт) + m_even (чёт) будет нечётной
    #     smin_odd = min(smin_odd, x + m_even)

    #     m_odd = min(m_odd, x)

    k = x % 2 # Критерий чётности

    smin[k] = min(smin[k], x + m[0])
    smin[1-k] = min(smin[1-k], x + m[1])
    m[k] = min(m[k], x)

# if smin_even == 60001: # Чётная пара отсутствует
#     print(smin_odd)
# else:
#     print(smin_even)

if smin[0] == 60001: # Чётная пара отсутствует
    print(smin[1])
else:
    print(smin[0])
