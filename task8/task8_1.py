#  Определение количества различных подстрок с использованием хеш-функции.
#  Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
#  Примечание: в сумму не включаем пустую строку и строку целиком.


import hashlib

str = input('Здравствцуйте, ведите строку для подсчета: ')
str_lower = str.lower()

sum_str = set()

for i in range(len(str_lower)):
    for j in range(len(str_lower), i, -1):
        hash_str = hashlib.sha1(str_lower[i:j].encode('utf-8')).hexdigest()
        sum_str.add(hash_str)

print(f'Количество различных подстрок = {len(sum_str) -1}, в строке: {str}')