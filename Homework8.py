import random
import string
# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список (названия сохранить без точки).
################################################################################

with open("domains.txt", "r") as txt_file:
    domains_line = []
    for line in txt_file.readlines():
        domains_line.append(line.strip(".\n"))
# print(domains_line)

################################################################################
# 2. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята
# с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.
################################################################################

with open("names.txt", "r") as txt_file:
    names_ = []
    for line in txt_file.readlines():
        names_.append(line.strip(" "))
names_line = [num.split()[1] for num in names_]
# print(names_line)


################################################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию
# в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы
# не смогут повторяться)
#
# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com
def number():
    return str(random.randint(100, 999))

# print(number())

def letter():
    return random.choice(string.ascii_lowercase)

# print(letter())

def word():
    return "".join(letter() for i in range(random.randint(5, 7)))

# print(word())

def create_email(domains, names):
    return names+"."+number()+"@"+word()+"."+domains

domains = domains_line[7]
names = names_line[20]

e_mail = create_email(domains, names)

print(e_mail)