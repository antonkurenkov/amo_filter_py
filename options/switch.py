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
    third = trash
    # todo дописать сюда другие функции
    # return [first, second]
    return [third]  # todo здесь формируется массив опций


def doublemail(line, pick):
    lst = []
    if ',' in line[20]:
        _ = line[20].split(',')
        lst.append(f'{line[58]},{pick},{_[0]},{line[2]}')  # когда 2 почты
        lst.append(f'{line[58]},{pick},{_[1].strip()},{line[2]}\n')
    else:
        lst.append(f'{line[58]},{pick},{line[20]},{line[2]}\n')
    return lst


def donot():
    return []

########################################################################################################################
########################################################################################################################


def easy1(line):
    export_name = who_am_i() + '.csv'
    lst = []
    lst.append(f'{line[1]},{line[20]},{line[2]}\n')
    with open(str(datetime.now())[:10] + '_' + export_name, 'a', encoding='utf8') as exp:
        exp.write('\n'.join(lst))


def cyr(line):
    """
    Только кириллические буквы в имени (не считая запятых и проблелов)
    :param line:
    :return:
    """
    export_name = who_am_i() + '.csv'
    pick = splitter(line[1])
    lst = doublemail(line, pick) if '@' in line[20] and not bool(list(filter(lambda x: x not in ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя', line[1]))) else []
    with open(str(datetime.now())[:10] + '_' + export_name, 'a', encoding='utf8') as exp:
        exp.write('\n'.join(lst))
        #print(lst)


def lat(line):
    """
    Только латинские буквы в имени (не считая запятых и проблелов)
    :param line:
    :return:
    """
    export_name = who_am_i() + '.csv'
    pick = splitter(line[1])

    lst = doublemail(line, pick) if '@' in line[20] and not bool(list(filter(lambda x: x not in ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', line[1]))) else []
    with open(str(datetime.now())[:10] + '_' + export_name, 'a', encoding='utf8') as exp:
        exp.write('\n'.join(lst))
        #print(lst)


def trash(line):
    """
    Когда в имени и кириллица и латиница
    :param line:
    :return:
    """
    export_name = who_am_i() + '.csv'
    pick = splitter(line[1])

    c = False
    l = False
    s = False

    for letter in line[1]:
        if letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            c = True
            break
    for letter in line[1]:
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            l = True
            break
    for letter in line[1]:
        if letter in '`1234567890=~!@#$%^&*()_+/?<>,':
            s = True
            break

    lst = doublemail(line, pick) if '@' in line[20] and ((c and l) or s) else []
    with open(str(datetime.now())[:10] + '_' + export_name, 'a', encoding='utf8') as exp:
        exp.write('\n'.join(lst))
        #print(lst)


#  todo дописать сюда другие функции
#doublemail(line, lst, pick) if False not in list(map(lambda x: x not in c2, str(pick))) else donot()