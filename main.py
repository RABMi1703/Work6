# Импортируем библиотеки
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from time import sleep

# Создаём класс на основе QWidget
class Calculator(QWidget):
    def __init__(self) -> None:
        # Передаем классу методы QWidget
        super(Calculator, self).__init__()

        # Создаём окна
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QVBoxLayout(self)
        self.hbox_first = QVBoxLayout(self)
        self.hbox_result = QVBoxLayout(self)

        # Создаём слои
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        # Создаём методы ввода данных
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # Создаём кнопки

        # Цифры и плавающая точка
        self.b_0 = QPushButton('0', self)
        self.hbox_first.addWidget(self.b_0)

        self.b_1 = QPushButton('1', self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton('2', self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton('3', self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton('4', self)
        self.hbox_first.addWidget(self.b_4)

        self.b_5 = QPushButton('5', self)
        self.hbox_first.addWidget(self.b_5)

        self.b_6 = QPushButton('6', self)
        self.hbox_first.addWidget(self.b_6)

        self.b_7 = QPushButton('7', self)
        self.hbox_first.addWidget(self.b_7)

        self.b_8 = QPushButton('8', self)
        self.hbox_first.addWidget(self.b_8)

        self.b_9 = QPushButton('9', self)
        self.hbox_first.addWidget(self.b_9)

        self.b_dot = QPushButton('.', self)
        self.hbox_first.addWidget(self.b_dot)

        # Операции
        self.b_plus = QPushButton('+', self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton('-', self)
        self.hbox_first.addWidget(self.b_minus)

        self.b_multiple = QPushButton('*', self)
        self.hbox_first.addWidget(self.b_multiple)

        self.b_deriv = QPushButton('/', self)
        self.hbox_first.addWidget(self.b_deriv)

        self.b_sqrt = QPushButton('sqrt', self)
        self.hbox_first.addWidget(self.b_sqrt)

        self.b_result = QPushButton('=', self)
        self.hbox_first.addWidget(self.b_result)

        # Привязываем действия к кнопкам
        self.b_0.clicked.connect(lambda: self._button('0'))
        self.b_1.clicked.connect(lambda: self._button('1'))
        self.b_2.clicked.connect(lambda: self._button('2'))
        self.b_3.clicked.connect(lambda: self._button('3'))
        self.b_4.clicked.connect(lambda: self._button('4'))
        self.b_5.clicked.connect(lambda: self._button('5'))
        self.b_6.clicked.connect(lambda: self._button('6'))
        self.b_7.clicked.connect(lambda: self._button('7'))
        self.b_8.clicked.connect(lambda: self._button('8'))
        self.b_9.clicked.connect(lambda: self._button('9'))
        self.b_dot.clicked.connect(lambda: self._button('.'))

        self.b_plus.clicked.connect(lambda: self._operation('+'))
        self.b_minus.clicked.connect(lambda: self._operation('-'))
        self.b_multiple.clicked.connect(lambda: self._operation('*'))
        self.b_deriv.clicked.connect(lambda: self._operation('/'))
        self.b_sqrt.clicked.connect(lambda: self._operation('sqrt'))
        self.b_result.clicked.connect(self._result)

        # Начальные значения
        self.num_1 = self.op = self.num_2 = None

    def _button(self, param) -> None:
        # Добавление цифры к строке
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op) -> None:
        # Запоминаем число и операцию, зануляя строку для ввода нового числа
        try:
            float(self.input.text())
        except ValueError:
            if self.input.text() == '':
                if op == '-':
                    self.input.setText('-')
                else:
                    self.input.setText('')
            else:
                self.input.setText('Input error')
                sleep(1)
                self.input.setText('')
        else:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText('')

    def _result(self) -> None:
        # Обрабатываем второе число и выводим результат
        try:
            float(self.input.text())
        except ValueError:
            if self.op == 'sqrt':
                if self.num_1 < 0:
                    result = 'Root of Negative Number'
                else:
                    result = self.num_1 ** .5
            elif self.input.text() == '':
                result = "You don't input number 2. Try again"
        else:
            self.num_2 = float(self.input.text())
            if self.op == '+':
                result = self.num_1 + self.num_2
            elif self.op == '-':
                result = self.num_1 - self.num_2
            elif self.op == '*':
                result = self.num_1 * self.num_2
            elif self.op == '/':
                try:
                    self.num_1 / self.num_2
                except ZeroDivisionError:
                    result = 'Division on Zero'
                else:
                    result = self.num_1 / self.num_2
            elif self.op == 'sqrt':
                if self.num_1 < 0:
                    result = 'Root of Negative Number'
                else:
                    result = self.num_1 ** .5

        # Обработка ошибки
        if type(result) == float:
            # Убираем лишние нули
            result = round(result, 16)
            if result % 1 == 0:
                result = int(result)
            self.input.setText(str(result))
        else:
            self.input.setText(result)
            sleep(1)
            self.input.setText('')

def main() -> None:
    # Создаём приложение
    app = QApplication(sys.argv)

    # Создаём окно
    window = Calculator()
    window.show()

    # Выходим из программы
    sys.exit(app.exec_())

main()
