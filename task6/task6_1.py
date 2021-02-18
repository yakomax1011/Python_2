#    Задача для ПЗ №6:
#    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#    Например, если введено число 3486, надо вывести 6843.

# Дынные оборудования и ПО:
# - PC = i3-4030U, 4Gb
# - OS = Windows 10 Home x64
# - PyCh = 64-bit

import sys
import copy
from collections import deque

# Ввод данных от пользователя:

num_str = input("Пожалуйста, введите целое число: ")
num = int(num_str)


# Решение №1
n = 1
num_1 = copy.deepcopy(num)
result_1 = 0
while num_1 > 0:
    add = num_1 % 10
    num_1 = num_1 // 10
    result_1 = result_1 * 10
    result_1 = result_1 + add
print(f'Решение № {n}. Число обратное по порядку: {result_1}')
print(f'Количество памяти затреченное на Решение № {n} = ', sys.getsizeof(num_1) + sys.getsizeof(add) + sys.getsizeof(result_1))
# 42 bytes - для числа: 12345


# Решение №2
n += 1
num_2 = copy.deepcopy(num)
result_2 = 0
base = 10
while num_2 > 0:
    result_2 = result_2 * base + num_2 % base
    num_2 = num_2 // base
print(f'Решение № {n}. Число обратное по порядку: {result_2}')
print(f'Количество памяти затреченное на Решение № {n} = ', sys.getsizeof(num_2) + sys.getsizeof(base) + sys.getsizeof(result_2))
# 42 bytes - для числа: 12345


# Решение №3
n += 1
num_3 = copy.deepcopy(num_str)
result_3 = ''
for i in num_3:
    result_3 = i + result_3
print(f'Решение № {n}. Число обратное по порядку: {result_3}')
print(f'Количество памяти затреченное на Решение № {n} = ', sys.getsizeof(num_3) + sys.getsizeof(i) + sys.getsizeof(result_3))
# 86 bytes - для числа: 12345


# Решение №4
n += 1
num_4 = copy.deepcopy(num_str)
result_4 = num_4[::-1]
print(f'Решение № {n}. Число обратное по порядку: {result_4}')
print(f'Количество памяти затреченное на Решение № {n} = ', sys.getsizeof(num_4) + sys.getsizeof(result_4))
# 60 bytes - для числа: 12345


# Решение №5
n += 1
num_5 = copy.deepcopy(num_str)
num_5 = deque(num_5)
num_5.reverse()
print(f'Решение № {n}. Число обратное по порядку: {num_5}')
print(f'Количество памяти затреченное на Решение № {n} = ', sys.getsizeof(num_5))
# 312 bytes - для числа: 12345


#        Выводы:

#        Если брать срез строго по этим решениям (с малонагруженными данными и ссылками),
#        и не принимать во внимание абсурдность перевода из str,
#        варианты 1 и 2 показывают наименьшее потребление ячеек ОЗУ.
