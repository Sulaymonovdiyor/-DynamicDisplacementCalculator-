import re

# Открытие файла и чтение данных
with open('moveA.txt', 'r') as f:
    data = f.readlines()

# Инициализация переменных
time = 0
velocity = [0, 0, 0]
displacement = [0, 0, 0]
g = 9.81

d_time = 1/104

# Обработка данных
for line in data:
    # Поиск значений ускорения в строке
    match = re.search(r'(\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*,', line)
    if match:
        # Преобразование значений в числа
        acceleration = [float(match.group(1)), float(match.group(2)), float(match.group(3)) - g]
        # Вычисление времени
        time += d_time
        # Вычисление скорости
        velocity[0] += acceleration[0] * d_time
        velocity[1] += acceleration[1] * d_time
        velocity[2] += acceleration[2] * d_time
        # Вычисление перемещения
        displacement[0] += velocity[0] * d_time
        displacement[1] += velocity[1] * d_time
        displacement[2] += velocity[2] * d_time

# Вывод результата
print(f'Итоговое перемещение: {displacement[0]*100:.2f} см, {displacement[1]*100:.2f} см, {displacement[2]*100:.2f} см')