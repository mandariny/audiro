import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PySide6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from main_page import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.stackedPages.setCurrentIndex(0)
        self.menu_toolBox.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(2)
        #self.label_41.setPixmap(Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, 'qr.png'])
        self.label_41.setPixmap(QPixmap('qr.png'))

    def nextMusic(self):
        currentPage = self.stackedCharts.currentIndex()
        countPage = self.stackedCharts.count()
        if currentPage+1 >= countPage:
            self.stackedCharts.setCurrentIndex(0)
        else:
            self.stackedCharts.setCurrentIndex(currentPage + 1)

    def prevMusic(self):
        currentPage = self.stackedCharts.currentIndex()
        countPage = self.stackedCharts.count()
        if currentPage-1 < 0:
            self.stackedCharts.setCurrentIndex(countPage-1)
        else:
            self.stackedCharts.setCurrentIndex(currentPage-1)

    def playMusic1_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedMemoPages.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(0)

    def playMusic2_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedMemoPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(0)

    def playMusic3_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedMemoPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(0)

    def playMusic1_post(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedMusicPosts.setCurrentIndex(0)

    def playMusic2_post(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedMusicPosts.setCurrentIndex(1)

    def playMusic3_post(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedMusicPosts.setCurrentIndex(2)

    def backToChart(self):
        self.stackedPages.setCurrentIndex(0)

    def backToPosts(self):
        self.stackedPages.setCurrentIndex(2)

    def changeMenu(self, ind):
        if ind == 0:
            self.stackedPages.setCurrentIndex(0)
            self.stackedPages2.setCurrentIndex(2)
        elif ind == 1:
            self.stackedPages.setCurrentIndex(2)
        else:
            self.stackedPages.setCurrentIndex(4)

    def moveToReceivedMail(self):
        self.stackedPages.setCurrentIndex(5)

    def moveToSendMail(self):
        self.stackedPages.setCurrentIndex(7)

    def moveToNextStep(self):
        currentPage = self.stackedPages.currentIndex()
        self.stackedPages.setCurrentIndex(currentPage + 1)

    def reply(self):
        self.stackedPages2.setCurrentIndex(3)

    def postMusic(self):
        self.stackedPages2.setCurrentIndex(3)

app = QApplication()
window = MyWindow()
#window.setFixedWidth(1000)
#window.setFixedHeight(1000)
window.show()

app.exec()

