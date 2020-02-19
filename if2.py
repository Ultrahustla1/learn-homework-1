string1 = input('Введите строку: ')
string2 = input('Введите строку: ')

def strings(string1, string2):
    if string1 == string2:
        return '1'
    elif string1 != string2:
        if len(string1) > len(string2):
            return '2'
        elif string2 == 'learn':
            return '3'

print(strings(string1, string2))