import numpy as np
from scipy.integrate import cumulative_trapezoid
# Загрузка данных из файла
data = np.loadtxt('accelerations.txt')
dt = 1/104 
# Шаг времениИнициализация переменных
vx=cumulative_trapezoid(data[:,0], dx=dt, initial=0)

vy = cumulative_trapezoid(data[:,1], dx=dt, initial=0)

vz = cumulative_trapezoid(data[:,2], dx=dt, initial=0)

x = cumulative_trapezoid(vx, dx=dt, initial=0)

y = cumulative_trapezoid(vy, dx=dt, initial=0)

z = cumulative_trapezoid(vz, dx=dt, initial=0)

# Вычисление итогового перемещения

displacement = np.sqrt(x[-1]**2 + y[-1]**2 + z[-1]**2) * 1000 # в мм 
#надо дописать print
print