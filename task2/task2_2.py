# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import math

num_user = int(input('Пожалуйста, введите целое число: '))
num_odd = 0
num_even = 0

def сounting_odd_or_even(num_user):
  global num_odd, num_even
  last_digit = num_user % 10
  if last_digit % 2 == 0:
    num_even += 1
  else:
    num_odd += 1

сounting_odd_or_even(num_user)

while num_user >= 10:
  num_user = math.floor(num_user / 10)
  сounting_odd_or_even(num_user)

print(f'Количество нечетных цифр: {num_odd}')
print(f'Количество четных цифр: {num_even}')
