# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 1500
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

# def min2_array(array):
#     num_min = -1
#     new_array = []
#     array_2 = array[::]
#     while True:
#         num_min += 1
#         for i, item in enumerate(array_2):
#             #print(i, item, num_min)
#             if num_min == item:
#                 num_min = i
#                 new_array.append(array_2[i])
#                 del array_2[i]
#                 if len(new_array) - 1 == 1:
#                     return new_array
#                 else:
#                     continue
# num_min_2 = min2_array(array_1)
# print(num_min_2)
# Опыт оказался неудачным...

if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

size = len(array) - 1
for i in range(2, size):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i

print(f'Два наименьших элемента в массиве: {array[min1]}, {array[min2]}')
