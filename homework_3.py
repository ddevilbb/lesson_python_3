# Практическое задание 3
print('Задайте список из вещественных чисел. '
      'Напишите программу, которая найдёт разницу '
      'между максимальным и минимальным значением дробной части элементов.')


def get_precision(number):
    s = str(number)
    return abs(s.find('.') - len(s)) - 1 if '.' in s else 0


while True:
    try:
        numbers = list(map(float, input("Введите несколько чисел через пробел: ").strip().split()))
        maxPrecision = max([get_precision(i) for i in numbers])
        newList = [round(abs(i) % 1, maxPrecision) for i in numbers if i % 1 != 0]
        print(f'{numbers} => {round(max(newList) - min(newList), maxPrecision)}')
        break
    except ValueError:
        print('Допустимые значения: любые вещественные числа')
