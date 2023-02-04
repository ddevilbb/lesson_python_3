# Практическое задание 5
print('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')


def fib(index):
    if index == 0 or index == 1:
        return index
    return fib(index-1) + fib(index-2)


def negative_fib(index):
    if index == 0:
        return 0
    elif index == -1:
        return 1
    return negative_fib(index + 2) - negative_fib(index + 1)


while True:
    try:
        k = int(input('Введите любое положительное число: '))
        if k < 0:
            raise ValueError
        fibList = [0]
        for i in range(1, k + 1):
            fibList.append(fib(i))
            fibList.insert(0, negative_fib(-i))
        print(fibList)
        break
    except ValueError:
        print('Допустимые значения: любое положительное число')
