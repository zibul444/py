# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):     # наследуемся от класса QWidget

    def __init__(self):     # конструктор
        super().__init__()

        self.initUI()       # Создание GUI

    def initUI(self):       # создаем инстанс окна, задаем ему параметры

        self.setGeometry(300, 300, 300, 220)    # расположение и размер
        self.setWindowTitle('Icon')             # заголовок
        self.setWindowIcon(QIcon('icon.png'))   # иконка
        self.show()                             # команда отобразить

if __name__ == '__main__':            # процесс вызова того что накодили

    app = QApplication(sys.argv)      # Создание объекта приложения
    ex = Example()                    # вызов говнокода
    sys.exit(app.exec_())             # основной цикл программы : чистый выход
