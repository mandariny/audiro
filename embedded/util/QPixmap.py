import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        self.setCentralWidget(widget)
        widget.setPixmap(QPixmap('qr.png'))

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
