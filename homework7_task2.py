# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
#    на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


from random import uniform, shuffle


def merge_sort(data):
    if len(data) <= 1:
        return data

    i = 0
    j = 0
    middle = int((len(data)) / 2)

    left_half = merge_sort(data[:middle])
    right_half = merge_sort(data[middle:])

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            data[i+j] = left_half[i]
            i += 1
        else:
            data[i+j] = right_half[j]
            j += 1

    while i < len(left_half):
        data[i+j] = left_half[i]
        i += 1
    while j < len(right_half):
        data[i + j] = left_half[i]
        j += 1

    return data


a = [uniform(0,50) for i in range(10)]
shuffle(a)
merge_sort(a)

print(a)