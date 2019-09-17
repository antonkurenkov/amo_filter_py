# box = ['васяasasaывывыsdfdf', 'sdfffs', 'sdsdsds', 'вася']
# for pick in box:
#     for letter in str(pick):
#         if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' and letter not in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя':
#             print(pick)
#             break
#         print(pick)


# cyrilic = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя '
# latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
# name1 = 'миша (do not work)'
# name2 = 'john (не работает)'
#
# print(name1) if False not in list(filter(lambda x: x not in latin, name1)) else print('some lat')
# print(name2) if False not in list(filter(lambda x: x not in latin, name1)) else print('some lat')
#
#
# print(name2) if False not in list(filter(lambda x: x not in cyrilic, name2)) else print('some cyr')
# print(name1) if False not in list(filter(lambda x: x not in cyrilic, name2)) else print('some cyr')
#
#
# print(list(filter(lambda x: x not in latin, name2)))
# print(list(filter(lambda x: x not in cyrilic, name1)))
#
# name3 = 'Иван Иванов'
# name4 = 'John Smithы'
#
# def donot():
#     pass
#
# print(name3) if not list(filter(lambda x: x not in cyrilic, name3)) else print('wrong!')
# print(name4) if not list(filter(lambda x: x not in latin, name4)) else print('wrong!')
#
#
# sss = name3 if not list(filter(lambda x: x not in ' АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя', name3)) else 'ыыы'
# print(sss)
# print("------------------")
#
# pick = 'Полное,имя,контакта'
#
# lst = 1 if not bool(list(filter(lambda x: x not in ' АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя', pick))) else 2
# print(lst)

a = 'Геннaдьевич'
b = 'Геннадьевич'

c = 'Геннадьевич'
d = 'Геннадьевич'


if a == b:
    print('a')

if c == d:
    print('c')