# Практическое задание 4
print('Напишите программу, которая будет преобразовывать десятичное число в двоичное.')
while True:
    try:
        number = int(input('Введите любое положительное целое число: '))
        if number < 0:
            raise ValueError
        print(number, end=' -> ')
        result = ''
        while number > 0:
            result = str(number % 2) + result
            number = number // 2
        print(result)
        break
    except ValueError:
        print('Допустимые значения: любые положительные целые числа')
