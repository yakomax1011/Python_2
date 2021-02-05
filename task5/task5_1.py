from collections import namedtuple
from statistics import mean

companies = namedtuple('Сompanies', 'name profit_list avg')

quarter = []
for i in range(int(input('Идеальный пользователь, пожалуйста, введите количество компаний: '))):
    sets = input('Идеальный пользователь, пожалуйста, введите имя и поквартальную прибыль через пробел: ').split()
    quarter.append(companies(sets[0], sets[1:], mean(map(int, sets[1:3]))))

avg = mean([i.avg for i in quarter])

for i in quarter:
    print(f'Компания: {i.name} - средняя прибыль за год: {i.avg}')


print('Сompanies с прибылью меньше средней: ')
for i in quarter:
    if i.avg < avg:
        print(i.name)

print('Сompanies с прибылью больше средней: ')
for i in quarter:
    if i.avg > avg:
        print(i.name)