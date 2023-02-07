import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt, QSize, QPoint
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from PySide6.QtWidgets import *

class MyWidget(QPanGesture):
    def __init__(self, parent=None):
        super().__init__(parent)




class MainWindow(QMainWindow):
    """An Application example to draw using a pen """

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.QPanGesture = MyWidget()