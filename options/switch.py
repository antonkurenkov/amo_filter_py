import traceback
from datetime import datetime
from options.names import splitter


def who_am_i():
    """
    :return: возвращает имя функции, вызвавшей эту функцию
    """
    stack = traceback.extract_stack()
    filename, codeline, funcName, text = stack[-2]
    return funcName


def box():
    """
    :return: возвращает массив используемых опций
    """
    first = cyr
    second = lat
    # todo дописать сюда другие функции
    return [first, second]  # todo здесь формируется массив опций


def easy1(line):
    export_name = who_am_i() + '.csv'
    lst = []
    lst.append(f"{line[1]},{line[20]},{line[2]}\n")
    with open(str(datetime.now())[:10] + '_' + export_name, "a", encoding="utf8") as exp:
        exp.write('\n'.join(lst))


def cyr(line):
    export_name = who_am_i() + '.csv'
    lst = []
    pick = splitter(line[1])
    for letter in str(pick):
        if letter in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя' and "@" in line[20]:
            if "," in line[20]:
                templine = line[20].split(",")
                lst.append(f"{line[58]},{pick},{templine[0]},{line[2]}")  # когда 2 почты
                lst.append(f"{line[58]},{pick},{templine[1].strip()},{line[2]}\n")
            else:
                lst.append(f"{line[58]},{pick},{line[20]},{line[2]}\n")
            break

    with open(str(datetime.now())[:10] + '_' + export_name, "a", encoding="utf8") as exp:
        exp.write('\n'.join(lst))


def lat(line):
    export_name = who_am_i() + '.csv'
    lst = []
    pick = splitter(line[1])
    for letter in str(pick):
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' and "@" in line[20]:
            if "," in line[20]:
                templine = line[20].split(",")
                lst.append(f"{line[58]},{pick},{templine[0]},{line[2]}")  # когда 2 почты
                lst.append(f"{line[58]},{pick},{templine[1].strip()},{line[2]}\n")
            else:
                lst.append(f"{line[58]},{pick},{line[20]},{line[2]}\n")
            break

    with open(str(datetime.now())[:10] + '_' + export_name, "a", encoding="utf8") as exp:
        exp.write('\n'.join(lst))

#  todo дописать сюда другие функции
