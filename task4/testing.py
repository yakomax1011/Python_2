#     Выбрал поиск мин и макс + сумму между этими элементами.
#     Задача №6 из 3-го практического задания:
#     " В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#     Сами минимальный и максимальный элементы в сумму не включать. "


import timeit
import cProfile
import random
from operator import itemgetter



# Решение №1



def min_max_1(n):
    #n = 100
    MIN_ITEM = -90
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    #print(array)

    num_max = 0
    for i in range(1, len(array)):
        if array[i] > array[num_max]:
            num_max = i
    #print(num_max)

    num_min = 0
    for i in range(1, len(array)):
        if array[i] < array[num_min]:
            num_min = i
    #print(num_min)

    if num_min > num_max:
        sum_elem = 0
        for i in array[(num_max + 1):num_min]:
            sum_elem += i
    else:
        sum_elem = 0
        for i in array[(num_min + 1):num_max]:
            sum_elem += i
    #print(f'Cумма элементов, находящаяся между минимальным и максимальным элементами = {sum_elem}')


print(timeit.timeit('min_max_1(100)', number=100, globals=globals()))         # 0.027477
print(timeit.timeit('min_max_1(200)', number=100, globals=globals()))         # 0.0583611
print(timeit.timeit('min_max_1(10000)', number=100, globals=globals()))       # 2.6260815
print(timeit.timeit('min_max_1(20000)', number=100, globals=globals()))       # 5.511435500000001
print(timeit.timeit('min_max_1(30000)', number=100, globals=globals()))       # 8.779261


cProfile.run('min_max_1(100_000)')

#     533873 function calls in 0.506 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#          1    0.002    0.002    0.506    0.506 <string>:1(<module>)
#     100000    0.136    0.000    0.304    0.000 random.py:200(randrange)
#     100000    0.084    0.000    0.388    0.000 random.py:244(randint)
#     100000    0.112    0.000    0.169    0.000 random.py:250(_randbelow_with_getrandbits)
#          1    0.039    0.039    0.504    0.504 testing.py:15(min_max_1)
#          1    0.077    0.077    0.465    0.465 testing.py:19(<listcomp>)
#          1    0.000    0.000    0.506    0.506 {built-in method builtins.exec}
#          2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     100000    0.023    0.000    0.023    0.000 {method 'bit_length' of 'int' objects}
#          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     133866    0.034    0.000    0.034    0.000 {method 'getrandbits' of '_random.Random' objects}



# Решение №2



def min_max_2(n):
    #n = 100
    MIN_ITEM = -90
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    num_max2 = max(enumerate(array), key=itemgetter(1))[0]
    num_min2 = min(enumerate(array), key=itemgetter(1))[0]

    if num_min2 > num_max2:
        sum_elem2 = 0
        for i in array[(num_max2 + 1):num_min2]:
            sum_elem2 += i
    else:
        sum_elem2 = 0
        for i in array[(num_min2 + 1):num_max2]:
            sum_elem2 += i

    #print(f'Cумма элементов, находящаяся между минимальным и максимальным элементами = {sum_elem2}')


print(timeit.timeit('min_max_2(100)', number=100, globals=globals()))        # 0.028871599999999997
print(timeit.timeit('min_max_2(200)', number=100, globals=globals()))        # 0.04953959999999999
print(timeit.timeit('min_max_2(10000)', number=100, globals=globals()))      # 2.7074293999999988
print(timeit.timeit('min_max_2(20000)', number=100, globals=globals()))      # 5.080577000000002
print(timeit.timeit('min_max_2(30000)', number=100, globals=globals()))      # 8.613672200000003

cProfile.run('min_max_2(100_000)')

#   534404 function calls in 0.604 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.002    0.002    0.604    0.604 <string>:1(<module>)
#   100000    0.174    0.000    0.377    0.000 random.py:200(randrange)
#   100000    0.094    0.000    0.471    0.000 random.py:244(randint)
#   100000    0.142    0.000    0.203    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.603    0.603 testing.py:58(min_max_2)
#        1    0.093    0.093    0.564    0.564 testing.py:62(<listcomp>)
#        1    0.000    0.000    0.604    0.604 {built-in method builtins.exec}
#        1    0.019    0.019    0.019    0.019 {built-in method builtins.max}
#        1    0.019    0.019    0.019    0.019 {built-in method builtins.min}
#   100000    0.024    0.000    0.024    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   134397    0.037    0.000    0.037    0.000 {method 'getrandbits' of '_random.Random' objects}



# Решение №3 - Какая-то "Dich"



test = """
n = 30000
MIN_ITEM = -90
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
length_array = len(array)
spam = length_array * -1
index_array = spam
numb_numb = spam
#print(spam, type(spam))
count_array = sum(array)
rever_array = count_array * -1
# Ищем минимум
rever_array_2 = rever_array
while rever_array_2 < count_array:
    if rever_array_2 in array:
        minimum = rever_array_2
        minimum = array.index(minimum)
        break
    else:
        rever_array_2 += 1
#print(minimum)
# Ищем максимум
count_array_2 = count_array
while True:
    if count_array_2 in array:
        maximum = count_array_2
        maximum = array.index(maximum)
        break
    else:
        count_array_2 -= 1
#print(maximum)

if minimum > maximum:
    sum_elem3 = 0
    for i in array[(maximum + 1):minimum]:
        sum_elem3 += i
else:
    sum_elem3 = 0
    for i in array[(minimum + 1):maximum]:
        sum_elem3 += i

print(f'Cумма элементов, находящаяся между минимальным и максимальным элементами = {sum_elem3}')

"""

print(timeit.timeit('test', number=100, globals=globals()))   # n = 10000 : 1.2499999999970868e-05
print(timeit.timeit('test', number=100, globals=globals()))   # n = 20000 : 5.699999999997374e-06
print(timeit.timeit('test', number=100, globals=globals()))   # n = 30000 : 5.999999997893701e-06

cProfile.run(test)  # n = 10000

#   53405 function calls in 30.899 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1   30.841   30.841   30.899   30.899 <string>:2(<module>)
#        1    0.010    0.010    0.057    0.057 <string>:5(<listcomp>)
#    10000    0.018    0.000    0.038    0.000 random.py:200(randrange)
#    10000    0.009    0.000    0.048    0.000 random.py:244(randint)
#    10000    0.015    0.000    0.021    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000   30.899   30.899 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#    10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    13396    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
#        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}



V_bl_V_O_D_bl = """

● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли)
-  Задача №6 из 3-го практического задания:
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

● написать 3 варианта кода (один у вас уже есть)
- Выполнено.

● проанализировать 3 варианта и выбрать оптимальный
- 1,2 решения схожи по времени выполнения. На первый взгляд решение №3 выполняется быстрее, но есть условие: только если
изменять длину массива, если для решения №3 вставить целые числа 500 и более, алгоритм отправляется в супер-микс, 
ракета дала старт, но стоит на месте... Если довести до ума монстра из решения №3, его можно использовать для длинных
массивов с малыми элементами, но очень осторожно. Всё же требуются испытания для других реципиентов, как по виду, так и 
по количеству.

● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры)
- результаты представлены после функций.
№1 Решение = O(n)
№2 Решение = O(n)
№3 Решение = O(n2)

● написать общий вывод: какой из трёх вариантов лучше и почему
1,2 варианты лучше. Почему описал выше.
3 вариант это что-то страшное... Боюсь теперь, что заразился написанием такого кода.

"""