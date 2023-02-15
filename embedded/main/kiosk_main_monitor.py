# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kiosk_main_monitor.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QStackedWidget,
    QTabWidget, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1338, 1995)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1100, 2000))
        self.centralwidget.setStyleSheet(u"background-color:#000000; color:#ffffff;")
        self.horizontalLayout_31 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_51 = QFrame(self.centralwidget)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(1080, 1920))
        self.frame_51.setMaximumSize(QSize(1080, 1920))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_51)
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.display1 = QFrame(self.frame_51)
        self.display1.setObjectName(u"display1")
        self.display1.setMinimumSize(QSize(0, 960))
        self.display1.setMaximumSize(QSize(16777215, 16777215))
        self.display1.setFrameShape(QFrame.StyledPanel)
        self.display1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.display1)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QFrame(self.display1)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(250, 900))
        self.menu_bar.setMaximumSize(QSize(16777215, 16777215))
        self.menu_bar.setFrameShape(QFrame.StyledPanel)
        self.menu_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.menu_bar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.menu_bar)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_38)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.frame_150 = QFrame(self.frame_38)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, -1, -1, 50)
        self.label_Name_4 = QLabel(self.frame_150)
        self.label_Name_4.setObjectName(u"label_Name_4")
        font = QFont()
        font.setPointSize(42)
        font.setBold(True)
        self.label_Name_4.setFont(font)
        self.label_Name_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_Name_4)


        self.verticalLayout_105.addWidget(self.frame_150)

        self.frame_151 = QFrame(self.frame_38)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_151)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.menu_toolBox = QToolBox(self.frame_151)
        self.menu_toolBox.setObjectName(u"menu_toolBox")
        self.menu_toolBox.setEnabled(True)
        self.menu_toolBox.setMinimumSize(QSize(0, 300))
        font1 = QFont()
        font1.setPointSize(16)
        self.menu_toolBox.setFont(font1)
        self.menu_toolBox.setFocusPolicy(Qt.NoFocus)
        self.menu_toolBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.menu_toolBox.setAcceptDrops(False)
        self.menu_toolBox.setLayoutDirection(Qt.LeftToRight)
        self.menu_toolBox.setAutoFillBackground(False)
        self.menu_toolBox.setStyleSheet(u"/*border:none;border-radius: 15px;\\n  color: #ffffff;\\n  background-color: #6522f2;*/\n"
"\n"
"QToolBox{\n"
"icon-size:30px;\n"
"}\n"
"QToolBox::tab{\n"
"border-radius:15px;\n"
"text-align:left;\n"
"font-size:23px;\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background: #6522F2;\n"
"}")
        self.menu_toolBox.setInputMethodHints(Qt.ImhNone)
        self.menu_toolBox.setFrameShadow(QFrame.Raised)
        self.menu_toolBox.setLineWidth(1)
        self.menu_toolBox.setMidLineWidth(0)
        self.menuPage1 = QWidget()
        self.menuPage1.setObjectName(u"menuPage1")
        self.menuPage1.setGeometry(QRect(0, 0, 244, 96))
        self.verticalLayout_26 = QVBoxLayout(self.menuPage1)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        icon = QIcon()
        icon.addFile(u"../resource/icons/empty.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_toolBox.addItem(self.menuPage1, icon, u"   \uba40\ucea0:\ub85c\uc758 \uc778\uae30\ucc28\ud2b8")
        self.menuPage2 = QWidget()
        self.menuPage2.setObjectName(u"menuPage2")
        self.menuPage2.setGeometry(QRect(0, 0, 244, 96))
        font2 = QFont()
        font2.setPointSize(9)
        self.menuPage2.setFont(font2)
        self.verticalLayout_107 = QVBoxLayout(self.menuPage2)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.frame_119 = QFrame(self.menuPage2)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMaximumSize(QSize(16777211, 16777215))
        self.frame_119.setFont(font2)
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_119)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_29 = QPushButton(self.frame_119)
        self.pushButton_29.setObjectName(u"pushButton_29")
        font3 = QFont()
        font3.setPointSize(15)
        self.pushButton_29.setFont(font3)
        self.pushButton_29.setStyleSheet(u"text-align:left;")
        self.pushButton_29.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.frame_119)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setFont(font3)
        self.pushButton_30.setStyleSheet(u"text-align:left;")

        self.verticalLayout_8.addWidget(self.pushButton_30)


        self.verticalLayout_107.addWidget(self.frame_119, 0, Qt.AlignTop)

        self.menu_toolBox.addItem(self.menuPage2, icon, u"   \uc74c\uc545 \uc120\ubb3c")
        self.menuPage3 = QWidget()
        self.menuPage3.setObjectName(u"menuPage3")
        self.menuPage3.setGeometry(QRect(0, 0, 244, 96))
        self.verticalLayout_4 = QVBoxLayout(self.menuPage3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_120 = QFrame(self.menuPage3)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_120)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_120)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font3)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"text-align:left;")

        self.verticalLayout_12.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_120)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"text-align:left;")

        self.verticalLayout_12.addWidget(self.pushButton_3, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_120, 0, Qt.AlignTop)

        self.menu_toolBox.addItem(self.menuPage3, icon, u"   \ud3b8\uc9c0\ud568")

        self.verticalLayout_106.addWidget(self.menu_toolBox)


        self.verticalLayout_105.addWidget(self.frame_151, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_38)

        self.frame_28 = QFrame(self.menu_bar)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_28)

        self.frame_12 = QFrame(self.menu_bar)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_18 = QPushButton(self.frame_12)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setPointSize(14)
        self.pushButton_18.setFont(font4)
        self.pushButton_18.setStyleSheet(u"padding: 3px 8px;\n"
"background: #6522F2;\n"
"border-radius: 25px;")

        self.horizontalLayout_25.addWidget(self.pushButton_18)


        self.verticalLayout_7.addWidget(self.frame_12, 0, Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.menu_bar, 0, Qt.AlignLeft|Qt.AlignTop)

        self.main = QFrame(self.display1)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(0, 0))
        self.main.setMaximumSize(QSize(16777215, 16777215))
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 40, 40)
        self.stackedPages = QStackedWidget(self.main)
        self.stackedPages.setObjectName(u"stackedPages")
        self.stackedPages.setMaximumSize(QSize(16777215, 16777215))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_3 = QVBoxLayout(self.page1)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 30, 0, 0)
        self.Tags = QFrame(self.frame_4)
        self.Tags.setObjectName(u"Tags")
        self.Tags.setMinimumSize(QSize(0, 0))
        self.Tags.setMaximumSize(QSize(16777215, 16777215))
        self.Tags.setFrameShape(QFrame.StyledPanel)
        self.Tags.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Tags)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tag1 = QPushButton(self.Tags)
        self.tag1.setObjectName(u"tag1")
        self.tag1.setMinimumSize(QSize(0, 40))
        self.tag1.setFont(font4)
        self.tag1.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag1)

        self.tag2 = QPushButton(self.Tags)
        self.tag2.setObjectName(u"tag2")
        self.tag2.setMinimumSize(QSize(0, 40))
        self.tag2.setFont(font4)
        self.tag2.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag2)

        self.tag3 = QPushButton(self.Tags)
        self.tag3.setObjectName(u"tag3")
        self.tag3.setMinimumSize(QSize(0, 40))
        self.tag3.setFont(font4)
        self.tag3.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag3)

        self.tag4 = QPushButton(self.Tags)
        self.tag4.setObjectName(u"tag4")
        self.tag4.setMinimumSize(QSize(0, 40))
        self.tag4.setFont(font4)
        self.tag4.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag4)

        self.tag5 = QPushButton(self.Tags)
        self.tag5.setObjectName(u"tag5")
        self.tag5.setMinimumSize(QSize(0, 40))
        self.tag5.setFont(font4)
        self.tag5.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag5)

        self.tag6 = QPushButton(self.Tags)
        self.tag6.setObjectName(u"tag6")
        self.tag6.setMinimumSize(QSize(0, 40))
        self.tag6.setFont(font4)
        self.tag6.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag6)


        self.verticalLayout.addWidget(self.Tags, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_7)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(30, 0, 0, 0)
        self.priorityBox = QComboBox(self.frame_7)
        self.priorityBox.addItem("")
        self.priorityBox.addItem("")
        self.priorityBox.addItem("")
        self.priorityBox.setObjectName(u"priorityBox")
        self.priorityBox.setMinimumSize(QSize(90, 50))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.priorityBox.setFont(font5)
        self.priorityBox.setStyleSheet(u"*{width: 66px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")
        self.priorityBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.priorityBox.setFrame(True)

        self.verticalLayout_73.addWidget(self.priorityBox, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_220 = QFrame(self.frame)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setMinimumSize(QSize(0, 0))
        self.frame_220.setMaximumSize(QSize(16777215, 16777215))
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_220)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.leftButton_19 = QPushButton(self.frame_220)
        self.leftButton_19.setObjectName(u"leftButton_19")
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.leftButton_19.setFont(font6)
        self.leftButton_19.setStyleSheet(u"")

        self.verticalLayout_155.addWidget(self.leftButton_19, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_220, 0, Qt.AlignLeft)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.scrollArea.setStyleSheet(u"QScrollBar:horizontal{\n"
"border:none;\n"
"background-color:rgb(59,59,90);\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"border-radius: 8px;\n"
"background-color:#6522F2;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 3072, 463))
        self.horizontalLayout_127 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.chart_img_Button1 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button1.setObjectName(u"chart_img_Button1")
        self.chart_img_Button1.setMinimumSize(QSize(300, 300))
        self.chart_img_Button1.setAutoFillBackground(False)
        self.chart_img_Button1.setStyleSheet(u"border-radius:150;")
        icon1 = QIcon()
        icon1.addFile(u"../resource/icons/ditto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chart_img_Button1.setIcon(icon1)
        self.chart_img_Button1.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button1)

        self.chart_img_Button2 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button2.setObjectName(u"chart_img_Button2")
        self.chart_img_Button2.setMinimumSize(QSize(300, 300))
        self.chart_img_Button2.setAutoFillBackground(False)
        self.chart_img_Button2.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button2.setIcon(icon1)
        self.chart_img_Button2.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button2)

        self.chart_img_Button3 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button3.setObjectName(u"chart_img_Button3")
        self.chart_img_Button3.setMinimumSize(QSize(300, 300))
        self.chart_img_Button3.setAutoFillBackground(False)
        self.chart_img_Button3.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button3.setIcon(icon1)
        self.chart_img_Button3.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button3)

        self.chart_img_Button4 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button4.setObjectName(u"chart_img_Button4")
        self.chart_img_Button4.setMinimumSize(QSize(300, 300))
        self.chart_img_Button4.setAutoFillBackground(False)
        self.chart_img_Button4.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button4.setIcon(icon1)
        self.chart_img_Button4.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button4)

        self.chart_img_Button5 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button5.setObjectName(u"chart_img_Button5")
        self.chart_img_Button5.setMinimumSize(QSize(300, 300))
        self.chart_img_Button5.setAutoFillBackground(False)
        self.chart_img_Button5.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button5.setIcon(icon1)
        self.chart_img_Button5.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button5)

        self.chart_img_Button6 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button6.setObjectName(u"chart_img_Button6")
        self.chart_img_Button6.setMinimumSize(QSize(300, 300))
        self.chart_img_Button6.setAutoFillBackground(False)
        self.chart_img_Button6.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button6.setIcon(icon1)
        self.chart_img_Button6.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button6)

        self.chart_img_Button7 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button7.setObjectName(u"chart_img_Button7")
        self.chart_img_Button7.setMinimumSize(QSize(300, 300))
        self.chart_img_Button7.setAutoFillBackground(False)
        self.chart_img_Button7.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button7.setIcon(icon1)
        self.chart_img_Button7.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button7)

        self.chart_img_Button8 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button8.setObjectName(u"chart_img_Button8")
        self.chart_img_Button8.setMinimumSize(QSize(300, 300))
        self.chart_img_Button8.setAutoFillBackground(False)
        self.chart_img_Button8.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button8.setIcon(icon1)
        self.chart_img_Button8.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button8)

        self.chart_img_Button9 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button9.setObjectName(u"chart_img_Button9")
        self.chart_img_Button9.setMinimumSize(QSize(300, 300))
        self.chart_img_Button9.setAutoFillBackground(False)
        self.chart_img_Button9.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button9.setIcon(icon1)
        self.chart_img_Button9.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button9)

        self.chart_img_Button10 = QPushButton(self.scrollAreaWidgetContents)
        self.chart_img_Button10.setObjectName(u"chart_img_Button10")
        self.chart_img_Button10.setMinimumSize(QSize(300, 300))
        self.chart_img_Button10.setAutoFillBackground(False)
        self.chart_img_Button10.setStyleSheet(u"border-radius:150;")
        self.chart_img_Button10.setIcon(icon1)
        self.chart_img_Button10.setIconSize(QSize(300, 300))

        self.horizontalLayout_127.addWidget(self.chart_img_Button10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.frame_230 = QFrame(self.frame)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setMinimumSize(QSize(0, 0))
        self.frame_230.setMaximumSize(QSize(16777215, 16777215))
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_230)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.rightButton_19 = QPushButton(self.frame_230)
        self.rightButton_19.setObjectName(u"rightButton_19")
        self.rightButton_19.setFont(font6)
        self.rightButton_19.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.rightButton_19, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.frame_230, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(800, 0))
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_132 = QFrame(self.frame_2)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(50, 0))
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_132)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")

        self.horizontalLayout_5.addWidget(self.frame_132)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.frame_222 = QFrame(self.frame_15)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setFrameShape(QFrame.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_222)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_116 = QFrame(self.frame_222)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(0, 0))
        self.frame_116.setMaximumSize(QSize(100, 40))
        self.frame_116.setStyleSheet(u"width:30px; height:20px;border: 1px solid #6522F2;\n"
"border-radius: 15px;")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_131.setSpacing(5)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(11, 11, 11, 11)
        self.label_100 = QLabel(self.frame_116)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(25, 35))
        self.label_100.setStyleSheet(u"border:none;")
        self.label_100.setPixmap(QPixmap(u"../resource/icons/mail 1.png"))
        self.label_100.setScaledContents(True)
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_131.addWidget(self.label_100)

        self.label_101 = QLabel(self.frame_116)
        self.label_101.setObjectName(u"label_101")
        font7 = QFont()
        font7.setPointSize(12)
        self.label_101.setFont(font7)
        self.label_101.setStyleSheet(u"border:none;")

        self.horizontalLayout_131.addWidget(self.label_101, 0, Qt.AlignRight)


        self.horizontalLayout_75.addWidget(self.frame_116, 0, Qt.AlignVCenter)

        self.label_Title_5 = QLabel(self.frame_222)
        self.label_Title_5.setObjectName(u"label_Title_5")
        font8 = QFont()
        font8.setPointSize(30)
        font8.setBold(True)
        self.label_Title_5.setFont(font8)
        self.label_Title_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_Title_5)

        self.frame_117 = QFrame(self.frame_222)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMinimumSize(QSize(0, 0))
        self.frame_117.setMaximumSize(QSize(100, 40))
        self.frame_117.setStyleSheet(u"width:30px; height:20px;border: 1px solid #6522F2;\n"
"border-radius: 15px;")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_132.setSpacing(11)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(11, 11, 11, 11)
        self.label_102 = QLabel(self.frame_117)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(20, 30))
        self.label_102.setStyleSheet(u"border:none;")
        self.label_102.setPixmap(QPixmap(u"../resource/icons/heart.png"))
        self.label_102.setScaledContents(True)
        self.label_102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_132.addWidget(self.label_102, 0, Qt.AlignLeft)

        self.song_liked = QLabel(self.frame_117)
        self.song_liked.setObjectName(u"song_liked")
        self.song_liked.setFont(font7)
        self.song_liked.setStyleSheet(u"border:none;")

        self.horizontalLayout_132.addWidget(self.song_liked, 0, Qt.AlignRight)


        self.horizontalLayout_75.addWidget(self.frame_117)


        self.verticalLayout_2.addWidget(self.frame_222)

        self.label_Artist_3 = QLabel(self.frame_15)
        self.label_Artist_3.setObjectName(u"label_Artist_3")
        font9 = QFont()
        font9.setPointSize(15)
        font9.setBold(True)
        self.label_Artist_3.setFont(font9)
        self.label_Artist_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_Artist_3, 0, Qt.AlignBottom)

        self.frame_118 = QFrame(self.frame_15)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_184 = QLabel(self.frame_118)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setFont(font7)

        self.horizontalLayout_133.addWidget(self.label_184)

        self.label_185 = QLabel(self.frame_118)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setFont(font7)

        self.horizontalLayout_133.addWidget(self.label_185, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_118, 0, Qt.AlignBottom)

        self.frame_223 = QFrame(self.frame_15)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setFrameShape(QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_223)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_223)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setStyleSheet(u"*{\n"
"  border-radius: 15px;\n"
"  background-color: #6522f2;}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_11)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(15, 10, 15, 10)
        self.chart_music_slider = QSlider(self.frame_11)
        self.chart_music_slider.setObjectName(u"chart_music_slider")
        self.chart_music_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: -5px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.chart_music_slider.setValue(25)
        self.chart_music_slider.setSliderPosition(25)
        self.chart_music_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_68.addWidget(self.chart_music_slider)


        self.horizontalLayout_76.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_223)


        self.horizontalLayout_5.addWidget(self.frame_15)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(50, 204))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.frame_139 = QFrame(self.frame_5)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setMinimumSize(QSize(50, 0))
        self.frame_139.setMaximumSize(QSize(16777215, 16777215))
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_139)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(9, 0, 9, 0)
        self.volume_frame_chart = QFrame(self.frame_139)
        self.volume_frame_chart.setObjectName(u"volume_frame_chart")
        self.volume_frame_chart.setEnabled(True)
        self.volume_frame_chart.setMinimumSize(QSize(0, 150))
        self.volume_frame_chart.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.volume_frame_chart.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.volume_frame_chart)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(9, 9, 9, 9)
        self.verticalSlider_31 = QSlider(self.volume_frame_chart)
        self.verticalSlider_31.setObjectName(u"verticalSlider_31")
        self.verticalSlider_31.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin:2  5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: 0 -5px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.verticalSlider_31.setValue(40)
        self.verticalSlider_31.setOrientation(Qt.Vertical)

        self.horizontalLayout_144.addWidget(self.verticalSlider_31)


        self.verticalLayout_81.addWidget(self.volume_frame_chart)


        self.verticalLayout_5.addWidget(self.frame_139)

        self.pushButton_35 = QPushButton(self.frame_5)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"}  ")
        icon2 = QIcon()
        icon2.addFile(u"../resource/icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_35.setIcon(icon2)
        self.pushButton_35.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.pushButton_35, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedPages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_41 = QVBoxLayout(self.page2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 30, 0, 20)
        self.frame_237 = QFrame(self.frame_3)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMaximumSize(QSize(16777215, 16777215))
        self.frame_237.setFont(font2)
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_237)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 50, 0)
        self.pushButton_23 = QPushButton(self.frame_237)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(0, 0))
        self.pushButton_23.setFont(font4)
        self.pushButton_23.setStyleSheet(u"width:100px;\n"
"height:50px;\n"
"padding: 3px 15px;\n"
"background: #6522F2;\n"
"border-radius: 25px;")

        self.horizontalLayout_79.addWidget(self.pushButton_23, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.frame_237)

        self.frame_136 = QFrame(self.frame_3)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.frame_227 = QFrame(self.frame_136)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setMinimumSize(QSize(30, 0))
        self.frame_227.setMaximumSize(QSize(30, 16777215))
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_227)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.leftButton_11 = QPushButton(self.frame_227)
        self.leftButton_11.setObjectName(u"leftButton_11")
        self.leftButton_11.setFont(font6)
        self.leftButton_11.setStyleSheet(u"")

        self.verticalLayout_78.addWidget(self.leftButton_11)


        self.horizontalLayout_66.addWidget(self.frame_227)

        self.stackedWidget_3 = QStackedWidget(self.frame_136)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 0))
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_40 = QHBoxLayout(self.page_10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(30)
        self.gridLayout_11.setVerticalSpacing(80)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.music_post4 = QLabel(self.page_10)
        self.music_post4.setObjectName(u"music_post4")
        self.music_post4.setMinimumSize(QSize(0, 0))
        self.music_post4.setMaximumSize(QSize(16777215, 16777215))
        self.music_post4.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.music_post4.setPixmap(QPixmap(u"../resource/post4.jpg"))
        self.music_post4.setScaledContents(True)
        self.music_post4.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.music_post4, 1, 0, 1, 1)

        self.music_post1 = QLabel(self.page_10)
        self.music_post1.setObjectName(u"music_post1")
        self.music_post1.setMinimumSize(QSize(0, 0))
        self.music_post1.setMaximumSize(QSize(16777215, 16777215))
        self.music_post1.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.music_post1.setPixmap(QPixmap(u"../resource/post1.jpg"))
        self.music_post1.setScaledContents(True)
        self.music_post1.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.music_post1, 0, 0, 1, 1)

        self.music_post3 = QLabel(self.page_10)
        self.music_post3.setObjectName(u"music_post3")
        self.music_post3.setMinimumSize(QSize(0, 0))
        self.music_post3.setMaximumSize(QSize(16777215, 16777215))
        self.music_post3.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.music_post3.setPixmap(QPixmap(u"../resource/post3.jpg"))
        self.music_post3.setScaledContents(True)
        self.music_post3.setAlignment(Qt.AlignCenter)
        self.music_post3.setMargin(0)
        self.music_post3.setIndent(-1)

        self.gridLayout_11.addWidget(self.music_post3, 0, 2, 1, 1)

        self.music_post6 = QLabel(self.page_10)
        self.music_post6.setObjectName(u"music_post6")
        self.music_post6.setMinimumSize(QSize(0, 0))
        self.music_post6.setMaximumSize(QSize(16777215, 16777215))
        self.music_post6.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.music_post6.setPixmap(QPixmap(u"../resource/post6.jpg"))
        self.music_post6.setScaledContents(True)
        self.music_post6.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.music_post6, 1, 2, 1, 1)

        self.music_post2 = QLabel(self.page_10)
        self.music_post2.setObjectName(u"music_post2")
        self.music_post2.setMinimumSize(QSize(0, 0))
        self.music_post2.setMaximumSize(QSize(16777215, 16777215))
        self.music_post2.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.music_post2.setPixmap(QPixmap(u"../resource/post2.jpg"))
        self.music_post2.setScaledContents(True)
        self.music_post2.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.music_post2, 0, 1, 1, 1)

        self.music_post5 = QLabel(self.page_10)
        self.music_post5.setObjectName(u"music_post5")
        self.music_post5.setMinimumSize(QSize(0, 0))
        self.music_post5.setMaximumSize(QSize(16777215, 16777215))
        self.music_post5.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.music_post5.setPixmap(QPixmap(u"../resource/post5.jpg"))
        self.music_post5.setScaledContents(True)
        self.music_post5.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.music_post5, 1, 1, 1, 1)


        self.horizontalLayout_40.addLayout(self.gridLayout_11)

        self.stackedWidget_3.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_41 = QHBoxLayout(self.page_11)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(30)
        self.gridLayout_21.setVerticalSpacing(50)
        self.gridLayout_21.setContentsMargins(0, 10, 0, 10)
        self.label_129 = QLabel(self.page_11)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMaximumSize(QSize(450, 450))
        self.label_129.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_129, 1, 1, 1, 1)

        self.label_130 = QLabel(self.page_11)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMaximumSize(QSize(450, 450))
        self.label_130.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_130, 0, 1, 1, 1)

        self.label_131 = QLabel(self.page_11)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMaximumSize(QSize(450, 450))
        self.label_131.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_131.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_131, 1, 0, 1, 1)

        self.label_132 = QLabel(self.page_11)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMaximumSize(QSize(450, 450))
        self.label_132.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_132.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_132, 0, 0, 1, 1)

        self.label_134 = QLabel(self.page_11)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMaximumSize(QSize(450, 450))
        self.label_134.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_134.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_134, 0, 2, 1, 1)

        self.label_135 = QLabel(self.page_11)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMaximumSize(QSize(450, 450))
        self.label_135.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_135.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_135, 1, 2, 1, 1)


        self.horizontalLayout_41.addLayout(self.gridLayout_21)

        self.stackedWidget_3.addWidget(self.page_11)

        self.horizontalLayout_66.addWidget(self.stackedWidget_3)

        self.frame_10 = QFrame(self.frame_136)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(30, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_10)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.leftButton_13 = QPushButton(self.frame_10)
        self.leftButton_13.setObjectName(u"leftButton_13")
        self.leftButton_13.setFont(font6)
        self.leftButton_13.setStyleSheet(u"")

        self.verticalLayout_77.addWidget(self.leftButton_13)


        self.horizontalLayout_66.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.frame_136)

        self.frame_133 = QFrame(self.frame_3)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(800, 0))
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_133)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_135 = QFrame(self.frame_133)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(50, 0))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_135)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")

        self.horizontalLayout.addWidget(self.frame_135)

        self.frame_137 = QFrame(self.frame_133)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_137)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_247 = QFrame(self.frame_137)
        self.frame_247.setObjectName(u"frame_247")
        self.frame_247.setFrameShape(QFrame.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_247)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_285 = QFrame(self.frame_247)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setFrameShape(QFrame.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_285)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.frame_285)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMinimumSize(QSize(100, 0))
        self.frame_121.setMaximumSize(QSize(100, 40))
        self.frame_121.setStyleSheet(u"width:30px; height:20px;border: 1px solid #6522F2;\n"
"border-radius: 15px;")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_134.setSpacing(5)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(11, 11, 11, 11)
        self.label_104 = QLabel(self.frame_121)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMaximumSize(QSize(25, 35))
        self.label_104.setStyleSheet(u"border:none;")
        self.label_104.setPixmap(QPixmap(u"../resource/icons/mail 1.png"))
        self.label_104.setScaledContents(True)
        self.label_104.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_134.addWidget(self.label_104)

        self.song_gift_cnt = QLabel(self.frame_121)
        self.song_gift_cnt.setObjectName(u"song_gift_cnt")
        self.song_gift_cnt.setFont(font7)
        self.song_gift_cnt.setStyleSheet(u"border:none;")

        self.horizontalLayout_134.addWidget(self.song_gift_cnt, 0, Qt.AlignRight)


        self.horizontalLayout_128.addWidget(self.frame_121, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.song_title = QLabel(self.frame_285)
        self.song_title.setObjectName(u"song_title")
        self.song_title.setFont(font8)
        self.song_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_128.addWidget(self.song_title)

        self.frame_122 = QFrame(self.frame_285)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 0))
        self.frame_122.setMaximumSize(QSize(100, 40))
        self.frame_122.setStyleSheet(u"width:30px; height:20px;border: 1px solid #6522F2;\n"
"border-radius: 15px;")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_135.setSpacing(11)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(11, 11, 11, 11)
        self.label_106 = QLabel(self.frame_122)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(20, 30))
        self.label_106.setStyleSheet(u"border:none;")
        self.label_106.setPixmap(QPixmap(u"../resource/icons/heart.png"))
        self.label_106.setScaledContents(True)
        self.label_106.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_135.addWidget(self.label_106, 0, Qt.AlignLeft)

        self.song_liked_cnt = QLabel(self.frame_122)
        self.song_liked_cnt.setObjectName(u"song_liked_cnt")
        self.song_liked_cnt.setFont(font7)
        self.song_liked_cnt.setStyleSheet(u"border:none;")

        self.horizontalLayout_135.addWidget(self.song_liked_cnt, 0, Qt.AlignRight)


        self.horizontalLayout_128.addWidget(self.frame_122, 0, Qt.AlignRight)


        self.horizontalLayout_91.addWidget(self.frame_285)


        self.verticalLayout_97.addWidget(self.frame_247)

        self.song_singer = QLabel(self.frame_137)
        self.song_singer.setObjectName(u"song_singer")
        self.song_singer.setFont(font9)
        self.song_singer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.song_singer, 0, Qt.AlignBottom)

        self.frame_123 = QFrame(self.frame_137)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.song_play_time = QLabel(self.frame_123)
        self.song_play_time.setObjectName(u"song_play_time")
        self.song_play_time.setFont(font7)

        self.horizontalLayout_136.addWidget(self.song_play_time)

        self.song_full_time = QLabel(self.frame_123)
        self.song_full_time.setObjectName(u"song_full_time")
        self.song_full_time.setFont(font7)

        self.horizontalLayout_136.addWidget(self.song_full_time, 0, Qt.AlignRight)


        self.verticalLayout_97.addWidget(self.frame_123, 0, Qt.AlignBottom)

        self.frame_124 = QFrame(self.frame_137)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMaximumSize(QSize(16777215, 30))
        self.frame_124.setStyleSheet(u"*{\n"
"  border-radius: 15px;\n"
"  background-color: #6522f2;}")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_124)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(15, 10, 15, 10)
        self.song_music_slider = QSlider(self.frame_124)
        self.song_music_slider.setObjectName(u"song_music_slider")
        self.song_music_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: -5px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.song_music_slider.setValue(25)
        self.song_music_slider.setSliderPosition(25)
        self.song_music_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_69.addWidget(self.song_music_slider, 0, Qt.AlignVCenter)


        self.verticalLayout_97.addWidget(self.frame_124, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_137)

        self.frame_134 = QFrame(self.frame_133)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMinimumSize(QSize(50, 196))
        self.frame_134.setMaximumSize(QSize(16777215, 16777215))
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_134)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(9, 0, 9, 0)
        self.volume_frame_song = QFrame(self.frame_134)
        self.volume_frame_song.setObjectName(u"volume_frame_song")
        self.volume_frame_song.setEnabled(True)
        self.volume_frame_song.setMinimumSize(QSize(0, 150))
        self.volume_frame_song.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.volume_frame_song.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_song.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.volume_frame_song)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(9, 9, 9, 9)
        self.verticalSlider_27 = QSlider(self.volume_frame_song)
        self.verticalSlider_27.setObjectName(u"verticalSlider_27")
        self.verticalSlider_27.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin:2  5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: 0 -5px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.verticalSlider_27.setValue(40)
        self.verticalSlider_27.setOrientation(Qt.Vertical)

        self.horizontalLayout_137.addWidget(self.verticalSlider_27)


        self.verticalLayout_75.addWidget(self.volume_frame_song)

        self.pushButton_47 = QPushButton(self.frame_134)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setIcon(icon2)
        self.pushButton_47.setIconSize(QSize(30, 30))

        self.verticalLayout_75.addWidget(self.pushButton_47, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_134)


        self.verticalLayout_10.addWidget(self.frame_133)


        self.verticalLayout_41.addWidget(self.frame_3)

        self.stackedPages.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.horizontalLayout_13 = QHBoxLayout(self.page3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setSpacing(40)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(300, 60))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_17)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_133 = QLabel(self.frame_17)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(0, 0))
        self.label_133.setMaximumSize(QSize(16777215, 16777215))
        self.label_133.setFont(font6)
        self.label_133.setStyleSheet(u"*{\n"
"  padding: 0px 20px 0 20px;\n"
"  border-radius: 20px;\n"
"  background-color: #6522f2;\n"
"color: #FFFFFF;\n"
"}")
        self.label_133.setFrameShape(QFrame.Box)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_133, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_17, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_79 = QFrame(self.frame_9)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 500))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_46.setSpacing(7)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.frame_157 = QFrame(self.frame_79)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(50, 0))
        self.frame_157.setMaximumSize(QSize(16777215, 16777215))
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_157)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.leftButton_14 = QPushButton(self.frame_157)
        self.leftButton_14.setObjectName(u"leftButton_14")
        self.leftButton_14.setFont(font6)
        self.leftButton_14.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.leftButton_14)


        self.horizontalLayout_46.addWidget(self.frame_157, 0, Qt.AlignLeft)

        self.post_scroll_area = QScrollArea(self.frame_79)
        self.post_scroll_area.setObjectName(u"post_scroll_area")
        self.post_scroll_area.setMinimumSize(QSize(600, 600))
        self.post_scroll_area.setStyleSheet(u"QScrollBar:horizontal{\n"
"border:none;\n"
"background-color:rgb(59,59,90);\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"border-radius: 8px;\n"
"background-color:#6522F2;\n"
"}\n"
"")
        self.post_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.post_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.post_scroll_area.setWidgetResizable(True)
        self.post_scroll_area.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1410, 581))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setSpacing(30)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.post1 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post1.setObjectName(u"post1")
        self.post1.setMinimumSize(QSize(250, 250))
        self.post1.setStyleSheet(u"background-color:white;")
        self.post1.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post1, 1, 0, 1, 1)

        self.post6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post6.setObjectName(u"post6")
        self.post6.setMinimumSize(QSize(250, 250))
        self.post6.setStyleSheet(u"background-color:white;")
        self.post6.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post6, 4, 0, 1, 1)

        self.post5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post5.setObjectName(u"post5")
        self.post5.setMinimumSize(QSize(250, 250))
        self.post5.setStyleSheet(u"background-color:white;")
        self.post5.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post5, 1, 5, 1, 1)

        self.post7 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post7.setObjectName(u"post7")
        self.post7.setMinimumSize(QSize(250, 250))
        self.post7.setStyleSheet(u"background-color:white;")
        self.post7.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post7, 4, 1, 1, 1)

        self.post4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post4.setObjectName(u"post4")
        self.post4.setMinimumSize(QSize(250, 250))
        self.post4.setStyleSheet(u"background-color:white;")
        self.post4.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post4, 1, 3, 1, 1)

        self.post10 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post10.setObjectName(u"post10")
        self.post10.setMinimumSize(QSize(250, 250))
        self.post10.setStyleSheet(u"background-color:white;")
        self.post10.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post10, 4, 5, 1, 1)

        self.post9 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post9.setObjectName(u"post9")
        self.post9.setMinimumSize(QSize(250, 250))
        self.post9.setStyleSheet(u"background-color:white;")
        self.post9.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post9, 4, 3, 1, 1)

        self.post2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post2.setObjectName(u"post2")
        self.post2.setMinimumSize(QSize(250, 250))
        self.post2.setStyleSheet(u"background-color:white;")
        self.post2.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post2, 1, 1, 1, 1)

        self.post3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post3.setObjectName(u"post3")
        self.post3.setMinimumSize(QSize(250, 250))
        self.post3.setStyleSheet(u"background-color:white;")
        self.post3.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post3, 1, 2, 1, 1)

        self.post8 = QPushButton(self.scrollAreaWidgetContents_2)
        self.post8.setObjectName(u"post8")
        self.post8.setMinimumSize(QSize(250, 250))
        self.post8.setStyleSheet(u"background-color:white;")
        self.post8.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.post8, 4, 2, 1, 1)

        self.post_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_46.addWidget(self.post_scroll_area)

        self.frame_160 = QFrame(self.frame_79)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(50, 0))
        self.frame_160.setMaximumSize(QSize(16777215, 16777215))
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_160)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.rightButton_14 = QPushButton(self.frame_160)
        self.rightButton_14.setObjectName(u"rightButton_14")
        self.rightButton_14.setFont(font6)
        self.rightButton_14.setStyleSheet(u"")

        self.verticalLayout_114.addWidget(self.rightButton_14)


        self.horizontalLayout_46.addWidget(self.frame_160, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_79)

        self.frame_27 = QFrame(self.frame_9)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_27)


        self.horizontalLayout_13.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.stackedPages.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.horizontalLayout_62 = QHBoxLayout(self.page4)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_13 = QFrame(self.page4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.frame_20)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(80, 0))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_69)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")

        self.horizontalLayout_15.addWidget(self.frame_69, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_235 = QFrame(self.frame_20)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setMaximumSize(QSize(16777215, 16777215))
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_235)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.emoji_button2 = QPushButton(self.frame_235)
        self.emoji_button2.setObjectName(u"emoji_button2")
        self.emoji_button2.setStyleSheet(u"background: rgba(101, 34, 242, 0.51); border:10px solid black;")
        icon3 = QIcon()
        icon3.addFile(u"../resource/sad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emoji_button2.setIcon(icon3)
        self.emoji_button2.setIconSize(QSize(200, 100))

        self.gridLayout_3.addWidget(self.emoji_button2, 0, 3, 1, 1)

        self.count_emoji1 = QLabel(self.frame_235)
        self.count_emoji1.setObjectName(u"count_emoji1")
        self.count_emoji1.setFont(font4)
        self.count_emoji1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.count_emoji1, 1, 2, 1, 1)

        self.count_emoji4 = QLabel(self.frame_235)
        self.count_emoji4.setObjectName(u"count_emoji4")
        self.count_emoji4.setFont(font4)
        self.count_emoji4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.count_emoji4, 1, 5, 1, 1)

        self.count_emoji2 = QLabel(self.frame_235)
        self.count_emoji2.setObjectName(u"count_emoji2")
        self.count_emoji2.setFont(font4)
        self.count_emoji2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.count_emoji2, 1, 3, 1, 1)

        self.count_emoji3 = QLabel(self.frame_235)
        self.count_emoji3.setObjectName(u"count_emoji3")
        self.count_emoji3.setFont(font4)
        self.count_emoji3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.count_emoji3, 1, 4, 1, 1)

        self.emoji_button4 = QPushButton(self.frame_235)
        self.emoji_button4.setObjectName(u"emoji_button4")
        icon4 = QIcon()
        icon4.addFile(u"../resource/laugh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emoji_button4.setIcon(icon4)
        self.emoji_button4.setIconSize(QSize(200, 100))

        self.gridLayout_3.addWidget(self.emoji_button4, 0, 5, 1, 1)

        self.emoji_button3 = QPushButton(self.frame_235)
        self.emoji_button3.setObjectName(u"emoji_button3")
        self.emoji_button3.setStyleSheet(u"background: rgba(101, 34, 242, 0.51); border:10px solid black;")
        icon5 = QIcon()
        icon5.addFile(u"../resource/surprise.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emoji_button3.setIcon(icon5)
        self.emoji_button3.setIconSize(QSize(200, 100))

        self.gridLayout_3.addWidget(self.emoji_button3, 0, 4, 1, 1)

        self.emoji_button1 = QPushButton(self.frame_235)
        self.emoji_button1.setObjectName(u"emoji_button1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emoji_button1.sizePolicy().hasHeightForWidth())
        self.emoji_button1.setSizePolicy(sizePolicy)
        self.emoji_button1.setStyleSheet(u"background: rgba(101, 34, 242, 0.51); border:10px solid black;")
        icon6 = QIcon()
        icon6.addFile(u"../resource/love.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emoji_button1.setIcon(icon6)
        self.emoji_button1.setIconSize(QSize(200, 100))

        self.gridLayout_3.addWidget(self.emoji_button1, 0, 2, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_235)

        self.frame_67 = QFrame(self.frame_20)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 0))
        self.frame_67.setStyleSheet(u"padding: 3px 8px;\n"
"background: #6522F2;\n"
"border-radius: 25px;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_67)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_65 = QPushButton(self.frame_67)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMinimumSize(QSize(100, 0))
        self.pushButton_65.setFont(font3)
        self.pushButton_65.setStyleSheet(u"background-color:#6522f2; border-radius:15px;")

        self.verticalLayout_27.addWidget(self.pushButton_65)


        self.horizontalLayout_15.addWidget(self.frame_67, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_25.addWidget(self.frame_20, 0, Qt.AlignTop)

        self.frame_25 = QFrame(self.frame_13)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(500, 500))
        self.frame_25.setBaseSize(QSize(0, 0))
        self.frame_25.setStyleSheet(u"background-color:#D9D9D9;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gift_detail_img = QLabel(self.frame_25)
        self.gift_detail_img.setObjectName(u"gift_detail_img")
        font10 = QFont()
        font10.setPointSize(28)
        font10.setBold(True)
        self.gift_detail_img.setFont(font10)
        self.gift_detail_img.setStyleSheet(u"color: red;")
        self.gift_detail_img.setScaledContents(True)
        self.gift_detail_img.setAlignment(Qt.AlignCenter)
        self.gift_detail_img.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.gift_detail_img, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_25, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_29 = QFrame(self.frame_13)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_37 = QFrame(self.frame_29)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(50, 0))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.pushButton_98 = QPushButton(self.frame_37)
        self.pushButton_98.setObjectName(u"pushButton_98")
        self.pushButton_98.setGeometry(QRect(11, 224, 41, 41))
        icon7 = QIcon()
        icon7.addFile(u"../resource/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_98.setIcon(icon7)
        self.pushButton_98.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.frame_37)

        self.frame_48 = QFrame(self.frame_29)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_48)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_194 = QFrame(self.frame_48)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_194)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.gift_detail_song = QLabel(self.frame_194)
        self.gift_detail_song.setObjectName(u"gift_detail_song")
        self.gift_detail_song.setFont(font8)
        self.gift_detail_song.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.gift_detail_song, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.frame_194)

        self.frame_54 = QFrame(self.frame_48)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 11, -1, -1)
        self.gift_detail_singer = QLabel(self.frame_54)
        self.gift_detail_singer.setObjectName(u"gift_detail_singer")
        self.gift_detail_singer.setMaximumSize(QSize(16777215, 16777215))
        self.gift_detail_singer.setFont(font9)
        self.gift_detail_singer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.gift_detail_singer, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.frame_54)

        self.frame_115 = QFrame(self.frame_48)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.label_158 = QLabel(self.frame_115)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setFont(font7)
        self.label_158.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_130.addWidget(self.label_158, 0, Qt.AlignLeft)

        self.label_159 = QLabel(self.frame_115)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setFont(font7)
        self.label_159.setStyleSheet(u"*{color:#ffffff;}")
        self.label_159.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_130.addWidget(self.label_159, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_115, 0, Qt.AlignBottom)

        self.frame_126 = QFrame(self.frame_48)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMaximumSize(QSize(16777215, 30))
        self.frame_126.setStyleSheet(u"*{\n"
"  border-radius: 15px;\n"
"  background-color: #6522f2;}")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_126)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(15, 10, 15, 10)
        self.manito_music_slider = QSlider(self.frame_126)
        self.manito_music_slider.setObjectName(u"manito_music_slider")
        self.manito_music_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: -5px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.manito_music_slider.setValue(25)
        self.manito_music_slider.setSliderPosition(25)
        self.manito_music_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_70.addWidget(self.manito_music_slider, 0, Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.frame_126, 0, Qt.AlignBottom)


        self.horizontalLayout_10.addWidget(self.frame_48, 0, Qt.AlignBottom)

        self.frame_198 = QFrame(self.frame_29)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setMinimumSize(QSize(50, 216))
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_198)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(-1, 11, -1, -1)
        self.volume_frame_manito = QFrame(self.frame_198)
        self.volume_frame_manito.setObjectName(u"volume_frame_manito")
        self.volume_frame_manito.setEnabled(True)
        self.volume_frame_manito.setMinimumSize(QSize(0, 150))
        self.volume_frame_manito.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.volume_frame_manito.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_manito.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.volume_frame_manito)
        self.horizontalLayout_140.setSpacing(7)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(10, -1, 10, 11)
        self.verticalSlider_29 = QSlider(self.volume_frame_manito)
        self.verticalSlider_29.setObjectName(u"verticalSlider_29")
        self.verticalSlider_29.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin:2  5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: 0 -5px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.verticalSlider_29.setValue(40)
        self.verticalSlider_29.setOrientation(Qt.Vertical)

        self.horizontalLayout_140.addWidget(self.verticalSlider_29)


        self.verticalLayout_140.addWidget(self.volume_frame_manito)

        self.pushButton_2 = QPushButton(self.frame_198)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.verticalLayout_140.addWidget(self.pushButton_2, 0, Qt.AlignBottom)


        self.horizontalLayout_10.addWidget(self.frame_198, 0, Qt.AlignBottom)


        self.verticalLayout_25.addWidget(self.frame_29)


        self.horizontalLayout_62.addWidget(self.frame_13)

        self.stackedPages.addWidget(self.page4)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_87 = QVBoxLayout(self.page_8)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_108 = QFrame(self.page_8)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_108)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.frame_158 = QFrame(self.frame_108)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(0, 150))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_158)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(-1, -1, -1, 0)
        self.frame_161 = QFrame(self.frame_158)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(120, 60))
        self.frame_161.setStyleSheet(u"")
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_161)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.frame_161)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(140, 60))
        font11 = QFont()
        font11.setPointSize(16)
        font11.setBold(False)
        self.pushButton_19.setFont(font11)
        self.pushButton_19.setStyleSheet(u"*{border-radius: 25px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}")

        self.verticalLayout_94.addWidget(self.pushButton_19, 0, Qt.AlignRight)


        self.verticalLayout_93.addWidget(self.frame_161, 0, Qt.AlignBottom)


        self.verticalLayout_95.addWidget(self.frame_158, 0, Qt.AlignBottom)

        self.frame_109 = QFrame(self.frame_108)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 0))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_109)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(20, -1, 20, -1)
        self.tabWidget_2 = QTabWidget(self.frame_109)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        font12 = QFont()
        font12.setPointSize(17)
        self.tabWidget_2.setFont(font12)
        self.tabWidget_2.setStyleSheet(u"QTabWidget{\n"
"border:none;\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #6522F2;\n"
"    position: absolute;\n"
"top:1em;\n"
"}\n"
"QTabBar::tab{\n"
"background-color:black;\n"
"}")
        self.tabWidget_2.setElideMode(Qt.ElideNone)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_91 = QVBoxLayout(self.tab_4)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_113 = QFrame(self.tab_4)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_113)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_179 = QFrame(self.frame_113)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setMinimumSize(QSize(0, 50))
        self.frame_179.setStyleSheet(u"background-color:white;")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_179)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(10, 0, 0, 0)
        self.lineEdit_gift_song = QLineEdit(self.frame_179)
        self.lineEdit_gift_song.setObjectName(u"lineEdit_gift_song")
        self.lineEdit_gift_song.setMinimumSize(QSize(0, 50))
        self.lineEdit_gift_song.setFont(font6)
        self.lineEdit_gift_song.setStyleSheet(u"background-color:white; border:none; color:black")

        self.horizontalLayout_94.addWidget(self.lineEdit_gift_song)

        self.pushButton_79 = QPushButton(self.frame_179)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_79.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"../resource/icons/search_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_79.setIcon(icon8)
        self.pushButton_79.setIconSize(QSize(30, 30))
        self.pushButton_79.setAutoRepeatDelay(305)
        self.pushButton_79.setFlat(True)

        self.horizontalLayout_94.addWidget(self.pushButton_79)


        self.verticalLayout_72.addWidget(self.frame_179)

        self.scrollArea_2 = QScrollArea(self.frame_113)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 664, 556))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.radio_label_gift_song = QLabel(self.scrollAreaWidgetContents_3)
        self.radio_label_gift_song.setObjectName(u"radio_label_gift_song")
        sizePolicy.setHeightForWidth(self.radio_label_gift_song.sizePolicy().hasHeightForWidth())
        self.radio_label_gift_song.setSizePolicy(sizePolicy)
        self.radio_label_gift_song.setFont(font1)
        self.radio_label_gift_song.setStyleSheet(u"border:2px solid #6522f2; border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px; \n"
"border-left:none;padding:10px;")
        self.radio_label_gift_song.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.radio_label_gift_song, 0, 1, 1, 1, Qt.AlignRight)

        self.radioButton_gift_song = QRadioButton(self.scrollAreaWidgetContents_3)
        self.radioButton_gift_song.setObjectName(u"radioButton_gift_song")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_gift_song.sizePolicy().hasHeightForWidth())
        self.radioButton_gift_song.setSizePolicy(sizePolicy1)
        self.radioButton_gift_song.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_song.setFont(font1)
        self.radioButton_gift_song.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")
        self.radioButton_gift_song.setChecked(True)
        self.radioButton_gift_song.setAutoExclusive(True)

        self.gridLayout.addWidget(self.radioButton_gift_song, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_72.addWidget(self.scrollArea_2)


        self.verticalLayout_91.addWidget(self.frame_113)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_89 = QVBoxLayout(self.tab_3)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.frame_110 = QFrame(self.tab_3)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_110)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.frame_171 = QFrame(self.frame_110)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setMinimumSize(QSize(0, 50))
        self.frame_171.setStyleSheet(u"background-color:white;")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(10, 0, 0, 0)
        self.lineEdit_gift_singer = QLineEdit(self.frame_171)
        self.lineEdit_gift_singer.setObjectName(u"lineEdit_gift_singer")
        self.lineEdit_gift_singer.setMinimumSize(QSize(0, 50))
        self.lineEdit_gift_singer.setFont(font6)
        self.lineEdit_gift_singer.setStyleSheet(u"background-color:white; border:none; color:black")

        self.horizontalLayout_85.addWidget(self.lineEdit_gift_singer)

        self.pushButton_21 = QPushButton(self.frame_171)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_21.setStyleSheet(u"")
        self.pushButton_21.setIcon(icon8)
        self.pushButton_21.setIconSize(QSize(30, 30))
        self.pushButton_21.setAutoRepeatDelay(305)
        self.pushButton_21.setFlat(True)

        self.horizontalLayout_85.addWidget(self.pushButton_21)


        self.verticalLayout_98.addWidget(self.frame_171)

        self.scrollArea_3 = QScrollArea(self.frame_110)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFont(font1)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 664, 556))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(30, -1, 30, -1)
        self.label_37 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"border:2px solid #6522f2; border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px; \n"
