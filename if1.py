age = int(input("Введите возраст: "))

def main(age):
    if age < 6:
        return 'Детский сад'
    elif 6 <= age <= 17:
        return 'Школа'
    elif 18 <= age <= 23:
        return 'Вуз'
    else:
        return 'Работа'

print(main(age))
