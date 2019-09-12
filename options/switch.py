from datetime import datetime
import traceback


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
    first = easy1
    second = easy2
    # todo дописать сюда другие функции
    return [first, second] # todo здесь формируется массив опций


def easy1(line):
    export_name = who_am_i() + '.csv'
    lst = []
    lst.append(f"{line[1]},{line[20]},{line[2]}\n")
    with open(str(datetime.now())[:10] + '_' + export_name, "a", encoding="utf8") as exp:
        exp.write('\n'.join(lst))


def easy2(line):
    export_name = who_am_i() + '.csv'
    lst = []
    lst.append(f"{line[1]},{line[20]},{line[2]}\n")
    with open(str(datetime.now())[:10] + '_' + export_name, "a", encoding="utf8") as exp:
        exp.write('\n'.join(lst))

# todo дописать сюда другие функции