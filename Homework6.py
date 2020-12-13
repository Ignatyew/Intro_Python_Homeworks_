# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.
#############################################################################

my_list = ['asd', 'qwe', 'zxc', 'rty']
new_list = []
for index, value in enumerate(my_list):
    if not index % 2:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)

#############################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
#############################################################################

my_list = ['asf', 'hfo', 'das', 'gas', 'ade']
first_a_list = [num for num in my_list if num[0] == 'a']
print(first_a_list)

#############################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#############################################################################

my_list = ['asf', 'hfo', 'das', 'gas', 'ade']
a_list = [num for num in my_list if "a" in num]
print(a_list)

#############################################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
#############################################################################

my_list = ['asf', 123, 'hfo', 456, 'das', 789, 'gas', 'ade']
new_list = [num for num in my_list if not isinstance(num, int)]
print(new_list)

#############################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
#############################################################################

my_str = "qqwwe122rtt344yy"
new_list = [num for num in my_str if my_str.count(num) == 1]
print(new_list)

#############################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#############################################################################

my_str1 = "qwerty1234569"
my_str2 = "qweasd1237888889"
if len(my_str1) >= len(my_str2):
    new_list = [num for num in my_str1 if num in my_str2]
else:
    new_list = [num for num in my_str2 if num in my_str1]
print(new_list)

#############################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#############################################################################

my_str1 = "qwerty1234569vbn"
my_str2 = "qqweasd123789vb"
if len(my_str1) >= len(my_str2):
    new_list = [num for num in my_str1 if my_str2.count(num) == 1 and my_str1.count(num) == 1]
else:
    new_list = [num for num in my_str2 if my_str2.count(num) == 1 and my_str1.count(num) == 1]
print(new_list)


#############################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
#############################################################################

addres = {"Страна": "Украина",
          "Город": "Днепр",
          "Улица": "Иванковская"}
job = {"Ниличие": "+",
       "Должность": "Экономист"}
customer = {"Фамилия": "Иванов",
            "Имя": "Иван",
            "Возраст": "30",
            "Проживание": addres,
            "Работа": job}
print(customer)

#############################################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         # Масло
#############################################################################

cakes = {"Мука": "300 гр.",
         "Молоко": "150 мл.",
         "Масло": "200 гр.",
         "Яйцо": "4 шт."}
cream = {"Сахар": "200 гр.",
         "Масло": "200 гр.",
         "Ваниль": "1 гр.",
         "Сметана": "300 гр."}
glaze = {"Какао": "20 гр.",
         "Сахар": "100 гр.",
         "Масло": "30 гр."}
ingredients = {"Коржи": cakes,
               "Крем": cream,
               "Глазурь": glaze}
print(ingredients)
print(cream)

#############################################################################