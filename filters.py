import csv
import options.switch
from datetime import datetime
from glue import glue

class Table:
    def __init__(self, imp):
        self.source = csv.reader(open(imp, encoding="utf8"), delimiter=";", quotechar='"')


def ops(line, check):
    """
    Функция принимает строку и массив опций, и применяет эти опции к строке поочередно.
    :param line: строка (1 контакт) из импорта
    :param check: массив используемых функций
    :return: не возвращает ничего
    """
    for key, itm in enumerate(check):
        if itm:
            check[key](line)


def main():
    #glue(int(input('Введите число первичных файлов: ')))
    # imp = input('Введите имя файла: ')
    imp = 'amocrm_contacts (total).csv'
    tab = Table(imp)
    i = 0
    check = options.switch.box()

    for line in tab.source:
        i += 1
        #print(f"{i:<5}'st line is: {line[58]:>10}{line[1]:>40}{line[20]:>60}{line[2]:>70}")
        print(f'{i:<5}\'st line is: {line[1]:>40}')
        ops(line, check)


if __name__ == '__main__':
    timer = datetime.now()

    main()

    end = datetime.now()
    total = end - timer
    print(f'\nduration: {str(total)[:7]}')