# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

num_max = 0
for i in range(1, len(array)):
    if array[i] > array[num_max]:
        num_max = i

num_min = 0
for i in range(1, len(array)):
    if array[i] < array[num_min]:
        num_min = i

#print(num_min)
#print(num_max)
#print(array[(num_max + 1):num_min])

if num_min > num_max:
    sum_elem = 0
    for i in array[(num_max + 1):num_min]:
        sum_elem += i
        #print(f'1 {sum_elem}')
else:
    sum_elem = 0
    for i in array[(num_min + 1):num_max]:
        sum_elem += i
        #print(f'2 {sum_elem}')

print(f'Cумма элементов, находящаяся между минимальным и максимальным элементами = {sum_elem}')
