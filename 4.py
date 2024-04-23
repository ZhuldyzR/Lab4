even_sum = 0
odd_sum = 0

for number in range(1, 101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("Сумма четных чисел:", even_sum)
print("Сумма нечетных чисел:", odd_sum)
