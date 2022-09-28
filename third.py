# Реализуйте алгоритм перемешивания списка.

import random

k = int(input("Введите число: "))
list = [random.randint(0,k) for i in range(0,k)]
print(list)
random.shuffle(list)
print(list)