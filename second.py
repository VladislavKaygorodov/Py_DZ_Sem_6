
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
size = 7
# size = int(input("Введите размер списка: "))
list = [random.randint(0,size) for i in range(0,size)]
print(list)

list_2 = []
i=0
k=1
while i < (len(list)/2):
    list_2.append(list[i] * list[k * -1])
    i+=1
    k+=1

print(list_2)