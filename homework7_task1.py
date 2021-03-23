# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
#    на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#    Примечания:
#       ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#       ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#    Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import shuffle, randint


def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return

arr = [randint(-100, 100) for i in range(10)]
shuffle(arr)
print(arr)

bubble_sort(arr)
print(arr)