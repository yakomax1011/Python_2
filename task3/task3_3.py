# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array_1)

# Пробую через while True и функцию

def min_array(array):
    num_min = -1
    while True:
        num_min += 1
        for i, item in enumerate(array):
            #print(i, item, num_min)
            if num_min == item:
                num_min = i
                #print(f'Индекс минимальный = {num_min}')
                return num_min

num_min = min_array(array_1)

# Можно и так, но мы не ищем легких путей.
# num_min = 0
# for i in range(1, len(array)):
#     if array[i] > array[num_min]:
#         num_min = i


# Пробую через цикл for

num_max = 0
for i in range(1, len(array_1)):
    if array_1[i] > array_1[num_max]:
        num_max = i

# Спасибо добрым людям, не нужно брать третью сковородку. Подкидываем и меняем блины на лету.

array_1[num_max], array_1[num_min] = array_1[num_min], array_1[num_max]

print(array_1)
