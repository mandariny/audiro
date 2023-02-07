import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PySide6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from test1 import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)

    def nextPage(self):
        currentPage = self.stackedWidget.currentIndex()
        countPage = self.stackedWidget.count()
        if currentPage+1 >= countPage:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(currentPage + 1)

    def prevPage(self):
        currentPage = self.stackedWidget.currentIndex()
        countPage = self.stackedWidget.count()
        if currentPage-1 < 0:
            self.stackedWidget.setCurrentIndex(countPage-1)
        else:
            self.stackedWidget.setCurrentIndex(currentPage-1)

app = QApplication()
window = MyWindow()
window.show()

app.exec()

