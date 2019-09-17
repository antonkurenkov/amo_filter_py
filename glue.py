import csv


def glue(num):
    for i in range(1, num):
        name = 'amocrm_contacts (' + str(i) + ').csv'
        source = csv.reader(open(name, encoding="utf8"), delimiter=';', quotechar='"')
        with open('amocrm_contacts (total).csv', 'a', encoding='utf8') as dest:
            for line in source:
                line = str(line)
                line = line.replace('\'', '"')
                line = line.replace(', ', ';')
                dest.write(f'{str(line)[1:-1]}\n')
            print(i)
