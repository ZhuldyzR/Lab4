from itertools import product

# Списки продуктов
breads = ['белый хлеб', 'ржаной хлеб', 'багет']
meats = ['ветчина', 'курица', 'свинина']
vegetables = ['помидоры', 'салат', 'огурцы']
sauces = ['горчица', 'кетчуп', 'майонез']

# Генерация всех возможных комбинаций сэндвичей
sandwiches = list(product(breads, meats, vegetables, sauces))

# Вывод всех комбинаций сэндвичей
for sandwich in sandwiches:
    print('Сэндвич с', sandwich[0], ',', sandwich[1], ',', sandwich[2], 'и', sandwich[3])
