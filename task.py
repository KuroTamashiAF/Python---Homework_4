# Для тех, кто только сейчас видит этот файл, вместо 1 задачи:Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7] Порядок элементов менять нельзя

# не понял в чем прикол задачи [1, 5, 2, 3, 4, 6, 1, 7]=> [1, 2, 3, 4, 6, 7], удалилась 5 и отсортирован список, и даже ес ли б
# мы удаляли дубликаты 5 ка бы осталась, не вижу связи или закона по которому получались бы такие числа,
# может более опытные, со курсники и разобрались, но разбора этого задания в записи нету, мы благополучно на него забили!!!!
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7] тоже не понятно, почему 5 и 1 слетели!!! На мой взгляд в условии ДЗ чего-то не хвататет.


# 2.	Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.
'''
from random import randint

def make_file_with_nuumbers(count):
    with open('file_with_numbers.txt', 'w') as data:
        for i in range(count):
            if i > 0 and i % 10 == 0:
                data.write('\n')
            data.write(str(f'{randint(0,100)} '))


def get_list():
    # воспользовался вашим советом так действителбно проще
    with open('file_with_numbers.txt', 'r') as data:
        new_list = list(map(int, data.read().split()))
    return new_list


def sort(list_of_numbers):
    list_of_numbers.sort()

def Rewrite_sort_list_in_file(list_of_numbers):
    with open('sortingfile.txt', 'w') as data:
        data.write(str(list_of_numbers))

count = int(input("Enter the count quantity of numbers: "))
make_file_with_nuumbers(count)
list_of_numbers = get_list()
print(list_of_numbers)
# print(type(list_of_numbers))
sort(list_of_numbers)
print(list_of_numbers)
Rewrite_sort_list_in_file(list_of_numbers)
'''


# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).
'''
def make_list():
    with open('1Kints.txt', 'r') as data:
        list_nummbers = list(map(int, data.read().split()))
    return list_nummbers


def find_triplets(list_nummbers, n):
  

    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (list_nummbers[i]+list_nummbers[j]+list_nummbers[k] == 0):
                    print(
                        f'{list_nummbers[i]} {list_nummbers[j]} {list_nummbers[k]} = 0')
              


list_nummbers = make_list()
n = len(list_nummbers)
print(find_triplets(list_nummbers, n))
# print(list_nummbers)
# # print(type(list_nummbers))
# # print(type(list_nummbers[100]))
'''