"border-left:none;padding:10px;")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_37, 3, 1, 1, 1)

        self.radioButton_gift_singer3 = QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton_gift_singer3.setObjectName(u"radioButton_gift_singer3")
        self.radioButton_gift_singer3.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer3.setFont(font1)
        self.radioButton_gift_singer3.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")

        self.gridLayout_4.addWidget(self.radioButton_gift_singer3, 3, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"border:2px solid #6522f2; border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px; \n"
"border-left:none;padding:10px;")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_29, 2, 1, 1, 1)

        self.radioButton_gift_singer4 = QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton_gift_singer4.setObjectName(u"radioButton_gift_singer4")
        self.radioButton_gift_singer4.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer4.setFont(font1)
        self.radioButton_gift_singer4.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")

        self.gridLayout_4.addWidget(self.radioButton_gift_singer4, 4, 0, 1, 1)

        self.radioButton_gift_singer2 = QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton_gift_singer2.setObjectName(u"radioButton_gift_singer2")
        self.radioButton_gift_singer2.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer2.setFont(font1)
        self.radioButton_gift_singer2.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")

        self.gridLayout_4.addWidget(self.radioButton_gift_singer2, 2, 0, 1, 1)

        self.radioButton_gift_singer1 = QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton_gift_singer1.setObjectName(u"radioButton_gift_singer1")
        sizePolicy1.setHeightForWidth(self.radioButton_gift_singer1.sizePolicy().hasHeightForWidth())
        self.radioButton_gift_singer1.setSizePolicy(sizePolicy1)
        self.radioButton_gift_singer1.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer1.setFont(font1)
        self.radioButton_gift_singer1.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")
        self.radioButton_gift_singer1.setChecked(True)
        self.radioButton_gift_singer1.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.radioButton_gift_singer1, 0, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"border:2px solid #6522f2; border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px; \n"
