import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton
import numpy as np
#это времное решения, я попробую решить 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Определение перемещения")
        self.setGeometry(100, 100, 400, 400)
        
        # Добавить метку и поле ввода для частоты опроса
        self.freq_label = QLabel("Частота опроса (Гц):", self)
        self.freq_label.setGeometry(20, 20, 150, 30)
        self.freq_input = QLineEdit(self)
        self.freq_input.setGeometry(170, 20, 200, 30)
        
        # Добавить метку для выбранного файла
        self.file_label = QLabel("", self)
        self.file_label.setGeometry(20, 70, 350, 30)
        
        # Добавить кнопку для выбора файла
        self.file_button = QPushButton("Выбрать файл", self)
        self.file_button.setGeometry(20, 120, 150, 30)
        self.file_button.clicked.connect(self.open_file_dialog)
        
        # Добавить кнопку для начала обработки данных
        self.process_button = QPushButton("Обработать данные", self)
        self.process_button.setGeometry(20, 170, 150, 30)
        self.process_button.clicked.connect(self.process_data)
        
        # Добавить метку и поле вывода для итогового перемещения
        self.result_label = QLabel("Итоговое перемещение:", self)
        self.result_label.setGeometry(20, 220, 150, 30)
        self.result_output = QLineEdit(self)
        self.result_output.setGeometry(170, 220, 200, 30)
        self.result_output.setReadOnly(True)
    #открыть файли
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,"Выбрать файл с ускорениями", "","CSV Files (*.csv)", options=options)
        if file_name:
            self.file_label.setText(file_name)
    
    def process_data(self):
        file_name = self.file_label.text()
        freq = float(self.freq_input.text())
        
        # Прочитать данные из файла и преобразовать в массив NumPy с этим проблемы
        data = np.loadtxt(file_name, delimiter=",")
        
        # Вычислить перемещение на каждом шаге
        dt = 1 / freq
        vel = np.cumsum(data * dt, axis=0)
        disp = np.cumsum(vel * dt, axis=0)
        result = disp[-1] * 1000  # конвертировать в мм
        
        # Вывести итоговое перемещение
        self.result_output.setText(f"{result:.2f} мм")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())