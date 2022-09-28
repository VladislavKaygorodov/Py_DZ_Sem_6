# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

def crt_mngchln(step):
    number = step
    size = number + 1
    numbers = [random.randint(0,101) for i in range(0,size)]
    step = [i for i in range(0, number+1)]
    list = [(str(numbers[i])+"*x**"+str(step[i])) for i in range(size)]

    temp_str = ""
    i=len(list)-1

    while i >= 0:
        temp_str += list[i]+"+"
        i-=1

    left_str = temp_str[:-1]

    return left_str

first = crt_mngchln(2)
second = crt_mngchln(2)

data_left = open("txt_for_zad5_first.txt", "w")
data_left.writelines(first)
data_left.close()

data_right = open("txt_for_zad5_second.txt", "w")
data_right.writelines(second)
data_right.close()

temp_one = ""
temp_two = ""

path_left = "txt_for_zad5_first.txt"
path_right = "txt_for_zad5_second.txt"

data_read_left = open(path_left, "r")
for line in data_read_left:
    temp_one = line
data_read_left.close()

data_read_right = open(path_right, "r")
for line in data_read_right:
    temp_two = line
data_read_right.close()

result = "(" + temp_one + ")+(" + temp_two + ")"

data_result = open("txt_for_zad5_result.txt", "w")
data_result.writelines(result)
data_result.close()