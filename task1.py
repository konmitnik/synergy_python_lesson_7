string = input('Введите строку без пробелов: ')

if string == string[::-1]:
    print('yes')
else:
    print('no')