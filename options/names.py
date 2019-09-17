import re


def single(name):
    order = name.split(',')
    if re.search('(ович$)|(евич$)|(овна$)|(евна$)', order[0]):  # иванОВИЧ
        return f',,{order[0]}'
    elif re.search('(ов$)|(ев$)|(ова$)|(ева$)', order[0]):  # иванОВ
        return f',,{order[0]}'
    else:
        return f'{order[0]},,'  # сохраняет изначальный порядок


def double(name):
    order = name.split(',')
    if re.search('(ович$)|(евич$)|(овна$)|(евна$)', order[2]): # иван иванОВИЧ
        return f'{order[0]},{order[2]},'
    elif re.search('(ов$)|(ев$)|(ова$)|(ева$)', order[2]): # иван иванОВ
        return f'{order[0]},,{order[2]}'
    elif re.search('(ов$)|(ев$)|(ова$)|(ева$)', order[0]): # иванОВ иван
        return f'{order[2]},,{order[0]}'
    else:
        return f'{order[0]},,{order[2]}'  # сохраняет изначальный порядок


def triple(name):
    order = name.split(',')
    if re.search('(ович$)|(евич$)|(овна$)|(евна$)', order[0]):  # семенОВИЧ иван иванович
        return f'{order[1]},{order[2]},{order[0]}'
    elif re.search('(ович$)|(евич$)|(овна$)|(евна$)', order[1]):  # иван иванОВИЧ иванов
        return f'{order[0]},{order[1]},{order[2]}'
    elif re.search('(ович$)|(евич$)|(овна$)|(евна$)', order[2]):  # иванов иван иванОВИЧ
        return f'{order[1]},{order[2]},{order[0]}'

    elif re.search('(ов$)|(ев$)|(ова$)|(ева$)', order[0]):  # иванОВ иван иванович
        return f'{order[1]},{order[2]},{order[0]}'
    elif re.search('(ов$)|(ев$)|(ова$)|(ева$)', order[2]):  # иван иванович иванОВ
        return f'{order[0]},{order[1]},{order[2]}'

    else:
        return f'{order[0]},{order[1]},{order[2]}'  # сохраняет изначальный порядок


def splitter(line):
    line = line.replace('  ', ' ')
    name = line.split(' ')

    if len(name) == 1:
        return single(f'{name[0]},,')
    elif len(name) == 2:
        return double(f'{name[0]},,{name[1]}')
    elif len(name) == 3:
        return triple(f'{name[0]},{name[1]},{name[2]}')
    else:
        mid = ' '.join(name[1:-1])
        return f'{name[0]},{mid},{name[-1]}'


def main():
    # line0 = 'Иванов'
    # line1 = 'Иван'
    # line2 = 'Иванович'
    # line3 = 'Иванов Иван'
    # line4 = 'Иван Иванов'
    # line5 = 'Иван Иванович'
    # line6 = 'Иван Иванович Иванов'
    # line7 = 'Иванов Иван Иванович'

    line0 = 'Анатолие'
    line1 = 'Тараненко'
    #line2 = 'Петрович'
    line3 = 'Анатолие Тараненко'
    line4 = 'Тараненко Анатолие'
    #line5 = 'Петр Петрович'
    #line6 = 'Петр Петрович Петров'
    #line7 = 'Петров Петр Петрович'

    print(splitter(line0))
    print(splitter(line1))
    #print(splitter(line2))
    print(splitter(line3))
    print(splitter(line4))
    #print(splitter(line5))
    #print(splitter(line6))
    #print(splitter(line7))


if __name__ == '__main__':
    main()


