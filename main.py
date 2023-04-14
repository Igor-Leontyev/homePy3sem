# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. В последующих  строках записаны N
# целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


import random


def Task_1():
    list_cur = list()
    count = 0
    n = int(input('введите количество элементов в массиве N:\n '))

    for i in range(n):
        list_cur.append(random.randint(1, n))
    print(f"\t{list_cur}")

    x = int(input('введите число X:\n\t'))

    for i in range(n):
        if list_cur[i] == x:
            count += 1
    print(f"\t-> {count}")


def Task_2():
    list_cur = list()
    n = int(input('введите количество элементов в массиве N:\n '))

    for i in range(n):
        list_cur.append(random.randint(1, n))
    print(f"\t{list_cur}")

    x = int(input('введите число X:\n\t'))

    min = 100
    for i in range(n):
        min_cur = abs(x - list_cur[i])
        max_cur = abs(list_cur[i] - x)

        if max_cur <= min:
            min = max_cur
            count = list_cur[i]
        elif min_cur <= min:
            min = min_cur
            count = list_cur[i]

    print(f"\t-> {count}")

# Task_2()


def Task_3():
    dict_ch = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
               'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
               'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3,
               'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4,
               'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

    word = input('ВВЕДИТЕ СЛОВО: ')
    word = word.upper()
    count = 0

    for i in range(len(word)):
        if word[i] in dict_ch:
            count += dict_ch.get(word[i])
        else:
            print('введены неверные символы')
            break


    print(f'\n\n\n{word}\n{count}')


Task_3()