"border-left:none;padding:10px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1, Qt.AlignRight)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"border:2px solid #6522f2; border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px; \n"
"border-left:none;padding:10px;")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_38, 4, 1, 1, 1)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.radioButton_gift_singer1_3 = QRadioButton(self.frame_33)
        self.radioButton_gift_singer1_3.setObjectName(u"radioButton_gift_singer1_3")
        self.radioButton_gift_singer1_3.setGeometry(QRect(0, 160, 546, 50))
        sizePolicy1.setHeightForWidth(self.radioButton_gift_singer1_3.sizePolicy().hasHeightForWidth())
        self.radioButton_gift_singer1_3.setSizePolicy(sizePolicy1)
        self.radioButton_gift_singer1_3.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer1_3.setFont(font1)
        self.radioButton_gift_singer1_3.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")
        self.radioButton_gift_singer1_3.setChecked(False)
        self.radioButton_gift_singer1_3.setAutoExclusive(True)
        self.radioButton_gift_singer1_4 = QRadioButton(self.frame_33)
        self.radioButton_gift_singer1_4.setObjectName(u"radioButton_gift_singer1_4")
        self.radioButton_gift_singer1_4.setGeometry(QRect(0, 230, 546, 50))
        sizePolicy1.setHeightForWidth(self.radioButton_gift_singer1_4.sizePolicy().hasHeightForWidth())
        self.radioButton_gift_singer1_4.setSizePolicy(sizePolicy1)
        self.radioButton_gift_singer1_4.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer1_4.setFont(font1)
        self.radioButton_gift_singer1_4.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")
        self.radioButton_gift_singer1_4.setChecked(False)
        self.radioButton_gift_singer1_4.setAutoExclusive(True)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(10, 10, 501, 141))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.radioButton_gift_singer1_5 = QRadioButton(self.frame_34)
        self.radioButton_gift_singer1_5.setObjectName(u"radioButton_gift_singer1_5")
        self.radioButton_gift_singer1_5.setGeometry(QRect(10, 0, 546, 50))
        sizePolicy1.setHeightForWidth(self.radioButton_gift_singer1_5.sizePolicy().hasHeightForWidth())
        self.radioButton_gift_singer1_5.setSizePolicy(sizePolicy1)
        self.radioButton_gift_singer1_5.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer1_5.setFont(font1)
        self.radioButton_gift_singer1_5.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")
        self.radioButton_gift_singer1_5.setChecked(False)
        self.radioButton_gift_singer1_5.setAutoExclusive(True)
        self.radioButton_gift_singer1_6 = QRadioButton(self.frame_34)
        self.radioButton_gift_singer1_6.setObjectName(u"radioButton_gift_singer1_6")
        self.radioButton_gift_singer1_6.setGeometry(QRect(10, 70, 546, 50))
        sizePolicy1.setHeightForWidth(self.radioButton_gift_singer1_6.sizePolicy().hasHeightForWidth())
        self.radioButton_gift_singer1_6.setSizePolicy(sizePolicy1)
        self.radioButton_gift_singer1_6.setMinimumSize(QSize(0, 50))
        self.radioButton_gift_singer1_6.setFont(font1)
        self.radioButton_gift_singer1_6.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px; \n"
