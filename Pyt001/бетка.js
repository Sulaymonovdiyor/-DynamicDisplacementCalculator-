// Импортировать библиотеку numeric.js
const numeric = require('numeric');

// Частота опроса
const frequency = 104;

// Ускорения по осям X, Y, Z (м/с^2)
const accelerations = [
  [1.2, 2.1, 0.9],
  [0.8, 1.9, 1.2],
  [1.1, 1.8, 1.1],
  // ...
];

// Интегрирование для получения скоростей по осям X, Y, Z
const velocities = accelerations.map(a => a.map(v => v / frequency))
                                .map(numeric.cumsum);

// Интегрирование для получения перемещений на каждом шаге по осям X, Y, Z
const displacements = velocities.map(v => v.map(d => d / frequency))
                                .map(numeric.cumsum);

// Итоговое перемещение в см
const totalDisplacement = displacements[displacements.length - 1].map(d => d * 100);

// Вывод результата
console.log(`Итоговое перемещение: ${totalDisplacement} см`);