# ACCELERATION
Давайте начнем с решения первой части задачи: определения перемещения на каждом шаге и затем итогового перемещения на основе данных об ускорениях.


# Перемещение на основе ускорения
def displacement_from_acceleration(accelerations, time_interval):
    displacements = []
    current_velocity = 0
    current_displacement = 0

  for accel in accelerations:
        # Используем уравнение движения для равноускоренного движения: s = ut + (1/2)at^2
        current_displacement += current_velocity * time_interval + 0.5 * accel * (time_interval ** 2)
        # Находим текущую скорость поступательного движения: v = u + at
        current_velocity += accel * time_interval
        displacements.append(current_displacement)

    return displacements

# Ускорения
accelerations = [0] * 100  # Заполняем ускорениями (в этом примере все ускорения равны 0)

# Шаг времени (в секундах)
time_interval = 1 / 104  # Переводим частоту опроса из Гц в секунды

# Рассчитываем перемещения на каждом шаге
displacements = displacement_from_acceleration(accelerations, time_interval)

# Итоговое перемещение (сумма всех перемещений)
total_displacement = displacements[-1]

print("Перемещения на каждом шаге (в метрах):", displacements)
print("Итоговое перемещение (в метрах):", total_displacement)



Теперь, решим обратную задачу - определить перемещение по ускорениям. Для этого нужно проинтегрировать ускорения для получения скорости, а затем проинтегрировать скорость для получения перемещения.

python
import numpy as np

# Обратное интегрирование для определения перемещения по ускорениям
def displacement_from_acceleration_reverse(accelerations, time_interval):
    velocities = np.zeros_like(accelerations)
    displacements = np.zeros_like(accelerations)

  for i in range(1, len(accelerations)):
        # Находим текущую скорость поступательного движения: v = u + at
        velocities[i] = velocities[i-1] + accel[i] * time_interval
        # Используем уравнение движения для равноускоренного движения: s = ut + (1/2)at^2
        displacements[i] = displacements[i-1] + velocities[i] * time_interval + 0.5 * accel[i] * (time_interval ** 2)

  return displacements

# Пример ускорений
accelerations_example = np.array([0] * 100)  # Заполняем ускорениями (в этом примере все ускорения равны 0)

# Шаг времени (в секундах)
time_interval_example = 1 / 104  # Переводим частоту опроса из Гц в секунды

# Рассчитываем перемещения по ускорениям
displacements_reverse = displacement_from_acceleration_reverse(accelerations_example, time_interval_example)

print("Перемещения на каждом шаге (в метрах) по ускорениям:", displacements_reverse)
```

В этом примере мы использовали библиотеку NumPy для более эффективной работы с массивами чисел.
