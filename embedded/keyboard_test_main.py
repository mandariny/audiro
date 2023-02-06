import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5 import QtCore
from keyboard_test import Ui_MainWindow

import Keyboard

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.widget.display()

app = QApplication(sys.argv)
window = MyWindow()
window.setFixedWidth(1200)
window.setFixedHeight(800)
window.show()

app.exec()
