# Предоставленный список персональных данных
personal_data = [
    {"имя": "Анна", "возраст": 25, "пол": "женский", "рост": 165, "вес": 60},
    {"имя": "Иван", "возраст": 30, "пол": "мужской", "рост": 180, "вес": 80},
    {"имя": "Мария", "возраст": 40, "пол": "женский", "рост": 170, "вес": 65},
    {"имя": "Петр", "возраст": 35, "пол": "мужской", "рост": 175, "вес": 75}
]

# Вычисляем средний возраст
total_age = sum(person["возраст"] for person in personal_data)
average_age = total_age / len(personal_data)

print("Средний возраст всех персон в списке:", average_age)
