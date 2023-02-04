# Практическое задание 5
print('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')


def fib(index):
    if index == 0 or index == 1:
        return index
    return fib(index-1) + fib(index-2)


while True:
    try:
        k = int(input('Введите любое положительное число: '))
        if k < 0:
            raise ValueError
        fibList = [0]
        for i in range(1, k + 1):
            fibNumber = fib(i)
            fibList.append(fibNumber)
            fibList.insert(0, fibNumber * (-1 if i % 2 == 0 else 1))
        print(fibList)
        break
    except ValueError:
        print('Допустимые значения: любое положительное число')
