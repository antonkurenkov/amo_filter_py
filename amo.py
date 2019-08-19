import csv
import string

#name = input("Введите имя файла ")
name = 'amocrm_contacts (total).csv'

source = csv.reader(open(name, encoding="utf8"), delimiter=';', quotechar='"')


def latin(line, dest):

    for letter in string.ascii_letters:
        if letter in line[1] and 'в' not in line[58] and 'Р' not in line[59]:  # отсутствие кириллицы в обращении и язык не Р...
            if "@" in line[20] and bool(line[58]) != False:  # проверка присутствия почты[20] и обращения[58]
                if "," in line[20]:
                    templine = line[20].split(",")
                    dest.write(f"{line[1]},{templine[0]},{line[58]},{line[2]}\n")  # когда 2 почты
                    dest.write(f"{line[1]},{templine[1].strip()},{line[58]},{line[2]}\n")
                else:
                    dest.write(f"{line[1]},{line[20]},{line[58]},{line[2]}\n")
                break


def cyrilic(line, dest):

    for letter in line[1]:
        if letter in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя':  # проверка кириллицы в имени[1]
            if "@" in line[20]:  # проверка на предмет присутствия символа в графе почты[20]
                dest.write(f"{line[1]},{line[20]},{line[2]}\n")
                break


i = 0

for line in source:
    try:
        print(f"{i:<5}'st line is: {line[58]:>10}{line[1]:>40}{line[20]:>60}{line[2]:>70}")
    except:
        print("EOL reached")

    dest = open("latin.csv", "a", encoding="utf8")
    latin(line, dest) # вынимает имена, где встречаются латинские символы

    dest = open("cyrilic.csv", "a", encoding="utf8")
    cyrilic(line, dest) # вынимает имена, где встречаются кириллические символы

    i += 1

print("done!")