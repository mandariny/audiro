import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5 import QtCore
from keyboard_test import Ui_MainWindow

import Keyboard
from jamo import h2j, j2hcj

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.widget.display()

app = QApplication(sys.argv)
a = "안녕하세요"
print(h2j(a))
print(j2hcj(h2j(a)))
window = MyWindow()
window.setFixedWidth(1200)
window.setFixedHeight(800)
window.show()

app.exec()
