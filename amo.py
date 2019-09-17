import csv
import string
from multiprocessing import Pool
from datetime import datetime

#name = input("Введите имя файла ")
name = 'amocrm_contacts (total).csv'

source = csv.reader(open(name, encoding="utf8"), delimiter=';', quotechar='"')


def latin_whole(line, dest): #без кириллицы в имени

    for letter in line[1]:
        if letter not in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя':  # проверка НЕкириллицы в имени[1]
            if "@" in line[20]:  # проверка на предмет присутствия символа в графе почты[20]
                if "," in line[20]:
                    templine = line[20].split(",")
                    dest.write(f"{line[1]},{templine[0]},{line[58]},{line[2]}\n")  # когда 2 почты
                    dest.write(f"{line[1]},{templine[1].strip()},{line[58]},{line[2]}\n")
                else:
                    dest.write(f"{line[1]},{line[20]},{line[58]},{line[2]}\n")
                break

def latin_gender(line, dest): #латиница в имени, с обращением

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

def latin_single(line, dest): #латиница в имени, с 1 словом в имени и обращением

    for letter in string.ascii_letters:
        if letter in line[1] and 'в' not in line[58] and 'Р' not in line[59]:  # отсутствие кириллицы в обращении и язык не Р...
            if "@" in line[20] and bool(line[58]) != False:  # проверка присутствия почты[20] и обращения[58]

                if "," in line[20]:
                    templine = line[20].split(",")
                    dest.write(f"{line[1].split()[0]},{templine[0]},{line[58]},{line[2]}\n")  # когда 2 почты
                    dest.write(f"{line[1].split()[0]},{templine[1].strip()},{line[58]},{line[2]}\n")
                else:
                    dest.write(f"{line[1].split()[0]},{line[20]},{line[58]},{line[2]}\n")
                break

def cyrilic(line, dest): #кирилица в имени

    for letter in line[1]:
        if letter in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя':  # проверка кириллицы в имени[1]
            if "@" in line[20]:  # проверка на предмет присутствия символа в графе почты[20]
                if "," in line[20]:
                    templine = line[20].split(",")
                    dest.write(f"{line[1]},{templine[0]},{line[2]},{line[58]}\n")  # когда 2 почты
                    dest.write(f"{line[1]},{templine[1].strip()},{line[2]},{line[58]}\n")
                else:
                    dest.write(f"{line[1]},{line[20]},{line[2]},{line[58]}\n")
                break

def cyrilic_double(line, dest): #кирилица в имени, 2 слова в имени, есть компания

    for letter in line[1]:
        if letter in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя':  # проверка кириллицы в имени[1]
            if "@" in line[20]:  # проверка на предмет присутствия символа в графе почты[20]
                if line[1].count(" ")  == 1 and line[2]:
                    if "," in line[20]:
                        templine = line[20].split(",")
                        dest.write(f"{line[1]},{templine[0]},{line[2]}\n")  # когда 2 почты
                        dest.write(f"{line[1]},{templine[1].strip()},{line[2]}\n")
                    else:
                        dest.write(f"{line[1]},{line[20]},{line[2]}\n")
                    break

i = 0
timer = datetime.now()

for line in source:
    try:
        print(f"{i:<5}'st line is: {line[58]:>10}{line[1]:>40}{line[20]:>60}{line[2]:>70}")
        #
        # with open("latin_gender.csv", "a", encoding="utf8") as dest:
        #     latin_gender(line, dest) # вынимает имена, где встречаются латинские символы и обращение
        #
        # with open("latin_single.csv", "a", encoding="utf8") as dest:
        #     latin_single(line, dest) # вынимает имена, где в графе имя только одно латинское слово
        #
        with open("cyrilic.csv", "a", encoding="utf8") as dest:
            cyrilic(line, dest) # вынимает имена, где встречаются кириллические символы
        #
        # with open("cyrilic_double.csv", "a", encoding="utf8") as dest:
        #     cyrilic_double(line, dest) # вынимает имена, где встречаются кириллические символы
        #
        # with open("latin_whole.csv", "a", encoding="utf8") as dest:
        #     latin_whole(line, dest)  # вынимает имена, где встречаются кириллические символы
    except:
        print("EOL reached")

    i += 1

end = datetime.now()
total = end - timer
print(f'time used: {str(total)[:7]}')