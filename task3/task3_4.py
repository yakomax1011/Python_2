# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100   #Подвисает на более 1000 (доработаю в выходные)
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

size = len(array)
num = array[0]
max_count = 1

for i in range(size - 1):
    count = 1
    for k in range(i + 1, size):
        if array[i] == array[k]:
            count += 1
    if count > max_count:
        max_count = count
        num = array[i]

if max_count > 1:
    print(f'Число {num}, встречается {max_count} раз(а)')
else:
    print('Все элементы уникальны')
