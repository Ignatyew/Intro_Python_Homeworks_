import random
import string
import json
import csv
# Цель задания - создать функции, которые будут генерировать случайные данные
# нужного формата для записи в файлы разных типов.
#
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более
# 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита,
# цифры, пробелы, знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять
# отдельно.
# Знаки препинания всегда идут в конце слова.
###############################################################################

def number():
    return str(random.randint(1, 10000))
# print(number())

def transition():
    return "\n"
# print(transition())

def letter():
    return random.choice(string.ascii_lowercase)
# print(letter())

def word():
    return "".join(letter() for i in range(random.randint(3, 9)))
# print(word())

def signs():
    return "".join(letter() for i in range(random.randint(3, 9))) + "".join(chr(random.randint(44, 46)))
# print(signs())

def bword():
    return random.choice(string.ascii_uppercase) + "".join(letter() for i in range(random.randint(3, 9)))
# print(bword())

def funcs():
    fun = [number(), signs(), transition(), word(), bword()]
    return random.choice(fun)+" "
# print(funcs())

def randomtxt():
    random_string = ''
    for i in range(random.randint(100, 1000)):
        if len(random_string) <= random.randint(100, 1000):
            random_string += funcs()
    return random_string
# print(randomtxt())

##############################################################################
# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не
# более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского
# алфавита (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в
# диапазоне от 0 до 1, или True/False. Выбор значения должен быть равновероятным.
# Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
###############################################################################
def letter2():
    return random.choice(string.ascii_lowercase)
# print(letter2())

def word2():
    return "".join(letter2() for i in range(5))
# print(word2())

def number_int():
    return str(random.randint(-100, 100))
# print(number_int())

def number_float():
    return str(random.random())
# print(number_float())

def number_T_F():
    return str(random.choice([True, False]))
# print(number_T_F())

def value2():
    return random.choice([number_int(), number_float(), number_T_F()])
# print(value2())
def dictionary_json():
    return {word2(): value2() for a in range(random.randint(5, 20))}
# print(dictionary_json())
################################################################################
# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с
# n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.
##########################################################################

def number_int():
    return random.randint(3, 10)
# print(number_int())

def number_1_0():
    return str(random.choice([1, 0]))
# print(number_1_0())

def list_csv():
    return [[number_1_0() for i in range(number_int())] for j in range(number_int())]
# print(list_csv())

# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - полный
# путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи
# и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file
# format"

print("Введите полный путь к файлу :  ")
way = input()

def w_txt(way):
    with open(way, "w") as txt_file:
        txt_file.write("".join(randomtxt()))

def w_cvs(way):
    with open(way, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerows(list_csv())

def w_json(way):
    with open(way, "w") as json_file:
        json.dump(dictionary_json(), json_file)


def generate_and_write_file(way):
    ext = way.split('.')[-1]
    if ext == "txt":
        result = w_txt(way)
    elif ext == "json":
        result = w_json(way)
    elif ext == "csv":
        result = w_cvs(way)
    else:
        print("Unsupported file format")
        result = ''
    return result

generate_and_write_file(way)