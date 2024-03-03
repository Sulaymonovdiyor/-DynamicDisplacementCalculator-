import numpy as np

# заданные ускорения в м/с^2
accelerations = np.array([[0.66, -0.09, 10.04],
                          [0.56, -0.14, 9.91],
                          [0.82, 0.10, 10.34],
                          [0.75, -0.06, 9.91],
                          [0.71, 0.01, 10.17],
                          [0.69, 0.03, 10.27],
                          [0.73, 0.01, 10.15],
                          [0.70, -0.02, 10.19],
                          [0.74, -0.01, 10.18],
                          [0.70, 0.06, 10.24],
                          [0.70, 0.03, 10.23],
                          [0.70, -0.06, 10.02],
                          [0.70, -0.03, 10.10],
                          [0.70, -0.02, 10.10],
                          [0.73, 0.05, 10.25],
                          [0.70, -0.03, 10.10],
                          [0.71, -0.03, 10.08]])
# переводим ускорения из м/с^2 в см/с^2
accelerations *= 100

# переводим частоту опроса в секунды
sampling_rate = 104
time_step = 1 / sampling_rate

# вычисляем перемещения по осям X, Y и Z
displacements = np.zeros_like(accelerations)
for i in range(1, len(accelerations)):
    displacements[i] = displacements[i-1] + time_step * (accelerations[i-1] + accelerations[i]) / 2

# вычисляем итоговое перемещение
total_displacement = np.sqrt(np.sum(displacements[-1]**2))

# выводим результаты
print("Перемещения на каждом шаге:")
print(displacements)
print("Итоговое перемещение: {:.2f} мм".format(total_displacement * 10))