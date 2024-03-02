import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создание виджетов
        self.button = QPushButton('Открыть файл')
        self.text_area = QTextEdit()

        # Создание вертикального контейнера для виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.text_area)

        # Установка макета для главного окна
        self.setLayout(layout)

        # Назначение действия для кнопки
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Открытие файла и чтение данных
        file_name, _ = QFileDialog.getOpenFileName(self, 'Выбрать файл', '.', 'Text Files (*.txt)')
        with open(file_name, 'r') as f:
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

        # Вывод результата в текстовое поле
        result = f'Итоговое перемещение: {displacement[0]*100:.2f} см, {displacement[1]*100:.2f} см, {displacement[2]*100:.2f} см'
        self.text_area.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

