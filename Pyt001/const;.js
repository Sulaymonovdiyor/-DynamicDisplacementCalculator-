const fs = require('fs');

// Частота опроса
const samplingFrequency = 104; // Гц

// Шаг времени
const timeStep = 1 / samplingFrequency;

// Масштаб для перевода метров в миллиметры const scale = 1000;

// Чтение ускорений из файла
const accelerations = fs.readFileSync('moveX.csv', 'utf-8')
.trim()
.split('\n')
.map(line => line.split(' ').map(Number));

// Преобразование ускорений из м/с² в мм/с²
const accelerationsScaled = accelerations.map(([x, y, z]) => [ x * scale,
y * scale, z * scale,
]);

// Вычисление перемещений для каждой оси let velocities = [0, 0, 0];
let displacements = [0, 0, 0];
for (let i = 1; i < accelerationsScaled.length; i++)
{ const [ax, ay, az] = accelerationsScaled[i]; const [vx0, vy0, vz0] = velocities;
const [dx0, dy0, dz0] = displacements;

// Вычисление скорости
const vx = vx0 + ((ax + accelerationsScaled[i-1][0]) / 2) * timeStep; const vy = vy0 + ((ay + accelerationsScaled[i-1][1]) / 2) * timeStep; const vz = vz0 + ((az + accelerationsScaled[i-1][2]) / 2) * timeStep;

// Вычисление перемещения
const dx = dx0 + ((vx + vx0) / 2) * timeStep; const dy = dy0 + ((vy + vy0) / 2) * timeStep; const dz = dz0 + ((vz + vz0) / 2) * timeStep;

velocities = [vx, vy, vz]; displacements = [dx, dy, dz];
}

// Вычисление итогового перемещения const totalDisplacement = Math.sqrt
(displacements[0] ** 2 + displacements[1] ** 2 + displacements[2] ** 2);

console.log(`Итоговое перемещение: ${totalDisplacement.toFixed(2)} мм`);координат