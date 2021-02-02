# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
from math import sqrt

def sieve(n):
    indx = n
    n *= 10
    sieve = list(range(n * 2))
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1[indx]

print(timeit.timeit('sieve(1000)', number=100, globals=globals()))   # 1.0617372
print(timeit.timeit('sieve(4000)', number=100, globals=globals()))   # 5.2268697
print(timeit.timeit('sieve(7000)', number=100, globals=globals()))   # 9.7312528
print('_' * 50)


def prime(n):
    #n = 3_000
    lst=[]
    for i in range(2, n * 12):
        if (i > 10):
            if (i % 2 == 0) or (i% 10 == 5):
                continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[n - 1]


print(timeit.timeit('prime(1000)', number=100, globals=globals()))   # 4.212472300000002
print(timeit.timeit('prime(4000)', number=100, globals=globals()))   # 25.1746382
print(timeit.timeit('prime(7000)', number=100, globals=globals()))   # 53.4429991

