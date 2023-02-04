# Практическое задание 1
print('Задайте список из нескольких чисел. '
      'Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
while True:
    try:
        numbers = list(map(int, input("Введите несколько чисел через пробел: ").strip().split()))
        result = 0
        lenNumbers = len(numbers)
        for i in range(lenNumbers):
            if i % 2 > 0:
                print(numbers[i], end=(' + ' if i < (lenNumbers - 2) else ' = '))
                result += numbers[i]
        print(result)
        break
    except ValueError:
        print('Допустимые значения: любые целые числа')
