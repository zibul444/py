# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QIcon, QFont

class Example(QWidget):     # наследуемся от класса QWidget

    def __init__(self):     # конструктор
        super().__init__()

        self.initUI()       # Создание GUI


    def initUI(self):       # создаем инстанс окна, задаем ему параметры

        QToolTip.setFont(QFont('SansSerif', 10))    #

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)        # расположение и размер
        self.setWindowTitle('Icon')                 # заголовок
        self.setWindowIcon(QIcon('icon.png'))       # иконка
        self.show()                                 # команда отобразить

if __name__ == '__main__':            # процесс вызова того что накодили

    app = QApplication(sys.argv)      # Создание объекта приложения
    ex = Example()                    # вызов говнокода
    sys.exit(app.exec_())             # основной цикл программы : чистый выход
