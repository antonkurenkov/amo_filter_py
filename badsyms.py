import csv
from datetime import datetime

class Table:
    def __init__(self, imp):
        self.source = csv.reader(open(imp, encoding="utf8"), delimiter=";", quotechar='"')


def main():

    imp = 'amocrm_contacts (total).csv'
    tab = Table(imp)
    i = 0

    for line in tab.source:
        i += 1

        lst = [x if x not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя' and
                         x not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' and
                         x not in '' else '' for x in line[1]]
        with open(str(datetime.now())[:10] + '_' + 'badsyms.csv', 'a', encoding='utf8') as exp:
            exp.write(''.join(lst))

        print(f'{i:<5}\'st line is: {line[1]:>40}')


if __name__ == '__main__':
    timer = datetime.now()

    main()

    end = datetime.now()
    total = end - timer
    print(f'\nduration: {str(total)[:7]}')