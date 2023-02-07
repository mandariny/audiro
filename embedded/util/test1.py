# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 30, 800, 480))
        self.frame_2.setMinimumSize(QSize(800, 480))
        self.frame_2.setMaximumSize(QSize(800, 480))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(200, 0))
        self.frame_23.setMaximumSize(QSize(200, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 200))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_25)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_Name_2 = QLabel(self.frame_37)
        self.label_Name_2.setObjectName(u"label_Name_2")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_Name_2.setFont(font)
        self.label_Name_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_Name_2)


        self.verticalLayout_25.addWidget(self.frame_37)

        self.toolBox = QToolBox(self.frame_25)
        self.toolBox.setObjectName(u"toolBox")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_10 = QVBoxLayout(self.page_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.toolBox.addItem(self.page_4, u"Page 1")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 196, 43))
        self.verticalLayout_14 = QVBoxLayout(self.widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_14.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_14.addWidget(self.label_2)

        self.toolBox.addItem(self.widget, u"Page")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 100, 30))
        self.toolBox.addItem(self.page_5, u"Page 2")

        self.verticalLayout_25.addWidget(self.toolBox)

        self.frame_38 = QFrame(self.frame_25)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_38)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_25.addWidget(self.frame_38)


        self.verticalLayout_13.addWidget(self.frame_25)

        self.frame_39 = QFrame(self.frame_23)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_39)


        self.horizontalLayout_2.addWidget(self.frame_23)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Tags = QFrame(self.frame_4)
        self.Tags.setObjectName(u"Tags")
        self.Tags.setMinimumSize(QSize(0, 50))
        self.Tags.setMaximumSize(QSize(16777215, 50))
        self.Tags.setFrameShape(QFrame.StyledPanel)
        self.Tags.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Tags)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tag1 = QPushButton(self.Tags)
        self.tag1.setObjectName(u"tag1")

        self.horizontalLayout_4.addWidget(self.tag1)

        self.tag2 = QPushButton(self.Tags)
        self.tag2.setObjectName(u"tag2")

        self.horizontalLayout_4.addWidget(self.tag2)

        self.tag3 = QPushButton(self.Tags)
        self.tag3.setObjectName(u"tag3")

        self.horizontalLayout_4.addWidget(self.tag3)

        self.tag4 = QPushButton(self.Tags)
        self.tag4.setObjectName(u"tag4")

        self.horizontalLayout_4.addWidget(self.tag4)

        self.tag5 = QPushButton(self.Tags)
        self.tag5.setObjectName(u"tag5")

        self.horizontalLayout_4.addWidget(self.tag5)

        self.tag6 = QPushButton(self.Tags)
        self.tag6.setObjectName(u"tag6")

        self.horizontalLayout_4.addWidget(self.tag6)


        self.verticalLayout.addWidget(self.Tags)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(100, 50))
        self.frame_9.setMaximumSize(QSize(100, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.priorityBox = QComboBox(self.frame_9)
        self.priorityBox.addItem("")
        self.priorityBox.addItem("")
        self.priorityBox.addItem("")
        self.priorityBox.setObjectName(u"priorityBox")
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.priorityBox.setFont(font1)

        self.horizontalLayout_6.addWidget(self.priorityBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_9, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(100, 50))
        self.frame_11.setMaximumSize(QSize(100, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.full_listBox = QPushButton(self.frame_11)
        self.full_listBox.setObjectName(u"full_listBox")

        self.horizontalLayout_3.addWidget(self.full_listBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(50, 0))
        self.frame_13.setMaximumSize(QSize(50, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_13)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.leftButton = QPushButton(self.frame_13)
        self.leftButton.setObjectName(u"leftButton")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.leftButton.setFont(font2)
        self.leftButton.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.leftButton)


        self.horizontalLayout_5.addWidget(self.frame_13)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_16 = QFrame(self.page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.graphicsView = QGraphicsView(self.frame_16)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_9.addWidget(self.graphicsView)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 80))
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_15)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_7 = QLabel(self.frame_22)
        self.label_Likes_7.setObjectName(u"label_Likes_7")

        self.horizontalLayout_12.addWidget(self.label_Likes_7)

        self.label_Title = QLabel(self.frame_22)
        self.label_Title.setObjectName(u"label_Title")
        font3 = QFont()
        font3.setPointSize(21)
        font3.setBold(True)
        self.label_Title.setFont(font3)
        self.label_Title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_Title)

        self.label_Likes = QLabel(self.frame_22)
        self.label_Likes.setObjectName(u"label_Likes")

        self.horizontalLayout_12.addWidget(self.label_Likes, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_22)

        self.label_Artist = QLabel(self.frame_15)
        self.label_Artist.setObjectName(u"label_Artist")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_Artist.setFont(font4)
        self.label_Artist.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_Artist)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_29 = QFrame(self.page_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.graphicsView_4 = QGraphicsView(self.frame_29)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_16.addWidget(self.graphicsView_4)


        self.verticalLayout_12.addWidget(self.frame_29)

        self.frame_24 = QFrame(self.page_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 80))
        self.frame_24.setMaximumSize(QSize(16777215, 80))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_24)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_5 = QLabel(self.frame_27)
        self.label_Likes_5.setObjectName(u"label_Likes_5")

        self.horizontalLayout_15.addWidget(self.label_Likes_5)

        self.label_Title_4 = QLabel(self.frame_27)
        self.label_Title_4.setObjectName(u"label_Title_4")
        self.label_Title_4.setFont(font3)
        self.label_Title_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_Title_4, 0, Qt.AlignHCenter)

        self.label_Likes_4 = QLabel(self.frame_27)
        self.label_Likes_4.setObjectName(u"label_Likes_4")

        self.horizontalLayout_15.addWidget(self.label_Likes_4, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_27)

        self.label_Artist_4 = QLabel(self.frame_24)
        self.label_Artist_4.setObjectName(u"label_Artist_4")
        self.label_Artist_4.setFont(font4)
        self.label_Artist_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_Artist_4)


        self.verticalLayout_12.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_17 = QFrame(self.page_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_Image = QLabel(self.frame_17)
        self.label_Image.setObjectName(u"label_Image")

        self.horizontalLayout_10.addWidget(self.label_Image)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.page_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 80))
        self.frame_18.setMaximumSize(QSize(16777215, 80))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_18)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_6 = QLabel(self.frame_19)
        self.label_Likes_6.setObjectName(u"label_Likes_6")

        self.horizontalLayout_11.addWidget(self.label_Likes_6)

        self.label_Title_2 = QLabel(self.frame_19)
        self.label_Title_2.setObjectName(u"label_Title_2")
        self.label_Title_2.setFont(font3)
        self.label_Title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_Title_2, 0, Qt.AlignHCenter)

        self.label_Likes_2 = QLabel(self.frame_19)
        self.label_Likes_2.setObjectName(u"label_Likes_2")

        self.horizontalLayout_11.addWidget(self.label_Likes_2, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.label_Artist_2 = QLabel(self.frame_18)
        self.label_Artist_2.setObjectName(u"label_Artist_2")
        self.label_Artist_2.setFont(font4)
        self.label_Artist_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_Artist_2)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_5.addWidget(self.stackedWidget)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(50, 0))
        self.frame_12.setMaximumSize(QSize(50, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rightButton = QPushButton(self.frame_12)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setFont(font2)
        self.rightButton.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.rightButton)


        self.horizontalLayout_5.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 884, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.rightButton.clicked.connect(MainWindow.nextPage)
        self.leftButton.clicked.connect(MainWindow.prevPage)

        self.toolBox.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Name_2.setText(QCoreApplication.translate("MainWindow", u"Audi:ro", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \ucd94\ucc9c\ud558\uae30", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Page", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.tag1.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\uadfc", None))
        self.tag2.setText(QCoreApplication.translate("MainWindow", u"\ud1f4\uadfc", None))
        self.tag3.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\ub0a8", None))
        self.tag4.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\uc6b8", None))
        self.tag5.setText(QCoreApplication.translate("MainWindow", u"\uc6b4\ub3d9", None))
        self.tag6.setText(QCoreApplication.translate("MainWindow", u"\ud734\uc2dd", None))
        self.priorityBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\ucd94\ucc9c\uc21c", None))
        self.priorityBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\ucd5c\uc2e0\uc21c", None))
        self.priorityBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc154\ud50c", None))

        self.full_listBox.setText(QCoreApplication.translate("MainWindow", u"\ub354\ubcf4\uae30", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_Likes_7.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Likes.setText(QCoreApplication.translate("MainWindow", u"\u2764  251450", None))
        self.label_Artist.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_Likes_5.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_4.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_4.setText(QCoreApplication.translate("MainWindow", u"\u2764  221378", None))
        self.label_Artist_4.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_Image.setText("")
        self.label_Likes_6.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_2.setText(QCoreApplication.translate("MainWindow", u"Hype Boy", None))
        self.label_Likes_2.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_Artist_2.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u">", None))
    # retranslateUi

