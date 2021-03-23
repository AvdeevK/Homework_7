# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#    Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
#    медианы, в другой — не больше медианы.


from random import randint


def gnome_sort(data):
    i = 1
    j = i + 1
    while i < len(data):
        if data[i - 1] < data[i]:
            i = j
            j += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1


m = 10

arr = [randint(0, 100) for i in range(2 * m + 1)]
print(arr)
gnome_sort(arr)
print(arr)

mediana = arr[len(arr) // 2]

print(f'Медиана для данной последовательности равна {mediana}')
