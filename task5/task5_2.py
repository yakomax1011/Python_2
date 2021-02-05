from collections import defaultdict
from collections import deque


# Перевод
def dec(str):
    dec = 0
    num = deque(str)
    num.reverse()
    for i in range(len(num)):
        dec += tab[num[i]] * 16 ** i
    return dec


# Подсчет
def hex(num):
    num_i = deque()
    while num > 0:
        d = num % 16
        for i in tab:
            if tab[i] == d:
                num_i.append(i)
        num //= 16
    num_i.reverse()
    return list(num_i)


# Сравнение + Поиск
array_HEX = '0123456789ABCDEF'
tab = defaultdict(int)
counter = 0
for key in array_HEX:
    tab[key] += counter
    counter += 1


# Запрос + Перевод
operand_1 = dec(input('Первое шестнадцатеричное число: ').upper())
operand_2 = dec(input('Второе шестнадцатеричное число:').upper())


# Вызов + Подсчет
print(f'Сумма: {hex(operand_1 + operand_2)}')
print(f'Произведение: {hex(operand_1 * operand_2)}')
