import csv
import options.switch


class Filter:
    def __init__(self, imp):
        self.source = csv.reader(open(imp, encoding="utf8"), delimiter=';', quotechar='"')


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
    # imp = input("Введите имя файла: ")
    imp = 'amocrm_contacts (total).csv'
    core = Filter(imp)
    i = 0
    check = options.switch.box()
    for line in core.source:
        i += 1
        print(f"{i:<5}'st line is: {line[58]:>10}{line[1]:>40}{line[20]:>60}{line[2]:>70}")
        ops(line, check)


if __name__ == '__main__':
    main()