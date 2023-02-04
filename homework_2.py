# Практическое задание 2
print('Напишите программу, которая найдёт произведение пар чисел списка. '
      'Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
while True:
    try:
        numbers = list(map(int, input("Введите несколько чисел через пробел: ").strip().split()))
        resultList = []
        for i in range(int(-1 * len(numbers) // 2 * -1)):
            resultList.append(numbers[i] * numbers[-i - 1])
        print(f'{numbers} => {resultList}')
        break
    except ValueError:
        print('Допустимые значения: любые целые числа')
