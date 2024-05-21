from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value, LpStatus

# Створення проблеми лінійного програмування
model = LpProblem(name="maximize_drinks_production", sense=LpMaximize)

# Змінні рішень: кількість вироблених одиниць лимонаду та фруктового соку
x = LpVariable(name="lemonade", lowBound=0, cat='Integer')
y = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Обмеження ресурсів
model += (2 * x + y <= 100, "water_constraint")
model += (x <= 50, "sugar_constraint")
model += (x <= 30, "lemon_juice_constraint")
model += (2 * y <= 40, "fruit_puree_constraint")

# Функція цілі: максимізація загальної кількості вироблених напоїв
model += lpSum([x, y])

# Розв'язання проблеми
model.solve()

# Перевірка статусу рішення
status = LpStatus[model.status]
print(f"Статус: {status}")

if status == 'Optimal':
    # Виведення результатів
    print(f"Кількість виробленого лимонаду: {value(x)}")
    print(f"Кількість виробленого фруктового соку: {value(y)}")
    print(f"Загальна кількість вироблених напоїв: {value(x) + value(y)}")
else:
    print("Оптимальне рішення не знайдено.")