"border-right:none;\n"
"padding:10px;")
        self.radioButton_gift_singer1_6.setChecked(False)
        self.radioButton_gift_singer1_6.setAutoExclusive(True)

        self.gridLayout_4.addWidget(self.frame_33, 1, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_98.addWidget(self.scrollArea_3)


        self.verticalLayout_89.addWidget(self.frame_110)

        self.tabWidget_2.addTab(self.tab_3, "")

        self.verticalLayout_88.addWidget(self.tabWidget_2)


        self.verticalLayout_95.addWidget(self.frame_109)


        self.verticalLayout_87.addWidget(self.frame_108)

        self.stackedPages.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_96 = QVBoxLayout(self.page_9)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.frame_159 = QFrame(self.page_9)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_159)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(30, 30, 30, -1)
        self.frame_162 = QFrame(self.frame_159)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setStyleSheet(u"background-color:#D9D9D9;")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_161 = QLabel(self.frame_162)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font10)
        self.label_161.setStyleSheet(u"color: red;")
        self.label_161.setAlignment(Qt.AlignCenter)
        self.label_161.setWordWrap(True)

        self.horizontalLayout_80.addWidget(self.label_161, 0, Qt.AlignHCenter)


        self.verticalLayout_102.addWidget(self.frame_162)


        self.verticalLayout_96.addWidget(self.frame_159)

        self.frame_30 = QFrame(self.page_9)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_39 = QFrame(self.frame_30)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(50, 0))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.pushButton_102 = QPushButton(self.frame_39)
        self.pushButton_102.setObjectName(u"pushButton_102")
        self.pushButton_102.setGeometry(QRect(11, 380, 41, 41))
        self.pushButton_102.setIcon(icon7)
        self.pushButton_102.setIconSize(QSize(30, 30))

        self.horizontalLayout_20.addWidget(self.frame_39)

        self.frame_153 = QFrame(self.frame_30)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_153)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_196 = QFrame(self.frame_153)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.gift_detail_song_2 = QLabel(self.frame_196)
        self.gift_detail_song_2.setObjectName(u"gift_detail_song_2")
        self.gift_detail_song_2.setFont(font8)
        self.gift_detail_song_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.gift_detail_song_2, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_21.addWidget(self.frame_196)

        self.frame_154 = QFrame(self.frame_153)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 11, -1, -1)
        self.gift_detail_singer_2 = QLabel(self.frame_154)
        self.gift_detail_singer_2.setObjectName(u"gift_detail_singer_2")
        self.gift_detail_singer_2.setMaximumSize(QSize(16777215, 16777215))
        self.gift_detail_singer_2.setFont(font9)
        self.gift_detail_singer_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.gift_detail_singer_2, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_21.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_153)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_160 = QLabel(self.frame_155)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font7)
        self.label_160.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_138.addWidget(self.label_160, 0, Qt.AlignLeft)

        self.label_165 = QLabel(self.frame_155)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setFont(font7)
        self.label_165.setStyleSheet(u"*{color:#ffffff;}")
        self.label_165.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_138.addWidget(self.label_165, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_155, 0, Qt.AlignBottom)

        self.frame_156 = QFrame(self.frame_153)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMaximumSize(QSize(16777215, 30))
        self.frame_156.setStyleSheet(u"*{\n"
"  border-radius: 15px;\n"
"  background-color: #6522f2;}")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_156)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(15, 10, 15, 10)
        self.manito_post_music_slider = QSlider(self.frame_156)
        self.manito_post_music_slider.setObjectName(u"manito_post_music_slider")
        self.manito_post_music_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: -5px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.manito_post_music_slider.setValue(25)
        self.manito_post_music_slider.setSliderPosition(25)
        self.manito_post_music_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_90.addWidget(self.manito_post_music_slider, 0, Qt.AlignVCenter)


        self.verticalLayout_21.addWidget(self.frame_156, 0, Qt.AlignBottom)


        self.horizontalLayout_20.addWidget(self.frame_153, 0, Qt.AlignBottom)

        self.frame_200 = QFrame(self.frame_30)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(50, 216))
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_200)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(-1, 11, -1, -1)
        self.volume_frame_post = QFrame(self.frame_200)
        self.volume_frame_post.setObjectName(u"volume_frame_post")
        self.volume_frame_post.setEnabled(True)
        self.volume_frame_post.setMinimumSize(QSize(0, 150))
        self.volume_frame_post.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.volume_frame_post.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_post.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.volume_frame_post)
        self.horizontalLayout_148.setSpacing(7)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(10, -1, 10, 11)
        self.verticalSlider_33 = QSlider(self.volume_frame_post)
        self.verticalSlider_33.setObjectName(u"verticalSlider_33")
        self.verticalSlider_33.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin:2  5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: 0 -5px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.verticalSlider_33.setValue(40)
        self.verticalSlider_33.setOrientation(Qt.Vertical)

        self.horizontalLayout_148.addWidget(self.verticalSlider_33)


        self.verticalLayout_142.addWidget(self.volume_frame_post, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pushButton_10 = QPushButton(self.frame_200)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QSize(30, 30))

        self.verticalLayout_142.addWidget(self.pushButton_10, 0, Qt.AlignBottom)


        self.horizontalLayout_20.addWidget(self.frame_200, 0, Qt.AlignBottom)


        self.verticalLayout_96.addWidget(self.frame_30)

        self.stackedPages.addWidget(self.page_9)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.horizontalLayout_12 = QHBoxLayout(self.page5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_23 = QFrame(self.page5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_23)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(400, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"*{\n"
"background-color: #6522f2;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 100, 50, 100)
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 100))
        font13 = QFont()
        font13.setPointSize(18)
        font13.setBold(True)
        self.pushButton_4.setFont(font13)
        self.pushButton_4.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_4, 0, Qt.AlignVCenter)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 100))
        self.pushButton_7.setFont(font13)
        self.pushButton_7.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_7, 0, Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_68 = QFrame(self.frame_23)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_68)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 16777215))
        self.label_21.setCursor(QCursor(Qt.ArrowCursor))
        self.label_21.setTabletTracking(False)
        self.label_21.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_21.setPixmap(QPixmap(u"../resource/lp.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(False)

        self.horizontalLayout_29.addWidget(self.label_21)


        self.horizontalLayout_8.addWidget(self.frame_68)


        self.horizontalLayout_12.addWidget(self.frame_23, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.horizontalLayout_14 = QHBoxLayout(self.page6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_8 = QFrame(self.page6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(600, 400))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_8)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, -1)
        self.frame_70 = QFrame(self.frame_8)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_70)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, -1)
        self.label_46 = QLabel(self.frame_70)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setPixmap(QPixmap(u"../resource/icons/envelope.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_46.setMargin(1)
        self.label_46.setIndent(-1)
        self.label_46.setOpenExternalLinks(False)

        self.verticalLayout_43.addWidget(self.label_46)

        self.label_24 = QLabel(self.frame_70)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u"../icons/envelope.png"))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_24, 0, Qt.AlignTop)


        self.verticalLayout_42.addWidget(self.frame_70)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(11, -1, -1, -1)
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setFont(font12)
        self.label.setStyleSheet(u"*{color:#ffffff;}")

        self.verticalLayout_9.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_18)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(400, 50))
        self.lineEdit.setStyleSheet(u"*{background-color:#ffffff; color:black;}")

        self.horizontalLayout_17.addWidget(self.lineEdit)

        self.pushButton_8 = QPushButton(self.frame_18)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 50))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        self.pushButton_8.setFont(font14)
        self.pushButton_8.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"*{color:black;background-color: #d9d9d9;}")
        icon9 = QIcon()
        icon9.addFile(u"../resource/icons/secret.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon9)

        self.horizontalLayout_17.addWidget(self.pushButton_8)


        self.verticalLayout_9.addWidget(self.frame_18, 0, Qt.AlignTop)


        self.verticalLayout_42.addWidget(self.frame_14, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages.addWidget(self.page6)
        self.page7 = QWidget()
        self.page7.setObjectName(u"page7")
        self.verticalLayout_16 = QVBoxLayout(self.page7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_19 = QFrame(self.page7)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, -1, 15, -1)
        self.postcard_detail_img = QLabel(self.frame_24)
        self.postcard_detail_img.setObjectName(u"postcard_detail_img")
        font15 = QFont()
        font15.setPointSize(28)
        self.postcard_detail_img.setFont(font15)
        self.postcard_detail_img.setLayoutDirection(Qt.LeftToRight)
        self.postcard_detail_img.setStyleSheet(u"background:#D9D9D9; color:red;")
        self.postcard_detail_img.setTextFormat(Qt.AutoText)
        self.postcard_detail_img.setAlignment(Qt.AlignCenter)
        self.postcard_detail_img.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.postcard_detail_img)


        self.verticalLayout_13.addWidget(self.frame_24)

        self.frame_32 = QFrame(self.frame_19)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_40 = QFrame(self.frame_32)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(50, 0))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.pushButton_101 = QPushButton(self.frame_40)
        self.pushButton_101.setObjectName(u"pushButton_101")
        self.pushButton_101.setGeometry(QRect(10, 370, 41, 41))
        self.pushButton_101.setIcon(icon7)
        self.pushButton_101.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.frame_40)

        self.frame_163 = QFrame(self.frame_32)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_163)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_195 = QFrame(self.frame_163)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_195)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.gift_detail_song_3 = QLabel(self.frame_195)
        self.gift_detail_song_3.setObjectName(u"gift_detail_song_3")
        self.gift_detail_song_3.setFont(font8)
        self.gift_detail_song_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.gift_detail_song_3, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_23.addWidget(self.frame_195)

        self.frame_164 = QFrame(self.frame_163)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 11, -1, -1)
        self.gift_detail_singer_3 = QLabel(self.frame_164)
        self.gift_detail_singer_3.setObjectName(u"gift_detail_singer_3")
        self.gift_detail_singer_3.setMaximumSize(QSize(16777215, 16777215))
        self.gift_detail_singer_3.setFont(font9)
        self.gift_detail_singer_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.gift_detail_singer_3, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_23.addWidget(self.frame_164)

        self.frame_165 = QFrame(self.frame_163)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_162 = QLabel(self.frame_165)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setFont(font7)
        self.label_162.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_142.addWidget(self.label_162, 0, Qt.AlignLeft)

        self.label_163 = QLabel(self.frame_165)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setFont(font7)
        self.label_163.setStyleSheet(u"*{color:#ffffff;}")
        self.label_163.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_142.addWidget(self.label_163, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_165, 0, Qt.AlignBottom)

        self.frame_166 = QFrame(self.frame_163)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMaximumSize(QSize(16777215, 30))
        self.frame_166.setStyleSheet(u"*{\n"
"  border-radius: 15px;\n"
"  background-color: #6522f2;}")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_166)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(15, 10, 15, 10)
        self.postcard_music_slider = QSlider(self.frame_166)
        self.postcard_music_slider.setObjectName(u"postcard_music_slider")
        self.postcard_music_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: -5px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.postcard_music_slider.setValue(25)
        self.postcard_music_slider.setSliderPosition(25)
        self.postcard_music_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_92.addWidget(self.postcard_music_slider, 0, Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_166, 0, Qt.AlignBottom)


        self.horizontalLayout_22.addWidget(self.frame_163, 0, Qt.AlignBottom)

        self.frame_199 = QFrame(self.frame_32)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setMinimumSize(QSize(50, 216))
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_199)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(-1, 11, -1, -1)
        self.volume_frame_received = QFrame(self.frame_199)
        self.volume_frame_received.setObjectName(u"volume_frame_received")
        self.volume_frame_received.setEnabled(True)
        self.volume_frame_received.setMinimumSize(QSize(0, 150))
        self.volume_frame_received.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.volume_frame_received.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_received.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.volume_frame_received)
        self.horizontalLayout_147.setSpacing(7)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(10, -1, 10, 11)
        self.verticalSlider_32 = QSlider(self.volume_frame_received)
        self.verticalSlider_32.setObjectName(u"verticalSlider_32")
        self.verticalSlider_32.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin:2  5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: 0 -5px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.verticalSlider_32.setValue(40)
        self.verticalSlider_32.setOrientation(Qt.Vertical)

        self.horizontalLayout_147.addWidget(self.verticalSlider_32)


        self.verticalLayout_141.addWidget(self.volume_frame_received, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pushButton_11 = QPushButton(self.frame_199)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.verticalLayout_141.addWidget(self.pushButton_11, 0, Qt.AlignBottom)


        self.horizontalLayout_22.addWidget(self.frame_199, 0, Qt.AlignBottom)


        self.verticalLayout_13.addWidget(self.frame_32)


        self.verticalLayout_16.addWidget(self.frame_19)

        self.stackedPages.addWidget(self.page7)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.verticalLayout_18 = QVBoxLayout(self.page8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_21 = QFrame(self.page8)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(700, 500))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 100, 0, 0)
        self.label_4 = QLabel(self.frame_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 100))
        self.label_4.setMaximumSize(QSize(200, 200))
        font16 = QFont()
        font16.setPointSize(20)
        self.label_4.setFont(font16)
        self.label_4.setPixmap(QPixmap(u"../resource/qr.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_21)
        self.label_3.setObjectName(u"label_3")
        font17 = QFont()
        font17.setPointSize(18)
        self.label_3.setFont(font17)
        self.label_3.setStyleSheet(u"*{color:#ffffff;}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_3)


        self.verticalLayout_18.addWidget(self.frame_21, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_15 = QPushButton(self.page8)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_18.addWidget(self.pushButton_15, 0, Qt.AlignHCenter)

        self.stackedPages.addWidget(self.page8)
        self.page9 = QWidget()
        self.page9.setObjectName(u"page9")
        self.verticalLayout_22 = QVBoxLayout(self.page9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_22 = QFrame(self.page9)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_22)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_46 = QFrame(self.frame_22)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 150))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, -1, -1, 0)
        self.frame_72 = QFrame(self.frame_46)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(450, 80))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_72)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_15 = QLabel(self.frame_72)
        self.label_15.setObjectName(u"label_15")
        font18 = QFont()
        font18.setFamilies([u"Arial"])
        font18.setPointSize(14)
        font18.setBold(True)
        self.label_15.setFont(font18)
        self.label_15.setStyleSheet(u"*{width: 312px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
" color:black; background-color: #2ae2e2;}")
        self.label_15.setFrameShape(QFrame.Box)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_15)


        self.horizontalLayout_38.addWidget(self.frame_72, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_71 = QFrame(self.frame_46)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(140, 60))
        self.frame_71.setFont(font1)
        self.frame_71.setStyleSheet(u"")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_71)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_71)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(140, 60))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"*{border-radius: 25px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}")

        self.verticalLayout_44.addWidget(self.pushButton_9)


        self.horizontalLayout_38.addWidget(self.frame_71, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_19.addWidget(self.frame_46, 0, Qt.AlignTop)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 400))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_26)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(20, -1, 20, -1)
        self.tabWidget = QTabWidget(self.frame_26)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font12)
        self.tabWidget.setStyleSheet(u"QTabWidget{\n"
"border:none;\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #6522F2;\n"
"    position: absolute;\n"
"top:1em;\n"
"}\n"
"QTabBar::tab{\n"
"background-color:black;\n"
"}")
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_148 = QFrame(self.tab_2)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.frame_172 = QFrame(self.frame_148)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setGeometry(QRect(1, 10, 684, 50))
        self.frame_172.setMinimumSize(QSize(0, 50))
        self.frame_172.setStyleSheet(u"background-color:white;")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(10, 0, 0, 0)
        self.lineEdit_postcard_song = QLineEdit(self.frame_172)
        self.lineEdit_postcard_song.setObjectName(u"lineEdit_postcard_song")
        self.lineEdit_postcard_song.setMinimumSize(QSize(0, 50))
        self.lineEdit_postcard_song.setFont(font6)
        self.lineEdit_postcard_song.setStyleSheet(u"background-color:white; border:none; color:black")

        self.horizontalLayout_86.addWidget(self.lineEdit_postcard_song)

        self.pushButton_22 = QPushButton(self.frame_172)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_22.setStyleSheet(u"")
        self.pushButton_22.setIcon(icon8)
        self.pushButton_22.setIconSize(QSize(30, 30))
        self.pushButton_22.setAutoRepeatDelay(305)
        self.pushButton_22.setFlat(True)

        self.horizontalLayout_86.addWidget(self.pushButton_22)

        self.frame_152 = QFrame(self.frame_148)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setGeometry(QRect(1, 65, 684, 16))
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.radioButton_postcard_song1 = QRadioButton(self.frame_148)
        self.radioButton_postcard_song1.setObjectName(u"radioButton_postcard_song1")
        self.radioButton_postcard_song1.setGeometry(QRect(1, 99, 681, 50))
        self.radioButton_postcard_song1.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_song1.setFont(font1)
        self.radioButton_postcard_song1.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radioButton_postcard_song1.setChecked(True)
        self.radioButton_postcard_song1.setAutoExclusive(True)
        self.radioButton_postcard_song2 = QRadioButton(self.frame_148)
        self.radioButton_postcard_song2.setObjectName(u"radioButton_postcard_song2")
        self.radioButton_postcard_song2.setGeometry(QRect(1, 154, 681, 50))
        self.radioButton_postcard_song2.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_song2.setFont(font1)
        self.radioButton_postcard_song2.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radioButton_postcard_song3 = QRadioButton(self.frame_148)
        self.radioButton_postcard_song3.setObjectName(u"radioButton_postcard_song3")
        self.radioButton_postcard_song3.setGeometry(QRect(1, 208, 681, 50))
        self.radioButton_postcard_song3.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_song3.setFont(font1)
        self.radioButton_postcard_song3.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radioButton_postcard_song4 = QRadioButton(self.frame_148)
        self.radioButton_postcard_song4.setObjectName(u"radioButton_postcard_song4")
        self.radioButton_postcard_song4.setGeometry(QRect(1, 263, 681, 50))
        self.radioButton_postcard_song4.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_song4.setFont(font1)
        self.radioButton_postcard_song4.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radio_label_postcard_song1 = QLabel(self.frame_148)
        self.radio_label_postcard_song1.setObjectName(u"radio_label_postcard_song1")
        self.radio_label_postcard_song1.setGeometry(QRect(611, 113, 56, 21))
        self.radio_label_postcard_song1.setFont(font1)
        self.radio_label_postcard_song1.setAlignment(Qt.AlignCenter)
        self.radio_label_postcard_song2 = QLabel(self.frame_148)
        self.radio_label_postcard_song2.setObjectName(u"radio_label_postcard_song2")
        self.radio_label_postcard_song2.setGeometry(QRect(611, 166, 56, 21))
        self.radio_label_postcard_song2.setFont(font1)
        self.radio_label_postcard_song2.setAlignment(Qt.AlignCenter)
        self.radio_label_postcard_song3 = QLabel(self.frame_148)
        self.radio_label_postcard_song3.setObjectName(u"radio_label_postcard_song3")
        self.radio_label_postcard_song3.setGeometry(QRect(611, 220, 56, 21))
        self.radio_label_postcard_song3.setFont(font1)
        self.radio_label_postcard_song3.setAlignment(Qt.AlignCenter)
        self.radio_label_postcard_song4 = QLabel(self.frame_148)
        self.radio_label_postcard_song4.setObjectName(u"radio_label_postcard_song4")
        self.radio_label_postcard_song4.setGeometry(QRect(611, 276, 56, 21))
        self.radio_label_postcard_song4.setFont(font1)
        self.radio_label_postcard_song4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.frame_148)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_128 = QFrame(self.tab)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.frame_174 = QFrame(self.frame_128)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setGeometry(QRect(1, 10, 684, 50))
        self.frame_174.setMinimumSize(QSize(0, 50))
        self.frame_174.setStyleSheet(u"background-color:white;")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_174)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(10, 0, 0, 0)
        self.lineEdit_postcard_singer = QLineEdit(self.frame_174)
        self.lineEdit_postcard_singer.setObjectName(u"lineEdit_postcard_singer")
        self.lineEdit_postcard_singer.setMinimumSize(QSize(0, 50))
        self.lineEdit_postcard_singer.setFont(font6)
        self.lineEdit_postcard_singer.setStyleSheet(u"background-color:white; border:none; color:black")

        self.horizontalLayout_88.addWidget(self.lineEdit_postcard_singer)

        self.pushButton_67 = QPushButton(self.frame_174)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_67.setStyleSheet(u"")
        self.pushButton_67.setIcon(icon8)
        self.pushButton_67.setIconSize(QSize(30, 30))
        self.pushButton_67.setAutoRepeatDelay(305)
        self.pushButton_67.setFlat(True)

        self.horizontalLayout_88.addWidget(self.pushButton_67)

        self.frame_129 = QFrame(self.frame_128)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setGeometry(QRect(1, 65, 684, 16))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.radioButton_postcard_singer1 = QRadioButton(self.frame_128)
        self.radioButton_postcard_singer1.setObjectName(u"radioButton_postcard_singer1")
        self.radioButton_postcard_singer1.setGeometry(QRect(1, 99, 681, 50))
        self.radioButton_postcard_singer1.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_singer1.setFont(font1)
        self.radioButton_postcard_singer1.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radioButton_postcard_singer1.setChecked(True)
        self.radioButton_postcard_singer1.setAutoExclusive(True)
        self.radioButton_postcard_singer2 = QRadioButton(self.frame_128)
        self.radioButton_postcard_singer2.setObjectName(u"radioButton_postcard_singer2")
        self.radioButton_postcard_singer2.setGeometry(QRect(1, 154, 681, 50))
        self.radioButton_postcard_singer2.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_singer2.setFont(font1)
        self.radioButton_postcard_singer2.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radioButton_postcard_singer3 = QRadioButton(self.frame_128)
        self.radioButton_postcard_singer3.setObjectName(u"radioButton_postcard_singer3")
        self.radioButton_postcard_singer3.setGeometry(QRect(1, 208, 681, 50))
        self.radioButton_postcard_singer3.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_singer3.setFont(font1)
        self.radioButton_postcard_singer3.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radioButton_postcard_singer4 = QRadioButton(self.frame_128)
        self.radioButton_postcard_singer4.setObjectName(u"radioButton_postcard_singer4")
        self.radioButton_postcard_singer4.setGeometry(QRect(1, 263, 681, 50))
        self.radioButton_postcard_singer4.setMinimumSize(QSize(0, 50))
        self.radioButton_postcard_singer4.setFont(font1)
        self.radioButton_postcard_singer4.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px; padding:10px;")
        self.radio_label_postcard_singer1 = QLabel(self.frame_128)
        self.radio_label_postcard_singer1.setObjectName(u"radio_label_postcard_singer1")
        self.radio_label_postcard_singer1.setGeometry(QRect(611, 113, 56, 21))
        self.radio_label_postcard_singer1.setFont(font1)
        self.radio_label_postcard_singer1.setAlignment(Qt.AlignCenter)
        self.radio_label_postcard_singer2 = QLabel(self.frame_128)
        self.radio_label_postcard_singer2.setObjectName(u"radio_label_postcard_singer2")
        self.radio_label_postcard_singer2.setGeometry(QRect(611, 166, 56, 21))
        self.radio_label_postcard_singer2.setFont(font1)
        self.radio_label_postcard_singer2.setAlignment(Qt.AlignCenter)
        self.radio_label_postcard_singer3 = QLabel(self.frame_128)
        self.radio_label_postcard_singer3.setObjectName(u"radio_label_postcard_singer3")
        self.radio_label_postcard_singer3.setGeometry(QRect(611, 220, 56, 21))
        self.radio_label_postcard_singer3.setFont(font1)
        self.radio_label_postcard_singer3.setAlignment(Qt.AlignCenter)
        self.radio_label_postcard_singer4 = QLabel(self.frame_128)
        self.radio_label_postcard_singer4.setObjectName(u"radio_label_postcard_singer4")
        self.radio_label_postcard_singer4.setGeometry(QRect(611, 276, 56, 21))
        self.radio_label_postcard_singer4.setFont(font1)
        self.radio_label_postcard_singer4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.frame_128)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_46.addWidget(self.tabWidget)


        self.verticalLayout_19.addWidget(self.frame_26)


        self.verticalLayout_22.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.stackedPages.addWidget(self.page9)
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")
        self.verticalLayout_28 = QVBoxLayout(self.page10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_36 = QFrame(self.page10)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_36)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_73 = QFrame(self.frame_36)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(450, 80))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_18 = QLabel(self.frame_73)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setFont(font18)
        self.label_18.setStyleSheet(u"*{width: 312px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
" color:black; background-color: #2ae2e2;}")
        self.label_18.setFrameShape(QFrame.Box)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_18)


        self.verticalLayout_48.addWidget(self.frame_73, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_16 = QLabel(self.frame_36)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font15)
        self.label_16.setStyleSheet(u"background:#D9D9D9; color:red;")
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setWordWrap(True)

        self.verticalLayout_48.addWidget(self.label_16)

        self.frame_31 = QFrame(self.frame_36)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_41 = QFrame(self.frame_31)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(50, 0))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.pushButton_99 = QPushButton(self.frame_41)
        self.pushButton_99.setObjectName(u"pushButton_99")
        self.pushButton_99.setGeometry(QRect(11, 224, 41, 41))
        self.pushButton_99.setIcon(icon7)
        self.pushButton_99.setIconSize(QSize(30, 30))

        self.horizontalLayout_19.addWidget(self.frame_41)

        self.frame_130 = QFrame(self.frame_31)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_130)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.frame_197 = QFrame(self.frame_130)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.gift_detail_song_4 = QLabel(self.frame_197)
        self.gift_detail_song_4.setObjectName(u"gift_detail_song_4")
        self.gift_detail_song_4.setFont(font8)
        self.gift_detail_song_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.gift_detail_song_4, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_71.addWidget(self.frame_197)

        self.frame_131 = QFrame(self.frame_130)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_131)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 11, -1, -1)
        self.gift_detail_singer_4 = QLabel(self.frame_131)
        self.gift_detail_singer_4.setObjectName(u"gift_detail_singer_4")
        self.gift_detail_singer_4.setMaximumSize(QSize(16777215, 16777215))
        self.gift_detail_singer_4.setFont(font9)
        self.gift_detail_singer_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.gift_detail_singer_4, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_71.addWidget(self.frame_131)

        self.frame_138 = QFrame(self.frame_130)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.label_164 = QLabel(self.frame_138)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setFont(font7)
        self.label_164.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_139.addWidget(self.label_164, 0, Qt.AlignLeft)

        self.label_166 = QLabel(self.frame_138)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setFont(font7)
        self.label_166.setStyleSheet(u"*{color:#ffffff;}")
        self.label_166.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_139.addWidget(self.label_166, 0, Qt.AlignRight)


        self.verticalLayout_71.addWidget(self.frame_138, 0, Qt.AlignBottom)

        self.frame_140 = QFrame(self.frame_130)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMaximumSize(QSize(16777215, 30))
        self.frame_140.setStyleSheet(u"*{\n"
"  border-radius: 15px;\n"
"  background-color: #6522f2;}")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_140)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(15, 10, 15, 10)
        self.postcard_send_music_slider = QSlider(self.frame_140)
        self.postcard_send_music_slider.setObjectName(u"postcard_send_music_slider")
        self.postcard_send_music_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: -5px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.postcard_send_music_slider.setValue(25)
        self.postcard_send_music_slider.setSliderPosition(25)
        self.postcard_send_music_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_80.addWidget(self.postcard_send_music_slider, 0, Qt.AlignVCenter)


        self.verticalLayout_71.addWidget(self.frame_140, 0, Qt.AlignBottom)


        self.horizontalLayout_19.addWidget(self.frame_130, 0, Qt.AlignBottom)

        self.frame_201 = QFrame(self.frame_31)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMinimumSize(QSize(50, 216))
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_201)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(-1, 11, -1, -1)
        self.volume_frame_send = QFrame(self.frame_201)
        self.volume_frame_send.setObjectName(u"volume_frame_send")
        self.volume_frame_send.setEnabled(True)
        self.volume_frame_send.setMinimumSize(QSize(0, 150))
        self.volume_frame_send.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.volume_frame_send.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_send.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.volume_frame_send)
        self.horizontalLayout_143.setSpacing(7)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(10, -1, 10, 11)
        self.verticalSlider_30 = QSlider(self.volume_frame_send)
        self.verticalSlider_30.setObjectName(u"verticalSlider_30")
        self.verticalSlider_30.setStyleSheet(u"QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"     /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin:2  5px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border: 1px solid #ffffff;\n"
"    width: 15px;\n"
"	height: 15px;\n"
"    margin: 0 -5px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}")
        self.verticalSlider_30.setValue(40)
        self.verticalSlider_30.setOrientation(Qt.Vertical)

        self.horizontalLayout_143.addWidget(self.verticalSlider_30)


        self.verticalLayout_143.addWidget(self.volume_frame_send, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pushButton_17 = QPushButton(self.frame_201)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setIcon(icon2)
        self.pushButton_17.setIconSize(QSize(30, 30))

        self.verticalLayout_143.addWidget(self.pushButton_17, 0, Qt.AlignBottom)


        self.horizontalLayout_19.addWidget(self.frame_201, 0, Qt.AlignBottom)


        self.verticalLayout_48.addWidget(self.frame_31)


        self.verticalLayout_28.addWidget(self.frame_36)

        self.stackedPages.addWidget(self.page10)
        self.page11 = QWidget()
        self.page11.setObjectName(u"page11")
        self.verticalLayout_29 = QVBoxLayout(self.page11)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_50 = QFrame(self.page11)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_50)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_74 = QFrame(self.frame_50)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(500, 80))
        self.frame_74.setFont(font3)
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_19 = QLabel(self.frame_74)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 0))
        self.label_19.setFont(font18)
        self.label_19.setStyleSheet(u"*{width: 312px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
" color:black; background-color: #2ae2e2;}")
        self.label_19.setFrameShape(QFrame.Box)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_19)


        self.verticalLayout_50.addWidget(self.frame_74, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(600, 400))
        self.frame_52.setMaximumSize(QSize(16777215, 16777215))
        self.frame_52.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_52)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, -1)
        self.frame_75 = QFrame(self.frame_52)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_75)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, -1)
        self.label_31 = QLabel(self.frame_75)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        self.label_31.setPixmap(QPixmap(u"../resource/icons/envelope.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setMargin(1)
        self.label_31.setIndent(-1)
        self.label_31.setOpenExternalLinks(False)

        self.verticalLayout_49.addWidget(self.label_31, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_47.addWidget(self.frame_75, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_47 = QFrame(self.frame_52)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_47)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.label_54 = QLabel(self.frame_47)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.verticalLayout_103.addWidget(self.label_54)

        self.lineEdit_3 = QLineEdit(self.frame_47)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(300, 50))
        self.lineEdit_3.setStyleSheet(u"*{background-color:#ffffff;}")

        self.verticalLayout_103.addWidget(self.lineEdit_3)


        self.verticalLayout_47.addWidget(self.frame_47, 0, Qt.AlignHCenter)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_53)
        self.verticalLayout_30.setSpacing(20)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(11, -1, -1, -1)
        self.label_17 = QLabel(self.frame_53)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"*{color:#ffffff;}")

        self.verticalLayout_30.addWidget(self.label_17, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_76 = QFrame(self.frame_53)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 50))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.frame_76)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(350, 50))
        self.lineEdit_2.setStyleSheet(u"*{background-color:#ffffff;}")

        self.horizontalLayout_30.addWidget(self.lineEdit_2)

        self.pushButton_12 = QPushButton(self.frame_76)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 50))
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))
        font19 = QFont()
        font19.setPointSize(13)
        font19.setBold(True)
        self.pushButton_12.setFont(font19)
        self.pushButton_12.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(u"*{color:black;background-color: #d9d9d9;}")
        self.pushButton_12.setIcon(icon9)

        self.horizontalLayout_30.addWidget(self.pushButton_12, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.frame_76, 0, Qt.AlignTop)


        self.verticalLayout_47.addWidget(self.frame_53, 0, Qt.AlignHCenter)


        self.verticalLayout_50.addWidget(self.frame_52, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_29.addWidget(self.frame_50)

        self.stackedPages.addWidget(self.page11)
        self.page12 = QWidget()
        self.page12.setObjectName(u"page12")
        self.verticalLayout_51 = QVBoxLayout(self.page12)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_77 = QFrame(self.page12)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(450, 80))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_78)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_20 = QLabel(self.frame_78)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font9)
        self.label_20.setStyleSheet(u"*{width: 356px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
"  color:black;\n"
"  background-color: #2ae2e2;}")
        self.label_20.setFrameShape(QFrame.Box)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_20)


        self.horizontalLayout_45.addWidget(self.frame_78, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_51.addWidget(self.frame_77)

        self.stackedPages.addWidget(self.page12)

        self.horizontalLayout_2.addWidget(self.stackedPages)


        self.horizontalLayout_11.addWidget(self.main)


        self.verticalLayout_31.addWidget(self.display1)

        self.display2 = QFrame(self.frame_51)
        self.display2.setObjectName(u"display2")
        self.display2.setMinimumSize(QSize(0, 960))
        self.display2.setFrameShape(QFrame.StyledPanel)
        self.display2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.display2)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.stackedPages2 = QStackedWidget(self.display2)
        self.stackedPages2.setObjectName(u"stackedPages2")
        self.stackedPages2.setFont(font2)
        self.stackedPages2.setStyleSheet(u"")
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.verticalLayout_32 = QVBoxLayout(self.page_draw)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.page_draw)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_16)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(20, -1, 20, -1)
        self.frame_55 = QFrame(self.frame_16)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 11)
        self.frame_81 = QFrame(self.frame_55)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"background-color:white;border-radius:30px;")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.pushButton_28 = QPushButton(self.frame_81)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setStyleSheet(u"*{width:40px; height:40px;background:#000000;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_28)

        self.pushButton_31 = QPushButton(self.frame_81)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"*{width:40px; height:40px;background:#F53333;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.frame_81)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"*{width:40px; height:40px;background:#EE6A1F;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.frame_81)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"*{width:40px; height:40px;background:#E7EA5B;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.frame_81)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setStyleSheet(u"*{width:40px; height:40px;background:#1ACB16;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_34)

        self.pushButton_52 = QPushButton(self.frame_81)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setStyleSheet(u"*{width:40px; height:40px;background:#4C25E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_52)

        self.pushButton_51 = QPushButton(self.frame_81)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setStyleSheet(u"*{width:40px; height:40px;background:#B525E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_51)

        self.pushButton_38 = QPushButton(self.frame_81)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setStyleSheet(u"*{width:40px; height:40px;background:#E8258E;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_38)

        self.pushButton_25 = QPushButton(self.frame_81)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"*{width:40px; height:40px;background:#FFFFFF;color:#000000; border-radius:20;border:1px solid black;}")

        self.horizontalLayout_32.addWidget(self.pushButton_25)


        self.horizontalLayout_6.addWidget(self.frame_81, 0, Qt.AlignBottom)

        self.pushButton_37 = QPushButton(self.frame_55)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(130, 55))
        font20 = QFont()
        font20.setPointSize(14)
        font20.setBold(True)
        self.pushButton_37.setFont(font20)
        self.pushButton_37.setStyleSheet(u"background-color:white; color:black;")

        self.horizontalLayout_6.addWidget(self.pushButton_37, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_54.addWidget(self.frame_55, 0, Qt.AlignBottom)

        self.frame_56 = QFrame(self.frame_16)
        self.frame_56.setObjectName(u"frame_56")
        font21 = QFont()
        font21.setPointSize(7)
        self.frame_56.setFont(font21)
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 0, -1, -1)
        self.painter_widget = QWidget(self.frame_56)
        self.painter_widget.setObjectName(u"painter_widget")
        self.painter_widget.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.painter_widget.sizePolicy().hasHeightForWidth())
        self.painter_widget.setSizePolicy(sizePolicy2)
        self.painter_widget.setMinimumSize(QSize(0, 600))
        font22 = QFont()
        font22.setPointSize(5)
        self.painter_widget.setFont(font22)
        self.painter_widget.setStyleSheet(u"background-color:white;")

        self.horizontalLayout_34.addWidget(self.painter_widget)


        self.verticalLayout_54.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_16)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_22 = QLabel(self.frame_57)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setToolTipDuration(0)

        self.horizontalLayout_7.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.pushButton_53 = QPushButton(self.frame_57)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(140, 60))
        self.pushButton_53.setFont(font9)
        self.pushButton_53.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_53.setStyleSheet(u"background: #6522F2;\n"
"border-radius: 30px;")

        self.horizontalLayout_7.addWidget(self.pushButton_53, 0, Qt.AlignRight)


        self.verticalLayout_54.addWidget(self.frame_57, 0, Qt.AlignTop)


        self.verticalLayout_32.addWidget(self.frame_16)

        self.stackedPages2.addWidget(self.page_draw)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.page_search.setStyleSheet(u"background-color:white;")
        self.verticalLayout_33 = QVBoxLayout(self.page_search)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_58 = QFrame(self.page_search)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"border:none;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_58)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(-1, 100, -1, 100)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_59)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_61)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(-1, -1, -1, 0)
        self.label_23 = QLabel(self.frame_61)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font9)
        self.label_23.setStyleSheet(u"color:black;")

        self.verticalLayout_57.addWidget(self.label_23, 0, Qt.AlignBottom)


        self.verticalLayout_56.addWidget(self.frame_61)

        self.frame_82 = QFrame(self.frame_59)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(500, 0))
        self.frame_83.setMaximumSize(QSize(16777215, 16777215))
        self.frame_83.setStyleSheet(u"*{\n"
"background-color: #6522f2;\n"
"}")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_83)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(50, 100, 50, 100)
        self.frame_101 = QFrame(self.frame_83)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(280, 0))
        self.frame_101.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(30, -1, 0, -1)
        self.pushButton_16 = QPushButton(self.frame_101)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font13)

        self.horizontalLayout_59.addWidget(self.pushButton_16, 0, Qt.AlignLeft)

        self.pushButton_5 = QPushButton(self.frame_101)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setFont(font13)
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"}")
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QSize(50, 50))
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pushButton_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_34.addWidget(self.frame_101, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_33.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.frame_82)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_84)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 16777215))
        self.label_27.setCursor(QCursor(Qt.ArrowCursor))
        self.label_27.setTabletTracking(False)
        self.label_27.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_27.setPixmap(QPixmap(u"../resource/lp.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setWordWrap(False)

        self.horizontalLayout_48.addWidget(self.label_27)


        self.horizontalLayout_33.addWidget(self.frame_84)


        self.verticalLayout_56.addWidget(self.frame_82, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_58.addWidget(self.frame_59)


        self.verticalLayout_33.addWidget(self.frame_58, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages2.addWidget(self.page_search)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_173 = QHBoxLayout(self.page)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(900, 900))
        self.label_5.setPixmap(QPixmap(u"../resource/audiro.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_173.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages2.addWidget(self.page)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setStyleSheet(u"background-color:white;")
        self.verticalLayout_35 = QVBoxLayout(self.page_login)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_62 = QFrame(self.page_login)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"border:none;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_62)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_85 = QFrame(self.frame_62)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"border:none;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_85)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.pushButton_24 = QPushButton(self.frame_85)
        self.pushButton_24.setObjectName(u"pushButton_24")
        font23 = QFont()
        font23.setPointSize(11)
        self.pushButton_24.setFont(font23)
        self.pushButton_24.setStyleSheet(u"color:black;")
        self.pushButton_24.setFlat(True)

        self.verticalLayout_62.addWidget(self.pushButton_24, 0, Qt.AlignLeft)


        self.verticalLayout_36.addWidget(self.frame_85, 0, Qt.AlignBottom)

        self.frame_86 = QFrame(self.frame_62)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(800, 400))
        self.frame_86.setStyleSheet(u"background-color:#6522F2;")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_86)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(-1, 30, -1, 30)
        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_2 = QLabel(self.frame_87)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../resource/qr.png"))

        self.horizontalLayout_49.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_61.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_86)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_88)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(100, -1, 100, -1)
        self.label_26 = QLabel(self.frame_88)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(430, 0))
        font24 = QFont()
        font24.setPointSize(13)
        self.label_26.setFont(font24)
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.label_26)


        self.verticalLayout_61.addWidget(self.frame_88)


        self.verticalLayout_36.addWidget(self.frame_86, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_35.addWidget(self.frame_62, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages2.addWidget(self.page_login)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color:white;")
        self.verticalLayout_65 = QVBoxLayout(self.page_3)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.frame_60 = QFrame(self.page_3)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_60)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(-1, 100, -1, 100)
        self.frame_65 = QFrame(self.frame_60)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"border:none;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_65)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.frame_89 = QFrame(self.frame_65)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(500, 0))
        self.frame_90.setMaximumSize(QSize(16777215, 16777215))
        self.frame_90.setStyleSheet(u"*{\n"
"background-color: #6522f2;\n"
"}")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_90)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(100, 100, 100, 100)
        self.pushButton_6 = QPushButton(self.frame_90)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 100))
        self.pushButton_6.setFont(font9)
        self.pushButton_6.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_6.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_6.setIconSize(QSize(50, 50))

        self.verticalLayout_38.addWidget(self.pushButton_6)


        self.horizontalLayout_35.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.frame_89)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_91)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setCursor(QCursor(Qt.ArrowCursor))
        self.label_32.setTabletTracking(False)
        self.label_32.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_32.setPixmap(QPixmap(u"../resource/lp.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setWordWrap(False)

        self.horizontalLayout_50.addWidget(self.label_32)


        self.horizontalLayout_35.addWidget(self.frame_91)


        self.verticalLayout_59.addWidget(self.frame_89, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_64.addWidget(self.frame_65, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_65.addWidget(self.frame_60)

        self.stackedPages2.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_174 = QHBoxLayout(self.page_2)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.frame_63 = QFrame(self.page_2)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_63)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_66 = QFrame(self.frame_63)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_66)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.frame_92 = QFrame(self.frame_66)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(500, 0))
        self.frame_93.setMaximumSize(QSize(16777215, 16777215))
        self.frame_93.setStyleSheet(u"*{\n"
"background-color: #6522f2;\n"
"}")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_93)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(100, 100, 100, 100)
        self.pushButton_14 = QPushButton(self.frame_93)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 100))
        self.pushButton_14.setFont(font9)
        self.pushButton_14.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_66.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.frame_93)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 100))
        self.pushButton_13.setFont(font9)
        self.pushButton_13.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_13.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_13.setIconSize(QSize(50, 50))

        self.verticalLayout_66.addWidget(self.pushButton_13)


        self.horizontalLayout_51.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_94)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setCursor(QCursor(Qt.ArrowCursor))
        self.label_33.setTabletTracking(False)
        self.label_33.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_33.setPixmap(QPixmap(u"../resource/lp.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setWordWrap(False)

        self.horizontalLayout_52.addWidget(self.label_33)


        self.horizontalLayout_51.addWidget(self.frame_94)


        self.verticalLayout_63.addWidget(self.frame_92, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_37.addWidget(self.frame_66)


        self.horizontalLayout_174.addWidget(self.frame_63)

        self.stackedPages2.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_39 = QVBoxLayout(self.page_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_170 = QFrame(self.page_4)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_170)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_39.addWidget(self.frame_170)

        self.stackedPages2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"")
        self.verticalLayout_67 = QVBoxLayout(self.page_5)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.frame_64 = QFrame(self.page_5)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(800, 500))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_64)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.frame_95 = QFrame(self.frame_64)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(700, 700))
        self.frame_95.setStyleSheet(u"background-color:white;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_95)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.sent_postcard_image = QLabel(self.frame_95)
        self.sent_postcard_image.setObjectName(u"sent_postcard_image")
        font25 = QFont()
        font25.setPointSize(25)
        font25.setBold(True)
        self.sent_postcard_image.setFont(font25)
        self.sent_postcard_image.setStyleSheet(u"color:red;")

        self.verticalLayout_82.addWidget(self.sent_postcard_image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_79.addWidget(self.frame_95)


        self.verticalLayout_67.addWidget(self.frame_64, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_55 = QVBoxLayout(self.page_6)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_96 = QFrame(self.page_6)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_96)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(20, -1, 20, -1)
        self.frame_97 = QFrame(self.frame_96)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(-1, -1, -1, 11)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setStyleSheet(u"background-color:white;border-radius:30px;")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_56.setSpacing(10)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(10, 10, 10, 10)
        self.pushButton_36 = QPushButton(self.frame_98)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setStyleSheet(u"*{width:40px; height:40px;background:#000000;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_36)

        self.pushButton_39 = QPushButton(self.frame_98)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setStyleSheet(u"*{width:40px; height:40px;background:#F53333;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_39)

        self.pushButton_41 = QPushButton(self.frame_98)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setStyleSheet(u"*{width:40px; height:40px;background:#EE6A1F;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_41)

        self.pushButton_42 = QPushButton(self.frame_98)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setStyleSheet(u"*{width:40px; height:40px;background:#E7EA5B;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.frame_98)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setStyleSheet(u"*{width:40px; height:40px;background:#1ACB16;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_43)

        self.pushButton_54 = QPushButton(self.frame_98)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setStyleSheet(u"*{width:40px; height:40px;background:#4C25E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_54)

        self.pushButton_55 = QPushButton(self.frame_98)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setStyleSheet(u"*{width:40px; height:40px;background:#B525E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_55)

        self.pushButton_44 = QPushButton(self.frame_98)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setStyleSheet(u"*{width:40px; height:40px;background:#E8258E;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_56.addWidget(self.pushButton_44)

        self.pushButton_26 = QPushButton(self.frame_98)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setStyleSheet(u"*{width:40px; height:40px;background:#FFFFFF;color:#000000; border-radius:20;border:1px solid black;}")

        self.horizontalLayout_56.addWidget(self.pushButton_26)


        self.horizontalLayout_55.addWidget(self.frame_98, 0, Qt.AlignBottom)

        self.pushButton_45 = QPushButton(self.frame_97)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(130, 55))
        self.pushButton_45.setFont(font20)
        self.pushButton_45.setStyleSheet(u"background-color:white; color:black;")

        self.horizontalLayout_55.addWidget(self.pushButton_45, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_83.addWidget(self.frame_97)

        self.frame_99 = QFrame(self.frame_96)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(-1, 0, -1, -1)
        self.painter_widget_2 = QWidget(self.frame_99)
        self.painter_widget_2.setObjectName(u"painter_widget_2")
        self.painter_widget_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.painter_widget_2.sizePolicy().hasHeightForWidth())
        self.painter_widget_2.setSizePolicy(sizePolicy2)
        self.painter_widget_2.setMinimumSize(QSize(0, 600))
        self.painter_widget_2.setStyleSheet(u"background-color:white;")

        self.horizontalLayout_57.addWidget(self.painter_widget_2)


        self.verticalLayout_83.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_96)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_30 = QLabel(self.frame_100)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)
        self.label_30.setToolTipDuration(0)

        self.horizontalLayout_58.addWidget(self.label_30)

        self.pushButton_56 = QPushButton(self.frame_100)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMinimumSize(QSize(140, 60))
        self.pushButton_56.setFont(font9)
        self.pushButton_56.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_56.setStyleSheet(u"background: #6522F2;\n"
"border-radius: 30px;")

        self.horizontalLayout_58.addWidget(self.pushButton_56, 0, Qt.AlignRight)


        self.verticalLayout_83.addWidget(self.frame_100, 0, Qt.AlignTop)


        self.verticalLayout_55.addWidget(self.frame_96)

        self.stackedPages2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_84 = QVBoxLayout(self.page_7)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.page_7)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_102)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(20, 0, 20, 11)
        self.frame_107 = QFrame(self.frame_102)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_107)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(15, 0, 11, -1)
        self.label_35 = QLabel(self.frame_107)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font12)

        self.verticalLayout_86.addWidget(self.label_35, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_85.addWidget(self.frame_107, 0, Qt.AlignBottom)

        self.frame_103 = QFrame(self.frame_102)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(11, 0, 11, 11)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setStyleSheet(u"background-color:white;border-radius:30px;")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_61.setSpacing(10)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(10, 10, 10, 10)
        self.pushButton_46 = QPushButton(self.frame_104)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setStyleSheet(u"*{width:40px; height:40px;background:#000000;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_46)

        self.pushButton_50 = QPushButton(self.frame_104)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setStyleSheet(u"*{width:40px; height:40px;background:#F53333;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_50)

        self.pushButton_57 = QPushButton(self.frame_104)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setStyleSheet(u"*{width:40px; height:40px;background:#EE6A1F;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_57)

        self.pushButton_58 = QPushButton(self.frame_104)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setStyleSheet(u"*{width:40px; height:40px;background:#E7EA5B;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_58)

        self.pushButton_59 = QPushButton(self.frame_104)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setStyleSheet(u"*{width:40px; height:40px;background:#1ACB16;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_59)

        self.pushButton_60 = QPushButton(self.frame_104)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setStyleSheet(u"*{width:40px; height:40px;background:#4C25E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_60)

        self.pushButton_61 = QPushButton(self.frame_104)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setStyleSheet(u"*{width:40px; height:40px;background:#B525E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_61)

        self.pushButton_62 = QPushButton(self.frame_104)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setStyleSheet(u"*{width:40px; height:40px;background:#E8258E;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_61.addWidget(self.pushButton_62)

        self.pushButton_27 = QPushButton(self.frame_104)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setStyleSheet(u"*{width:40px; height:40px;background:#FFFFFF;color:#000000; border-radius:20;border:1px solid black;}")

        self.horizontalLayout_61.addWidget(self.pushButton_27)


        self.horizontalLayout_60.addWidget(self.frame_104, 0, Qt.AlignBottom)

        self.pushButton_63 = QPushButton(self.frame_103)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMinimumSize(QSize(130, 55))
        self.pushButton_63.setFont(font20)
        self.pushButton_63.setStyleSheet(u"background-color:white; color:black;")

        self.horizontalLayout_60.addWidget(self.pushButton_63, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_85.addWidget(self.frame_103)

        self.frame_105 = QFrame(self.frame_102)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(-1, 0, -1, -1)
        self.painter_widget_3 = QWidget(self.frame_105)
        self.painter_widget_3.setObjectName(u"painter_widget_3")
        self.painter_widget_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.painter_widget_3.sizePolicy().hasHeightForWidth())
        self.painter_widget_3.setSizePolicy(sizePolicy2)
        self.painter_widget_3.setMinimumSize(QSize(0, 600))
        self.painter_widget_3.setStyleSheet(u"background-color:white;")

        self.horizontalLayout_63.addWidget(self.painter_widget_3)


        self.verticalLayout_85.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_102)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_34 = QLabel(self.frame_106)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setToolTipDuration(0)

        self.horizontalLayout_64.addWidget(self.label_34)

        self.pushButton_64 = QPushButton(self.frame_106)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMinimumSize(QSize(170, 60))
        self.pushButton_64.setFont(font9)
        self.pushButton_64.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_64.setStyleSheet(u"background: #6522F2;\n"
"border-radius: 30px;")

        self.horizontalLayout_64.addWidget(self.pushButton_64, 0, Qt.AlignRight)


        self.verticalLayout_85.addWidget(self.frame_106, 0, Qt.AlignTop)


        self.verticalLayout_84.addWidget(self.frame_102)

        self.stackedPages2.addWidget(self.page_7)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_113 = QVBoxLayout(self.page_12)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.page_12)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_111)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(20, 0, 20, 11)
        self.frame_149 = QFrame(self.frame_111)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_149)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(15, 0, 11, -1)
        self.label_36 = QLabel(self.frame_149)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font12)

        self.verticalLayout_112.addWidget(self.label_36, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_110.addWidget(self.frame_149, 0, Qt.AlignBottom)

        self.frame_175 = QFrame(self.frame_111)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_175)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(11, 0, 11, 11)
        self.frame_176 = QFrame(self.frame_175)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setStyleSheet(u"background-color:white;border-radius:30px;")
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_72.setSpacing(10)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(10, 10, 10, 10)
        self.pushButton_68 = QPushButton(self.frame_176)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setStyleSheet(u"*{width:40px; height:40px;background:#000000;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_68)

        self.pushButton_69 = QPushButton(self.frame_176)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setStyleSheet(u"*{width:40px; height:40px;background:#F53333;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_69)

        self.pushButton_70 = QPushButton(self.frame_176)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setStyleSheet(u"*{width:40px; height:40px;background:#EE6A1F;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_70)

        self.pushButton_71 = QPushButton(self.frame_176)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setStyleSheet(u"*{width:40px; height:40px;background:#E7EA5B;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_71)

        self.pushButton_72 = QPushButton(self.frame_176)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setStyleSheet(u"*{width:40px; height:40px;background:#1ACB16;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_72)

        self.pushButton_73 = QPushButton(self.frame_176)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setStyleSheet(u"*{width:40px; height:40px;background:#4C25E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_73)

        self.pushButton_74 = QPushButton(self.frame_176)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setStyleSheet(u"*{width:40px; height:40px;background:#B525E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_74)

        self.pushButton_75 = QPushButton(self.frame_176)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setStyleSheet(u"*{width:40px; height:40px;background:#E8258E;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_72.addWidget(self.pushButton_75)

        self.pushButton_76 = QPushButton(self.frame_176)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setStyleSheet(u"*{width:40px; height:40px;background:#FFFFFF;color:#000000; border-radius:20;border:1px solid black;}")

        self.horizontalLayout_72.addWidget(self.pushButton_76)


        self.horizontalLayout_67.addWidget(self.frame_176, 0, Qt.AlignBottom)

        self.pushButton_77 = QPushButton(self.frame_175)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setMinimumSize(QSize(130, 55))
        self.pushButton_77.setFont(font20)
        self.pushButton_77.setStyleSheet(u"background-color:white; color:black;")

        self.horizontalLayout_67.addWidget(self.pushButton_77, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_110.addWidget(self.frame_175)

        self.frame_177 = QFrame(self.frame_111)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(-1, 0, -1, -1)
        self.painter_widget_4 = QWidget(self.frame_177)
        self.painter_widget_4.setObjectName(u"painter_widget_4")
        self.painter_widget_4.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.painter_widget_4.sizePolicy().hasHeightForWidth())
        self.painter_widget_4.setSizePolicy(sizePolicy2)
        self.painter_widget_4.setMinimumSize(QSize(0, 600))
        self.painter_widget_4.setStyleSheet(u"background-color:white;")

        self.horizontalLayout_89.addWidget(self.painter_widget_4)


        self.verticalLayout_110.addWidget(self.frame_177)

        self.frame_178 = QFrame(self.frame_111)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.pushButton_78 = QPushButton(self.frame_178)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setMinimumSize(QSize(170, 60))
        self.pushButton_78.setFont(font9)
        self.pushButton_78.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_78.setStyleSheet(u"background: #6522F2;\n"
"border-radius: 30px;")

        self.horizontalLayout_90.addWidget(self.pushButton_78, 0, Qt.AlignRight)


        self.verticalLayout_110.addWidget(self.frame_178, 0, Qt.AlignTop)


        self.verticalLayout_113.addWidget(self.frame_111)

        self.stackedPages2.addWidget(self.page_12)

        self.horizontalLayout_54.addWidget(self.stackedPages2)


        self.verticalLayout_31.addWidget(self.display2)


        self.horizontalLayout_31.addWidget(self.frame_51)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_toolBox.currentChanged.connect(MainWindow.changeMenu)
        self.pushButton_9.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_23.clicked.connect(MainWindow.backToChart)
        self.pushButton_7.clicked.connect(MainWindow.moveToSendMail)
        self.pushButton_8.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_4.clicked.connect(MainWindow.moveToReceivedMail)
        self.rightButton_19.clicked.connect(MainWindow.scroll_chart_right)
        self.leftButton_19.clicked.connect(MainWindow.scroll_chart_left)
        self.leftButton_13.clicked.connect(MainWindow.nextMemos)
        self.leftButton_11.clicked.connect(MainWindow.prevMemos)
        self.pushButton_65.clicked.connect(MainWindow.moveto_reply)
        self.pushButton_28.clicked.connect(MainWindow.colorChange1)
        self.pushButton_31.clicked.connect(MainWindow.colorChange2)
        self.pushButton_32.clicked.connect(MainWindow.colorChange3)
        self.pushButton_33.clicked.connect(MainWindow.colorChange4)
        self.pushButton_34.clicked.connect(MainWindow.colorChange5)
        self.pushButton_52.clicked.connect(MainWindow.colorChange6)
        self.pushButton_51.clicked.connect(MainWindow.colorChange7)
        self.pushButton_38.clicked.connect(MainWindow.colorChange8)
        self.pushButton_25.clicked.connect(MainWindow.colorChange9)
        self.pushButton_37.clicked.connect(MainWindow.painterClear)
        self.post1.clicked.connect(MainWindow.playMusic1_post)
        self.post2.clicked.connect(MainWindow.playMusic2_post)
        self.post3.clicked.connect(MainWindow.playMusic3_post)
        self.pushButton_15.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_12.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_30.clicked.connect(MainWindow.postMusic)
        self.pushButton.clicked.connect(MainWindow.moveToReceivedMail)
        self.pushButton_3.clicked.connect(MainWindow.moveToSendMail)
        self.pushButton_24.clicked.connect(MainWindow.login)
        self.pushButton_6.clicked.connect(MainWindow.reply)
        self.pushButton_53.clicked.connect(MainWindow.send_feedback)
        self.pushButton_13.clicked.connect(MainWindow.backToPosts)
        self.pushButton_14.clicked.connect(MainWindow.postMusic)
        self.pushButton_5.clicked.connect(MainWindow.searchMusic)
        self.pushButton_19.clicked.connect(MainWindow.moveto_reply)
        self.pushButton_36.clicked.connect(MainWindow.colorChange1)
        self.pushButton_39.clicked.connect(MainWindow.colorChange2)
        self.pushButton_41.clicked.connect(MainWindow.colorChange3)
        self.pushButton_42.clicked.connect(MainWindow.colorChange4)
        self.pushButton_43.clicked.connect(MainWindow.colorChange5)
        self.pushButton_54.clicked.connect(MainWindow.colorChange6)
        self.pushButton_55.clicked.connect(MainWindow.colorChange7)
        self.pushButton_44.clicked.connect(MainWindow.colorChange8)
        self.pushButton_26.clicked.connect(MainWindow.colorChange9)
        self.pushButton_45.clicked.connect(MainWindow.painterClear)
        self.pushButton_46.clicked.connect(MainWindow.colorChange1)
        self.pushButton_50.clicked.connect(MainWindow.colorChange2)
        self.pushButton_57.clicked.connect(MainWindow.colorChange3)
        self.pushButton_58.clicked.connect(MainWindow.colorChange4)
        self.pushButton_59.clicked.connect(MainWindow.colorChange5)
        self.pushButton_60.clicked.connect(MainWindow.colorChange6)
        self.pushButton_61.clicked.connect(MainWindow.colorChange7)
        self.pushButton_62.clicked.connect(MainWindow.colorChange8)
        self.pushButton_27.clicked.connect(MainWindow.colorChange9)
        self.pushButton_63.clicked.connect(MainWindow.painterClear)
        self.pushButton_68.clicked.connect(MainWindow.colorChange1)
        self.pushButton_69.clicked.connect(MainWindow.colorChange2)
        self.pushButton_70.clicked.connect(MainWindow.colorChange3)
        self.pushButton_71.clicked.connect(MainWindow.colorChange4)
        self.pushButton_72.clicked.connect(MainWindow.colorChange5)
        self.pushButton_73.clicked.connect(MainWindow.colorChange6)
        self.pushButton_74.clicked.connect(MainWindow.colorChange7)
        self.pushButton_75.clicked.connect(MainWindow.colorChange8)
        self.pushButton_76.clicked.connect(MainWindow.colorChange9)
        self.pushButton_77.clicked.connect(MainWindow.painterClear)
        self.chart_img_Button1.clicked.connect(MainWindow.playMusic1_chart)
        self.chart_img_Button2.clicked.connect(MainWindow.playMusic2_chart)
        self.chart_img_Button3.clicked.connect(MainWindow.playMusic3_chart)
        self.chart_img_Button4.clicked.connect(MainWindow.playMusic4_chart)
        self.chart_img_Button5.clicked.connect(MainWindow.playMusic5_chart)
        self.chart_img_Button6.clicked.connect(MainWindow.playMusic6_chart)
        self.chart_img_Button7.clicked.connect(MainWindow.playMusic7_chart)
        self.chart_img_Button8.clicked.connect(MainWindow.playMusic8_chart)
        self.chart_img_Button9.clicked.connect(MainWindow.playMusic9_chart)
        self.chart_img_Button10.clicked.connect(MainWindow.playMusic10_chart)
        self.pushButton_8.clicked.connect(MainWindow.input_code)
        self.pushButton_12.clicked.connect(MainWindow.change_volume)
        self.pushButton_78.clicked.connect(MainWindow.save_postcard)
        self.pushButton_64.clicked.connect(MainWindow.post_manito)
        self.pushButton_56.clicked.connect(MainWindow.backToChart)
        self.emoji_button1.clicked.connect(MainWindow.press_emoji1)
        self.emoji_button2.clicked.connect(MainWindow.press_emoji2)
        self.emoji_button3.clicked.connect(MainWindow.press_emoji3)
        self.emoji_button4.clicked.connect(MainWindow.press_emoji4)
        self.verticalSlider_29.valueChanged.connect(MainWindow.change_volume)
        self.pushButton_35.clicked.connect(MainWindow.show_volume_chart)
        self.pushButton_47.clicked.connect(MainWindow.show_volume_song)
        self.pushButton_2.clicked.connect(MainWindow.show_volume_manito)
        self.pushButton_10.clicked.connect(MainWindow.show_volume_post)
        self.pushButton_11.clicked.connect(MainWindow.show_volume_received)
        self.pushButton_17.clicked.connect(MainWindow.show_volume_send)
        self.pushButton_98.clicked.connect(MainWindow.pause)
        self.pushButton_102.clicked.connect(MainWindow.pause)
        self.pushButton_101.clicked.connect(MainWindow.pause)
        self.pushButton_99.clicked.connect(MainWindow.pause)
        self.pushButton_18.clicked.connect(MainWindow.logout)
        self.post4.clicked.connect(MainWindow.playMusic4_post)
        self.post5.clicked.connect(MainWindow.playMusic5_post)
        self.post10.clicked.connect(MainWindow.playMusic10_post)
        self.post9.clicked.connect(MainWindow.playMusic9_post)
        self.post8.clicked.connect(MainWindow.playMusic8_post)
        self.post6.clicked.connect(MainWindow.playMusic6_post)
        self.post7.clicked.connect(MainWindow.playMusic7_post)
        self.leftButton_14.pressed.connect(MainWindow.scroll_post_left)
        self.rightButton_14.pressed.connect(MainWindow.scroll_post_right)
        self.priorityBox.currentIndexChanged.connect(MainWindow.align_chart)
        self.verticalSlider_33.valueChanged.connect(MainWindow.change_volume)
        self.verticalSlider_32.valueChanged.connect(MainWindow.change_volume)
        self.verticalSlider_30.valueChanged.connect(MainWindow.change_volume)
        self.pushButton_79.clicked.connect(MainWindow.search_song)
        self.pushButton_21.clicked.connect(MainWindow.search_singer)
        self.pushButton_67.clicked.connect(MainWindow.search_song)
        self.pushButton_22.clicked.connect(MainWindow.search_song)
        self.verticalSlider_27.valueChanged.connect(MainWindow.change_volume)

        self.menu_toolBox.setCurrentIndex(1)
        self.menu_toolBox.layout().setSpacing(30)
        self.pushButton_29.setDefault(False)
        self.stackedPages.setCurrentIndex(4)
        self.priorityBox.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Name_4.setText(QCoreApplication.translate("MainWindow", u"Audi:ro", None))
        self.menu_toolBox.setItemText(self.menu_toolBox.indexOf(self.menuPage1), QCoreApplication.translate("MainWindow", u"   \uba40\ucea0:\ub85c\uc758 \uc778\uae30\ucc28\ud2b8", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \ucd94\ucc9c\ud558\uae30", None))
        self.menu_toolBox.setItemText(self.menu_toolBox.indexOf(self.menuPage2), QCoreApplication.translate("MainWindow", u"   \uc74c\uc545 \uc120\ubb3c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ud655\uc778\ud558\uae30", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30", None))
        self.menu_toolBox.setItemText(self.menu_toolBox.indexOf(self.menuPage3), QCoreApplication.translate("MainWindow", u"   \ud3b8\uc9c0\ud568", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc544\uc6c3", None))
        self.tag1.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\uadfc", None))
        self.tag2.setText(QCoreApplication.translate("MainWindow", u"\ud1f4\uadfc", None))
        self.tag3.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\ub0a8", None))
        self.tag4.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\uc6b8", None))
        self.tag5.setText(QCoreApplication.translate("MainWindow", u"\uc6b4\ub3d9", None))
        self.tag6.setText(QCoreApplication.translate("MainWindow", u"\ud734\uc2dd", None))
        self.priorityBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\ucd94\ucc9c\uc21c", None))
        self.priorityBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\ucd5c\uc2e0\uc21c", None))
        self.priorityBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc154\ud50c", None))

        self.leftButton_19.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.chart_img_Button1.setText("")
        self.chart_img_Button2.setText("")
        self.chart_img_Button3.setText("")
        self.chart_img_Button4.setText("")
        self.chart_img_Button5.setText("")
        self.chart_img_Button6.setText("")
        self.chart_img_Button7.setText("")
        self.chart_img_Button8.setText("")
        self.chart_img_Button9.setText("")
        self.chart_img_Button10.setText("")
        self.rightButton_19.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_100.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_Title_5.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_102.setText("")
        self.song_liked.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_Artist_3.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_35.setText("")
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.leftButton_11.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.music_post4.setText("")
        self.music_post1.setText("")
        self.music_post3.setText("")
        self.music_post6.setText("")
        self.music_post2.setText("")
        self.music_post5.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.leftButton_13.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_104.setText("")
        self.song_gift_cnt.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.song_title.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_106.setText("")
        self.song_liked_cnt.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.song_singer.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.song_play_time.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.song_full_time.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_47.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_14.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.post1.setText(QCoreApplication.translate("MainWindow", u"DItto \ucd94\ucc9c", None))
        self.post6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post5.setText(QCoreApplication.translate("MainWindow", u"Love Dive \ucd94\ucc9c", None))
        self.post7.setText(QCoreApplication.translate("MainWindow", u"Love Dive \ucd94\ucc9c", None))
        self.post4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post2.setText(QCoreApplication.translate("MainWindow", u"Hype Boy \ucd94\ucc9c", None))
        self.post3.setText(QCoreApplication.translate("MainWindow", u"Love Dive \ucd94\ucc9c", None))
        self.post8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_14.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.emoji_button2.setText("")
        self.count_emoji1.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.count_emoji4.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.count_emoji2.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.count_emoji3.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.emoji_button4.setText("")
        self.emoji_button3.setText("")
        self.emoji_button1.setText("")
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.gift_detail_img.setText("")
        self.pushButton_98.setText("")
        self.gift_detail_song.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.gift_detail_singer.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_2.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc644\ub8cc", None))
        self.lineEdit_gift_song.setText("")
        self.lineEdit_gift_song.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.pushButton_79.setText("")
        self.radio_label_gift_song.setText(QCoreApplication.translate("MainWindow", u"di", None))
        self.radioButton_gift_song.setText(QCoreApplication.translate("MainWindow", u"\ub274", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\ub178\ub798 \uc81c\ubaa9\uc73c\ub85c \uac80\uc0c9", None))
        self.lineEdit_gift_singer.setText("")
        self.lineEdit_gift_singer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.pushButton_21.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_gift_singer3.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_gift_singer4.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_gift_singer2.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_gift_singer1.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_gift_singer1_3.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_gift_singer1_4.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_gift_singer1_5.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_gift_singer1_6.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\uac00\uc218 \uc774\ub984\uc73c\ub85c \uac80\uc0c9", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"ditto \uc568\ubc94 \ucee4\ubc84", None))
        self.pushButton_102.setText("")
        self.gift_detail_song_2.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.gift_detail_singer_2.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_10.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ud655\uc778\ud558\uae30", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30", None))
        self.label_21.setText("")
        self.label_46.setText("")
        self.label_24.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubb38\uc790\ub85c \ubc1b\uc740 \uc778\uc99d \ucf54\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"  \ud655\uc778", None))
        self.postcard_detail_img.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ub0b4\uc6a9                                                   (\ub2e4\ub978 \uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \uc791\uc131\ud55c \uc5fd\uc11c)", None))
        self.pushButton_101.setText("")
        self.gift_detail_song_3.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.gift_detail_singer_3.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_11.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30\ub97c \uc6d0\ud558\uc2dc\uba74 \ub85c\uadf8\uc778\uc744 \ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1\ub2e8\uacc4. \ud3b8\uc9c0\uc5d0 \ucca8\ubd80\ud560 \ub178\ub798\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc644\ub8cc", None))
        self.lineEdit_postcard_song.setText("")
        self.lineEdit_postcard_song.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.pushButton_22.setText("")
        self.radioButton_postcard_song1.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_postcard_song2.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_postcard_song3.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_postcard_song4.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radio_label_postcard_song1.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radio_label_postcard_song2.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radio_label_postcard_song3.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radio_label_postcard_song4.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\ub178\ub798 \uc81c\ubaa9\uc73c\ub85c \uac80\uc0c9", None))
        self.lineEdit_postcard_singer.setText("")
        self.lineEdit_postcard_singer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.pushButton_67.setText("")
        self.radioButton_postcard_singer1.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_postcard_singer2.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_postcard_singer3.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radioButton_postcard_singer4.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.radio_label_postcard_singer1.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radio_label_postcard_singer2.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radio_label_postcard_singer3.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radio_label_postcard_singer4.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uac00\uc218 \uc774\ub984\uc73c\ub85c \uac80\uc0c9", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"2\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \uc791\uc131\ud574 \uc8fc\uc138\uc694.", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ditto \uc568\ubc94 \ucee4\ubc84", None))
        self.pushButton_99.setText("")
        self.gift_detail_song_4.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.gift_detail_singer_4.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_17.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"3\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \ubcf4\ub0bc \uc0ac\ub78c\uc758 \uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694.", None))
        self.label_31.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.(-\ub294 \ube7c\uace0 \uc785\ub825\ud574\uc8fc\uc138\uc694)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\uc778\uc99d \ucf54\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.(\ud2b9\uc218\ubb38\uc790\ub294 \ube7c\uace0 \uc785\ub825\ud574\uc8fc\uc138\uc694.)", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"  \ud655\uc778", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc911\ud55c \ud3b8\uc9c0\uac00 \uc798 \uc804\ub2ec\ub418\uc5c8\uc2b5\ub2c8\ub2e4!", None))
        self.pushButton_28.setText("")
        self.pushButton_31.setText("")
        self.pushButton_32.setText("")
        self.pushButton_33.setText("")
        self.pushButton_34.setText("")
        self.pushButton_52.setText("")
        self.pushButton_51.setText("")
        self.pushButton_38.setText("")
        self.pushButton_25.setText("")
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc9c0\uc6b0\uae30", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\ub098\uc5d0\uac8c \uc88b\uc740 \uc74c\uc545\uc744 \ucd94\ucc9c\ud574\uc900 \uc0ac\ub78c\uc5d0\uac8c \uace0\ub9c8\uc6b4 \ub9c8\uc74c\uc744 \uc804\ud569\ub2c8\ub2e4.", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \uc120\ud0dd\ud55c \ud6c4, \uc774 \uc74c\uc545\uc744 \ub4e4\uc744 \ub204\uad70\uac00\ub97c \uc704\ud574 \ucd94\ucc9c\ud558\ub294 \uc5fd\uc11c\ub97c \uadf8\ub9bd\ub2c8\ub2e4.", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \uac80\uc0c9\ud558\uae30", None))
        self.pushButton_5.setText("")
        self.label_27.setText("")
        self.label_5.setText("")
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778", None))
        self.label_2.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30\uc640 \ub178\ub798\ucd94\ucc9c\ud558\uae30\ub294 \ub85c\uadf8\uc778 \ud6c4 \uc774\uc6a9 \uac00\ub2a5\ud569\ub2c8\ub2e4. \uc0c1\ub2e8 QR\ub85c \uc774\ub3d9\ud558\uc5ec \ub85c\uadf8\uc778 \ud68c\uc6d0\uac00\uc785\uc744 \uc9c4\ud589\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.label_32.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \ucd94\ucc9c\ud558\uae30", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ud558\uae30", None))
        self.label_33.setText("")
        self.sent_postcard_image.setText("")
        self.pushButton_36.setText("")
        self.pushButton_39.setText("")
        self.pushButton_41.setText("")
        self.pushButton_42.setText("")
        self.pushButton_43.setText("")
        self.pushButton_54.setText("")
        self.pushButton_55.setText("")
        self.pushButton_44.setText("")
        self.pushButton_26.setText("")
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc9c0\uc6b0\uae30", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\ub178\ub798\ub97c \ub4e3\uace0 \ub290\ub080 \uac10\uc815 \ud639\uc740 \uae30\ubd84\uc744 \ud45c\ud604\ud569\ub2c8\ub2e4.", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ditto - New Jeans", None))
        self.pushButton_46.setText("")
        self.pushButton_50.setText("")
        self.pushButton_57.setText("")
        self.pushButton_58.setText("")
        self.pushButton_59.setText("")
        self.pushButton_60.setText("")
        self.pushButton_61.setText("")
        self.pushButton_62.setText("")
        self.pushButton_27.setText("")
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc9c0\uc6b0\uae30", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\ub178\ub798\ub97c \ucd94\ucc9c\ud558\ub294 \uc5fd\uc11c\ub97c \uc791\uc131\ud569\ub2c8\ub2e4. \uc774 \uc5fd\uc11c\ub294 \uc74c\uc545 \uc120\ubb3c \ud398\uc774\uc9c0\uc5d0 \ub178\ucd9c\ub429\ub2c8\ub2e4.", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"\ub178\ub798 \ucd94\ucc9c\ud558\uae30", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Ditto - New Jeans", None))
        self.pushButton_68.setText("")
        self.pushButton_69.setText("")
        self.pushButton_70.setText("")
        self.pushButton_71.setText("")
        self.pushButton_72.setText("")
        self.pushButton_73.setText("")
        self.pushButton_74.setText("")
        self.pushButton_75.setText("")
        self.pushButton_76.setText("")
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc9c0\uc6b0\uae30", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc74c\uc73c\ub85c", None))
    # retranslateUi

