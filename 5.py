def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Введите число для вычисления факториала: "))
    if num < 0:
        print("Факториал определен только для неотрицательных чисел.")
    else:
        result = factorial(num)
        print("Факториал числа", num, "равен", result)
except ValueError:
    print("Ошибка: Введено некорректное значение.")
