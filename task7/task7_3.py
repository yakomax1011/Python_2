#  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#  в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#  Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
#  используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random
import copy


def median_search(array):
    centr = (len(arr) / 2) + 0.5
    for i in array:
        count = 1
        for j in range(len(array)):
            if i < array[j]:
                count += 1
        if count == centr:
            mad_median = i
    return mad_median


m = int(input('Ввод m: '))

SIZE = (2 * m) + 1
MIN_ITEM = 1
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)


print(median_search(arr))


#  Читерский способ:

arr2 = copy.deepcopy(arr)

while len(arr2) > 2:
    arr2.remove(max(arr2))
    arr2.remove(min(arr2))

print(arr2[0])
