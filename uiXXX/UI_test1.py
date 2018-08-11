
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv) # Создаем обязательный объект приложения

    w = QWidget()   # объект GUI
    w.resize(550, 350)  # задаем размеры
    # w.move(700, 700)    #Перемещение
    w.setWindowTitle('Simple')  # задаем заголовок
    w.show()    # отображает все что создали

    sys.exit(app.exec_())   # основной цикл
