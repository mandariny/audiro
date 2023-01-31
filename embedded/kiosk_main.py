# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kiosk_main.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSlider, QStackedWidget, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)

import painter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 1200)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(800, 1200))
        self.centralwidget.setStyleSheet(u"background-color:#000000; color:#ffffff;")
        self.horizontalLayout_31 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_51 = QFrame(self.centralwidget)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(800, 1200))
        self.frame_51.setMaximumSize(QSize(800, 1200))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_51)
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.display1 = QFrame(self.frame_51)
        self.display1.setObjectName(u"display1")
        self.display1.setMaximumSize(QSize(800, 590))
        self.display1.setFrameShape(QFrame.StyledPanel)
        self.display1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.display1)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QFrame(self.display1)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(200, 0))
        self.menu_bar.setMaximumSize(QSize(200, 16777215))
        self.menu_bar.setFrameShape(QFrame.StyledPanel)
        self.menu_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.menu_bar)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.menu_bar)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 300))
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
        self.label_Name_4 = QLabel(self.frame_150)
        self.label_Name_4.setObjectName(u"label_Name_4")
        font = QFont()
        font.setPointSize(15)
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
        self.menu_toolBox.setFocusPolicy(Qt.NoFocus)
        self.menu_toolBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.menu_toolBox.setAcceptDrops(False)
        self.menu_toolBox.setStyleSheet(u"/*border:none;border-radius: 15px;\\n  color: #ffffff;\\n  background-color: #6522f2;*/\n"
"\n"
"QToolBox{\n"
"text-allgin:left;\n"
"}\n"
"QToolBox::tab{\n"
"border-radius:20px;\n"
"text-allgin:left;\n"
"}")
        self.menu_toolBox.setInputMethodHints(Qt.ImhNone)
        self.menu_toolBox.setLineWidth(1)
        self.menuPage1 = QWidget()
        self.menuPage1.setObjectName(u"menuPage1")
        self.menuPage1.setGeometry(QRect(0, 0, 194, 150))
        self.verticalLayout_26 = QVBoxLayout(self.menuPage1)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.menu_toolBox.addItem(self.menuPage1, u"\uba40\ucea0:\ub85c\uc758 \uc778\uae30\ucc28\ud2b8")
        self.menuPage2 = QWidget()
        self.menuPage2.setObjectName(u"menuPage2")
        self.menuPage2.setGeometry(QRect(0, 0, 194, 150))
        self.verticalLayout_107 = QVBoxLayout(self.menuPage2)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.frame_119 = QFrame(self.menuPage2)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMaximumSize(QSize(16777211, 16777215))
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_119)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_29 = QPushButton(self.frame_119)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setStyleSheet(u"text-align:left;")

        self.verticalLayout_8.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.frame_119)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"text-align:left;")

        self.verticalLayout_8.addWidget(self.pushButton_30)


        self.verticalLayout_107.addWidget(self.frame_119, 0, Qt.AlignTop)

        self.menu_toolBox.addItem(self.menuPage2, u"\uc74c\uc545 \uc120\ubb3c")
        self.menuPage3 = QWidget()
        self.menuPage3.setObjectName(u"menuPage3")
        self.menuPage3.setGeometry(QRect(0, 0, 194, 150))
        self.verticalLayout_4 = QVBoxLayout(self.menuPage3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_120 = QFrame(self.menuPage3)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_120)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_120)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"text-align:left;")

        self.verticalLayout_12.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_120)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"text-align:left;")

        self.verticalLayout_12.addWidget(self.pushButton_3, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_120, 0, Qt.AlignTop)

        self.menu_toolBox.addItem(self.menuPage3, u"\ud3b8\uc9c0\ud568")

        self.verticalLayout_106.addWidget(self.menu_toolBox)


        self.verticalLayout_105.addWidget(self.frame_151)


        self.verticalLayout_25.addWidget(self.frame_38)

        self.frame_152 = QFrame(self.menu_bar)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.frame_67 = QFrame(self.frame_152)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setGeometry(QRect(160, 290, 736, 414))
        self.frame_67.setMinimumSize(QSize(0, 400))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(500, 0))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.pushButton_66 = QPushButton(self.frame_68)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setGeometry(QRect(140, 130, 211, 101))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.pushButton_66.setFont(font1)

        self.horizontalLayout_42.addWidget(self.frame_68)

        self.label_54 = QLabel(self.frame_67)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(200, 16777215))
        self.label_54.setPixmap(QPixmap(u"lp.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_54)

        self.stackedPages_2 = QStackedWidget(self.frame_152)
        self.stackedPages_2.setObjectName(u"stackedPages_2")
        self.stackedPages_2.setGeometry(QRect(180, 160, 580, 598))
        self.stackedPages_2.setMaximumSize(QSize(580, 600))
        self.page1_2 = QWidget()
        self.page1_2.setObjectName(u"page1_2")
        self.verticalLayout_15 = QVBoxLayout(self.page1_2)
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.page1_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Tags_2 = QFrame(self.frame_20)
        self.Tags_2.setObjectName(u"Tags_2")
        self.Tags_2.setMinimumSize(QSize(0, 50))
        self.Tags_2.setMaximumSize(QSize(16777215, 50))
        self.Tags_2.setFrameShape(QFrame.StyledPanel)
        self.Tags_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Tags_2)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tag1_2 = QPushButton(self.Tags_2)
        self.tag1_2.setObjectName(u"tag1_2")

        self.horizontalLayout_10.addWidget(self.tag1_2)

        self.tag2_2 = QPushButton(self.Tags_2)
        self.tag2_2.setObjectName(u"tag2_2")

        self.horizontalLayout_10.addWidget(self.tag2_2)

        self.tag3_2 = QPushButton(self.Tags_2)
        self.tag3_2.setObjectName(u"tag3_2")

        self.horizontalLayout_10.addWidget(self.tag3_2)

        self.tag4_2 = QPushButton(self.Tags_2)
        self.tag4_2.setObjectName(u"tag4_2")

        self.horizontalLayout_10.addWidget(self.tag4_2)

        self.tag5_2 = QPushButton(self.Tags_2)
        self.tag5_2.setObjectName(u"tag5_2")

        self.horizontalLayout_10.addWidget(self.tag5_2)

        self.tag6_2 = QPushButton(self.Tags_2)
        self.tag6_2.setObjectName(u"tag6_2")

        self.horizontalLayout_10.addWidget(self.tag6_2)


        self.verticalLayout_27.addWidget(self.Tags_2)

        self.frame_29 = QFrame(self.frame_20)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 30))
        self.frame_29.setMaximumSize(QSize(16777215, 30))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.priorityBox_2 = QComboBox(self.frame_29)
        self.priorityBox_2.addItem("")
        self.priorityBox_2.addItem("")
        self.priorityBox_2.addItem("")
        self.priorityBox_2.setObjectName(u"priorityBox_2")
        self.priorityBox_2.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.priorityBox_2.setFont(font2)

        self.horizontalLayout_15.addWidget(self.priorityBox_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.full_listBox_2 = QPushButton(self.frame_29)
        self.full_listBox_2.setObjectName(u"full_listBox_2")
        self.full_listBox_2.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_15.addWidget(self.full_listBox_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.frame_29)

        self.frame_37 = QFrame(self.frame_20)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_221 = QFrame(self.frame_37)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setMinimumSize(QSize(30, 0))
        self.frame_221.setMaximumSize(QSize(50, 16777215))
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_221)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.leftButton_20 = QPushButton(self.frame_221)
        self.leftButton_20.setObjectName(u"leftButton_20")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.leftButton_20.setFont(font3)
        self.leftButton_20.setStyleSheet(u"")

        self.verticalLayout_156.addWidget(self.leftButton_20)


        self.horizontalLayout_16.addWidget(self.frame_221)

        self.pushButton_41 = QPushButton(self.frame_37)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(200, 150))
        self.pushButton_41.setIconSize(QSize(100, 100))

        self.horizontalLayout_16.addWidget(self.pushButton_41)

        self.frame_232 = QFrame(self.frame_37)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setMinimumSize(QSize(30, 0))
        self.frame_232.setMaximumSize(QSize(50, 16777215))
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_232)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.rightButton_20 = QPushButton(self.frame_232)
        self.rightButton_20.setObjectName(u"rightButton_20")
        self.rightButton_20.setFont(font3)
        self.rightButton_20.setStyleSheet(u"")

        self.horizontalLayout_83.addWidget(self.rightButton_20)


        self.horizontalLayout_16.addWidget(self.frame_232)


        self.verticalLayout_27.addWidget(self.frame_37)

        self.frame_47 = QFrame(self.frame_20)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(500, 0))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_48)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(30, 0, 0, 0)
        self.frame_233 = QFrame(self.frame_48)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_233)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_13 = QLabel(self.frame_233)
        self.label_Likes_13.setObjectName(u"label_Likes_13")

        self.horizontalLayout_84.addWidget(self.label_Likes_13)

        self.label_Title_8 = QLabel(self.frame_233)
        self.label_Title_8.setObjectName(u"label_Title_8")
        font4 = QFont()
        font4.setPointSize(23)
        font4.setBold(True)
        self.label_Title_8.setFont(font4)
        self.label_Title_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_84.addWidget(self.label_Title_8)

        self.label_Likes_14 = QLabel(self.frame_233)
        self.label_Likes_14.setObjectName(u"label_Likes_14")

        self.horizontalLayout_84.addWidget(self.label_Likes_14, 0, Qt.AlignRight)


        self.verticalLayout_40.addWidget(self.frame_233)

        self.label_Artist_5 = QLabel(self.frame_48)
        self.label_Artist_5.setObjectName(u"label_Artist_5")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.label_Artist_5.setFont(font5)
        self.label_Artist_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_Artist_5)

        self.frame_234 = QFrame(self.frame_48)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_234)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_188 = QLabel(self.frame_234)
        self.label_188.setObjectName(u"label_188")

        self.horizontalLayout_86.addWidget(self.label_188, 0, Qt.AlignLeft)

        self.horizontalSlider_19 = QSlider(self.frame_234)
        self.horizontalSlider_19.setObjectName(u"horizontalSlider_19")
        self.horizontalSlider_19.setValue(25)
        self.horizontalSlider_19.setSliderPosition(25)
        self.horizontalSlider_19.setOrientation(Qt.Horizontal)

        self.horizontalLayout_86.addWidget(self.horizontalSlider_19)

        self.label_190 = QLabel(self.frame_234)
        self.label_190.setObjectName(u"label_190")

        self.horizontalLayout_86.addWidget(self.label_190, 0, Qt.AlignRight)


        self.verticalLayout_40.addWidget(self.frame_234)


        self.horizontalLayout_18.addWidget(self.frame_48)

        self.frame_54 = QFrame(self.frame_47)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(50, 0))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_54)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalSlider_19 = QSlider(self.frame_54)
        self.verticalSlider_19.setObjectName(u"verticalSlider_19")
        self.verticalSlider_19.setValue(40)
        self.verticalSlider_19.setOrientation(Qt.Vertical)

        self.verticalLayout_42.addWidget(self.verticalSlider_19, 0, Qt.AlignHCenter)

        self.pushButton_42 = QPushButton(self.frame_54)
        self.pushButton_42.setObjectName(u"pushButton_42")

        self.verticalLayout_42.addWidget(self.pushButton_42, 0, Qt.AlignHCenter)


        self.horizontalLayout_18.addWidget(self.frame_54)


        self.verticalLayout_27.addWidget(self.frame_47)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.stackedPages_2.addWidget(self.page1_2)
        self.page2_2 = QWidget()
        self.page2_2.setObjectName(u"page2_2")
        self.verticalLayout_43 = QVBoxLayout(self.page2_2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_239 = QFrame(self.page2_2)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setMaximumSize(QSize(16777215, 30))
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_239)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 50, 0)
        self.pushButton_43 = QPushButton(self.frame_239)
        self.pushButton_43.setObjectName(u"pushButton_43")

        self.horizontalLayout_88.addWidget(self.pushButton_43, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_43.addWidget(self.frame_239)

        self.frame_69 = QFrame(self.page2_2)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_240 = QFrame(self.frame_69)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setMinimumSize(QSize(30, 0))
        self.frame_240.setMaximumSize(QSize(30, 16777215))
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_240)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.frame_240)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.verticalLayout_44.addWidget(self.frame_70)

        self.leftButton_12 = QPushButton(self.frame_240)
        self.leftButton_12.setObjectName(u"leftButton_12")
        self.leftButton_12.setFont(font3)
        self.leftButton_12.setStyleSheet(u"")

        self.verticalLayout_44.addWidget(self.leftButton_12)

        self.frame_71 = QFrame(self.frame_240)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 300))
        self.frame_71.setMaximumSize(QSize(16777215, 500))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.verticalLayout_44.addWidget(self.frame_71)


        self.horizontalLayout_29.addWidget(self.frame_240)

        self.frame_72 = QFrame(self.frame_69)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(480, 0))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_72)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_5 = QStackedWidget(self.frame_72)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setMinimumSize(QSize(450, 0))
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_43 = QHBoxLayout(self.page_12)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setSpacing(10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.page_12)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMaximumSize(QSize(120, 120))
        self.label_117.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_117.setPixmap(QPixmap(u"post2.jpg"))
        self.label_117.setScaledContents(True)
        self.label_117.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_117, 0, 1, 1, 1)

        self.label_118 = QLabel(self.page_12)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMaximumSize(QSize(120, 120))
        self.label_118.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_118.setPixmap(QPixmap(u"post4.jpg"))
        self.label_118.setScaledContents(True)
        self.label_118.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_118, 1, 0, 1, 1)

        self.label_119 = QLabel(self.page_12)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMaximumSize(QSize(120, 120))
        self.label_119.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_119.setPixmap(QPixmap(u"post5.jpg"))
        self.label_119.setScaledContents(True)
        self.label_119.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_119, 1, 1, 1, 1)

        self.label_120 = QLabel(self.page_12)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMaximumSize(QSize(120, 120))
        self.label_120.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_120.setPixmap(QPixmap(u"post6.jpg"))
        self.label_120.setScaledContents(True)
        self.label_120.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_120, 1, 2, 1, 1)

        self.label_121 = QLabel(self.page_12)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMaximumSize(QSize(120, 120))
        self.label_121.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_121.setPixmap(QPixmap(u"post3.jpg"))
        self.label_121.setScaledContents(True)
        self.label_121.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_121, 0, 2, 1, 1)

        self.label_122 = QLabel(self.page_12)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMaximumSize(QSize(120, 120))
        self.label_122.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_122.setPixmap(QPixmap(u"post1.jpg"))
        self.label_122.setScaledContents(True)
        self.label_122.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_122, 0, 0, 1, 1)


        self.horizontalLayout_43.addLayout(self.gridLayout_12)

        self.stackedWidget_5.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.horizontalLayout_44 = QHBoxLayout(self.page_13)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setSpacing(10)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 10, 0, 10)
        self.label_136 = QLabel(self.page_13)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMaximumSize(QSize(120, 120))
        self.label_136.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_136.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_136, 1, 1, 1, 1)

        self.label_137 = QLabel(self.page_13)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMaximumSize(QSize(120, 120))
        self.label_137.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_137.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_137, 0, 1, 1, 1)

        self.label_138 = QLabel(self.page_13)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMaximumSize(QSize(120, 120))
        self.label_138.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_138, 1, 0, 1, 1)

        self.label_139 = QLabel(self.page_13)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMaximumSize(QSize(120, 120))
        self.label_139.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_139, 0, 0, 1, 1)

        self.label_141 = QLabel(self.page_13)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMaximumSize(QSize(120, 120))
        self.label_141.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_141.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_141, 0, 2, 1, 1)

        self.label_142 = QLabel(self.page_13)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMaximumSize(QSize(120, 120))
        self.label_142.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_142.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_142, 1, 2, 1, 1)


        self.horizontalLayout_44.addLayout(self.gridLayout_22)

        self.stackedWidget_5.addWidget(self.page_13)

        self.verticalLayout_45.addWidget(self.stackedWidget_5)

        self.frame_138 = QFrame(self.frame_72)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMaximumSize(QSize(16777215, 100))
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_139 = QFrame(self.frame_138)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_139)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_249 = QFrame(self.frame_139)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_249)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_21 = QLabel(self.frame_249)
        self.label_Likes_21.setObjectName(u"label_Likes_21")

        self.horizontalLayout_93.addWidget(self.label_Likes_21)

        self.label_Title_11 = QLabel(self.frame_249)
        self.label_Title_11.setObjectName(u"label_Title_11")
        self.label_Title_11.setFont(font4)
        self.label_Title_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_93.addWidget(self.label_Title_11)

        self.label_Likes_22 = QLabel(self.frame_249)
        self.label_Likes_22.setObjectName(u"label_Likes_22")

        self.horizontalLayout_93.addWidget(self.label_Likes_22, 0, Qt.AlignRight)


        self.verticalLayout_98.addWidget(self.frame_249)

        self.label_Artist_9 = QLabel(self.frame_139)
        self.label_Artist_9.setObjectName(u"label_Artist_9")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.label_Artist_9.setFont(font6)
        self.label_Artist_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.label_Artist_9)

        self.frame_250 = QFrame(self.frame_139)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_250)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_196 = QLabel(self.frame_250)
        self.label_196.setObjectName(u"label_196")

        self.horizontalLayout_94.addWidget(self.label_196, 0, Qt.AlignLeft)

        self.horizontalSlider_23 = QSlider(self.frame_250)
        self.horizontalSlider_23.setObjectName(u"horizontalSlider_23")
        self.horizontalSlider_23.setValue(25)
        self.horizontalSlider_23.setSliderPosition(25)
        self.horizontalSlider_23.setOrientation(Qt.Horizontal)

        self.horizontalLayout_94.addWidget(self.horizontalSlider_23)

        self.label_197 = QLabel(self.frame_250)
        self.label_197.setObjectName(u"label_197")

        self.horizontalLayout_94.addWidget(self.label_197, 0, Qt.AlignRight)


        self.verticalLayout_98.addWidget(self.frame_250)


        self.horizontalLayout_50.addWidget(self.frame_139)


        self.verticalLayout_45.addWidget(self.frame_138)


        self.horizontalLayout_29.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_69)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(30, 0))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_73)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMaximumSize(QSize(16777215, 183))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_74)

        self.rightButton_12 = QPushButton(self.frame_73)
        self.rightButton_12.setObjectName(u"rightButton_12")
        self.rightButton_12.setFont(font3)
        self.rightButton_12.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.rightButton_12, 0, Qt.AlignHCenter)

        self.verticalSlider_22 = QSlider(self.frame_73)
        self.verticalSlider_22.setObjectName(u"verticalSlider_22")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_22.sizePolicy().hasHeightForWidth())
        self.verticalSlider_22.setSizePolicy(sizePolicy)
        self.verticalSlider_22.setValue(40)
        self.verticalSlider_22.setOrientation(Qt.Vertical)

        self.verticalLayout_46.addWidget(self.verticalSlider_22, 0, Qt.AlignHCenter)

        self.pushButton_48 = QPushButton(self.frame_73)
        self.pushButton_48.setObjectName(u"pushButton_48")

        self.verticalLayout_46.addWidget(self.pushButton_48, 0, Qt.AlignHCenter)


        self.horizontalLayout_29.addWidget(self.frame_73)


        self.verticalLayout_43.addWidget(self.frame_69)

        self.stackedPages_2.addWidget(self.page2_2)
        self.page3_2 = QWidget()
        self.page3_2.setObjectName(u"page3_2")
        self.horizontalLayout_36 = QHBoxLayout(self.page3_2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_6 = QStackedWidget(self.page3_2)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_47 = QVBoxLayout(self.page_6)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_75 = QFrame(self.page_6)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_75)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_143 = QLabel(self.frame_76)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMaximumSize(QSize(300, 70))
        self.label_143.setFont(font6)
        self.label_143.setStyleSheet(u"*{\n"
"  padding: 0px 10px 0 10px;\n"
"  border-radius: 33px;\n"
"  background-color: #6522f2;\n"
"color: #FFFFFF;\n"
"}")
        self.label_143.setFrameShape(QFrame.Box)
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_143)


        self.verticalLayout_48.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_75)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 450))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_158 = QFrame(self.frame_77)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(50, 0))
        self.frame_158.setMaximumSize(QSize(50, 16777215))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_158)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.leftButton_17 = QPushButton(self.frame_158)
        self.leftButton_17.setObjectName(u"leftButton_17")
        self.leftButton_17.setFont(font3)
        self.leftButton_17.setStyleSheet(u"")

        self.verticalLayout_49.addWidget(self.leftButton_17)


        self.horizontalLayout_56.addWidget(self.frame_158)

        self.verticalLayout_115 = QVBoxLayout()
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setSpacing(10)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.post2_2 = QPushButton(self.frame_77)
        self.post2_2.setObjectName(u"post2_2")
        self.post2_2.setMinimumSize(QSize(0, 100))
        self.post2_2.setIconSize(QSize(20, 20))

        self.gridLayout_16.addWidget(self.post2_2, 0, 1, 1, 1)

        self.post1_2 = QPushButton(self.frame_77)
        self.post1_2.setObjectName(u"post1_2")
        self.post1_2.setMinimumSize(QSize(0, 100))
        self.post1_2.setIconSize(QSize(20, 20))

        self.gridLayout_16.addWidget(self.post1_2, 0, 0, 1, 1)

        self.post3_2 = QPushButton(self.frame_77)
        self.post3_2.setObjectName(u"post3_2")
        self.post3_2.setMinimumSize(QSize(0, 100))
        self.post3_2.setIconSize(QSize(20, 20))

        self.gridLayout_16.addWidget(self.post3_2, 0, 2, 1, 1)

        self.post5_2 = QPushButton(self.frame_77)
        self.post5_2.setObjectName(u"post5_2")
        self.post5_2.setMinimumSize(QSize(0, 100))
        self.post5_2.setIconSize(QSize(20, 20))

        self.gridLayout_16.addWidget(self.post5_2, 1, 1, 1, 1)

        self.post4_2 = QPushButton(self.frame_77)
        self.post4_2.setObjectName(u"post4_2")
        self.post4_2.setMinimumSize(QSize(0, 100))
        self.post4_2.setIconSize(QSize(20, 20))

        self.gridLayout_16.addWidget(self.post4_2, 1, 0, 1, 1)

        self.post6_2 = QPushButton(self.frame_77)
        self.post6_2.setObjectName(u"post6_2")
        self.post6_2.setMinimumSize(QSize(0, 100))
        self.post6_2.setIconSize(QSize(20, 20))

        self.gridLayout_16.addWidget(self.post6_2, 1, 2, 1, 1)


        self.verticalLayout_115.addLayout(self.gridLayout_16)


        self.horizontalLayout_56.addLayout(self.verticalLayout_115)

        self.frame_161 = QFrame(self.frame_77)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(50, 0))
        self.frame_161.setMaximumSize(QSize(50, 16777215))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_161)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.rightButton_17 = QPushButton(self.frame_161)
        self.rightButton_17.setObjectName(u"rightButton_17")
        self.rightButton_17.setFont(font3)
        self.rightButton_17.setStyleSheet(u"")

        self.verticalLayout_128.addWidget(self.rightButton_17)


        self.horizontalLayout_56.addWidget(self.frame_161)


        self.verticalLayout_48.addWidget(self.frame_77)


        self.verticalLayout_47.addWidget(self.frame_75)

        self.stackedWidget_6.addWidget(self.page_6)
        self.page_27 = QWidget()
        self.page_27.setObjectName(u"page_27")
        self.verticalLayout_129 = QVBoxLayout(self.page_27)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.frame_179 = QFrame(self.page_27)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frame_179)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.label_144 = QLabel(self.frame_179)
        self.label_144.setObjectName(u"label_144")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_144.setFont(font7)
        self.label_144.setAlignment(Qt.AlignCenter)

        self.verticalLayout_130.addWidget(self.label_144)

        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setMinimumSize(QSize(0, 350))
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_181 = QFrame(self.frame_180)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setMinimumSize(QSize(50, 0))
        self.frame_181.setMaximumSize(QSize(50, 16777215))
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_181)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.frame_182 = QFrame(self.frame_181)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMinimumSize(QSize(0, 150))
        self.frame_182.setMaximumSize(QSize(16777215, 150))
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)

        self.verticalLayout_131.addWidget(self.frame_182)

        self.leftButton_18 = QPushButton(self.frame_181)
        self.leftButton_18.setObjectName(u"leftButton_18")
        self.leftButton_18.setFont(font3)
        self.leftButton_18.setStyleSheet(u"")

        self.verticalLayout_131.addWidget(self.leftButton_18)

        self.frame_183 = QFrame(self.frame_181)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)

        self.verticalLayout_131.addWidget(self.frame_183)


        self.horizontalLayout_61.addWidget(self.frame_181)

        self.verticalLayout_132 = QVBoxLayout()
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setSpacing(10)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_44 = QPushButton(self.frame_180)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(0, 100))
        self.pushButton_44.setIconSize(QSize(20, 20))

        self.gridLayout_17.addWidget(self.pushButton_44, 0, 0, 1, 1)

        self.pushButton_45 = QPushButton(self.frame_180)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(0, 100))
        self.pushButton_45.setIconSize(QSize(20, 20))

        self.gridLayout_17.addWidget(self.pushButton_45, 1, 1, 1, 1)

        self.pushButton_46 = QPushButton(self.frame_180)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(0, 100))
        self.pushButton_46.setIconSize(QSize(20, 20))

        self.gridLayout_17.addWidget(self.pushButton_46, 1, 2, 1, 1)

        self.pushButton_49 = QPushButton(self.frame_180)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(0, 100))
        self.pushButton_49.setIconSize(QSize(20, 20))

        self.gridLayout_17.addWidget(self.pushButton_49, 0, 1, 1, 1)

        self.pushButton_58 = QPushButton(self.frame_180)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMinimumSize(QSize(0, 100))
        self.pushButton_58.setIconSize(QSize(20, 20))

        self.gridLayout_17.addWidget(self.pushButton_58, 1, 0, 1, 1)

        self.pushButton_59 = QPushButton(self.frame_180)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMinimumSize(QSize(0, 100))
        self.pushButton_59.setIconSize(QSize(20, 20))

        self.gridLayout_17.addWidget(self.pushButton_59, 0, 2, 1, 1)


        self.verticalLayout_132.addLayout(self.gridLayout_17)


        self.horizontalLayout_61.addLayout(self.verticalLayout_132)

        self.frame_184 = QFrame(self.frame_180)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(50, 0))
        self.frame_184.setMaximumSize(QSize(50, 16777215))
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_184)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMinimumSize(QSize(0, 150))
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_185)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_135.addWidget(self.frame_185)

        self.rightButton_18 = QPushButton(self.frame_184)
        self.rightButton_18.setObjectName(u"rightButton_18")
        self.rightButton_18.setFont(font3)
        self.rightButton_18.setStyleSheet(u"")

        self.verticalLayout_135.addWidget(self.rightButton_18)

        self.frame_186 = QFrame(self.frame_184)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_186)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")

        self.verticalLayout_135.addWidget(self.frame_186)


        self.horizontalLayout_61.addWidget(self.frame_184)


        self.verticalLayout_130.addWidget(self.frame_180)


        self.verticalLayout_129.addWidget(self.frame_179)

        self.stackedWidget_6.addWidget(self.page_27)
        self.page_28 = QWidget()
        self.page_28.setObjectName(u"page_28")
        self.verticalLayout_142 = QVBoxLayout(self.page_28)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.frame_187 = QFrame(self.page_28)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_187)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.label_148 = QLabel(self.frame_187)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font7)
        self.label_148.setAlignment(Qt.AlignCenter)

        self.verticalLayout_144.addWidget(self.label_148)

        self.frame_190 = QFrame(self.frame_187)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setMinimumSize(QSize(0, 350))
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_191 = QFrame(self.frame_190)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(50, 0))
        self.frame_191.setMaximumSize(QSize(50, 16777215))
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_191)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMinimumSize(QSize(0, 150))
        self.frame_192.setMaximumSize(QSize(16777215, 150))
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)

        self.verticalLayout_145.addWidget(self.frame_192)

        self.leftButton_21 = QPushButton(self.frame_191)
        self.leftButton_21.setObjectName(u"leftButton_21")
        self.leftButton_21.setFont(font3)
        self.leftButton_21.setStyleSheet(u"")

        self.verticalLayout_145.addWidget(self.leftButton_21)

        self.frame_199 = QFrame(self.frame_191)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)

        self.verticalLayout_145.addWidget(self.frame_199)


        self.horizontalLayout_68.addWidget(self.frame_191)

        self.verticalLayout_149 = QVBoxLayout()
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setSpacing(10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_61 = QPushButton(self.frame_190)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMinimumSize(QSize(0, 100))
        self.pushButton_61.setIconSize(QSize(20, 20))

        self.gridLayout_18.addWidget(self.pushButton_61, 0, 2, 1, 1)

        self.pushButton_67 = QPushButton(self.frame_190)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(0, 100))
        self.pushButton_67.setIconSize(QSize(20, 20))

        self.gridLayout_18.addWidget(self.pushButton_67, 0, 1, 1, 1)

        self.pushButton_68 = QPushButton(self.frame_190)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(0, 100))
        self.pushButton_68.setIconSize(QSize(20, 20))

        self.gridLayout_18.addWidget(self.pushButton_68, 0, 0, 1, 1)

        self.pushButton_69 = QPushButton(self.frame_190)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setMinimumSize(QSize(0, 100))
        self.pushButton_69.setIconSize(QSize(20, 20))

        self.gridLayout_18.addWidget(self.pushButton_69, 1, 0, 1, 1)

        self.pushButton_70 = QPushButton(self.frame_190)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setMinimumSize(QSize(0, 100))
        self.pushButton_70.setIconSize(QSize(20, 20))

        self.gridLayout_18.addWidget(self.pushButton_70, 1, 1, 1, 1)

        self.pushButton_71 = QPushButton(self.frame_190)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setMinimumSize(QSize(0, 100))
        self.pushButton_71.setIconSize(QSize(20, 20))

        self.gridLayout_18.addWidget(self.pushButton_71, 1, 2, 1, 1)


        self.verticalLayout_149.addLayout(self.gridLayout_18)


        self.horizontalLayout_68.addLayout(self.verticalLayout_149)

        self.frame_200 = QFrame(self.frame_190)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(50, 0))
        self.frame_200.setMaximumSize(QSize(50, 16777215))
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_200)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.frame_201 = QFrame(self.frame_200)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMinimumSize(QSize(0, 150))
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_201)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_150.addWidget(self.frame_201)

        self.rightButton_21 = QPushButton(self.frame_200)
        self.rightButton_21.setObjectName(u"rightButton_21")
        self.rightButton_21.setFont(font3)
        self.rightButton_21.setStyleSheet(u"")

        self.verticalLayout_150.addWidget(self.rightButton_21)

        self.frame_202 = QFrame(self.frame_200)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.verticalLayout_151 = QVBoxLayout(self.frame_202)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")

        self.verticalLayout_150.addWidget(self.frame_202)


        self.horizontalLayout_68.addWidget(self.frame_200)


        self.verticalLayout_144.addWidget(self.frame_190)


        self.verticalLayout_142.addWidget(self.frame_187)

        self.stackedWidget_6.addWidget(self.page_28)

        self.horizontalLayout_36.addWidget(self.stackedWidget_6)

        self.stackedPages_2.addWidget(self.page3_2)
        self.page4_2 = QWidget()
        self.page4_2.setObjectName(u"page4_2")
        self.horizontalLayout_72 = QHBoxLayout(self.page4_2)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.stackedMusicPosts_2 = QStackedWidget(self.page4_2)
        self.stackedMusicPosts_2.setObjectName(u"stackedMusicPosts_2")
        self.page_33 = QWidget()
        self.page_33.setObjectName(u"page_33")
        self.verticalLayout_152 = QVBoxLayout(self.page_33)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.frame_241 = QFrame(self.page_33)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setMinimumSize(QSize(0, 60))
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(130, -1, -1, -1)
        self.frame_242 = QFrame(self.frame_241)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMaximumSize(QSize(300, 100))
        self.frame_242.setFrameShape(QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_242)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_55 = QLabel(self.frame_242)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setPixmap(QPixmap(u"laugh.png"))
        self.label_55.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_55, 0, 3, 1, 1)

        self.label_56 = QLabel(self.frame_242)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setPixmap(QPixmap(u"sad.png"))
        self.label_56.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_56, 0, 1, 1, 1)

        self.label_57 = QLabel(self.frame_242)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setPixmap(QPixmap(u"surprise.png"))
        self.label_57.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_57, 0, 2, 1, 1)

        self.label_58 = QLabel(self.frame_242)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setPixmap(QPixmap(u"love.png"))
        self.label_58.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_59 = QLabel(self.frame_242)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_59, 1, 0, 1, 1)

        self.label_60 = QLabel(self.frame_242)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_60, 1, 1, 1, 1)

        self.label_61 = QLabel(self.frame_242)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_61, 1, 2, 1, 1)

        self.label_62 = QLabel(self.frame_242)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_62, 1, 3, 1, 1)


        self.horizontalLayout_95.addWidget(self.frame_242)

        self.pushButton_72 = QPushButton(self.frame_241)
        self.pushButton_72.setObjectName(u"pushButton_72")

        self.horizontalLayout_95.addWidget(self.pushButton_72, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_152.addWidget(self.frame_241)

        self.frame_205 = QFrame(self.page_33)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_205)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.frame_206 = QFrame(self.frame_205)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.pushButton_73 = QPushButton(self.frame_206)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_73.addWidget(self.pushButton_73, 0, Qt.AlignBottom)

        self.verticalLayout_154 = QVBoxLayout()
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.label_160 = QLabel(self.frame_206)
        self.label_160.setObjectName(u"label_160")

        self.verticalLayout_154.addWidget(self.label_160, 0, Qt.AlignHCenter)

        self.frame_207 = QFrame(self.frame_206)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setMinimumSize(QSize(0, 100))
        self.frame_207.setMaximumSize(QSize(16777215, 150))
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_207)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.frame_209 = QFrame(self.frame_207)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_209)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_Title_9 = QLabel(self.frame_209)
        self.label_Title_9.setObjectName(u"label_Title_9")
        font8 = QFont()
        font8.setPointSize(21)
        font8.setBold(True)
        self.label_Title_9.setFont(font8)
        self.label_Title_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.label_Title_9, 0, Qt.AlignHCenter)


        self.verticalLayout_158.addWidget(self.frame_209)

        self.label_161 = QLabel(self.frame_207)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(True)
        self.label_161.setFont(font9)

        self.verticalLayout_158.addWidget(self.label_161, 0, Qt.AlignHCenter)

        self.frame_210 = QFrame(self.frame_207)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setStyleSheet(u"*{\n"
"border-radius: 10px;\n"
"  background-color: #6522f2;\n"
"}")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_210)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_166 = QLabel(self.frame_210)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_89.addWidget(self.label_166, 0, Qt.AlignLeft)

        self.horizontalSlider_15 = QSlider(self.frame_210)
        self.horizontalSlider_15.setObjectName(u"horizontalSlider_15")
        self.horizontalSlider_15.setStyleSheet(u"*{color: #FFFFFF;}")
        self.horizontalSlider_15.setValue(25)
        self.horizontalSlider_15.setSliderPosition(25)
        self.horizontalSlider_15.setOrientation(Qt.Horizontal)

        self.horizontalLayout_89.addWidget(self.horizontalSlider_15)

        self.label_167 = QLabel(self.frame_210)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_89.addWidget(self.label_167, 0, Qt.AlignRight)


        self.verticalLayout_158.addWidget(self.frame_210)


        self.verticalLayout_154.addWidget(self.frame_207)


        self.horizontalLayout_73.addLayout(self.verticalLayout_154)

        self.frame_211 = QFrame(self.frame_206)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setMinimumSize(QSize(50, 0))
        self.frame_211.setMaximumSize(QSize(50, 16777215))
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_211)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(0, 0, 0, 0)
        self.frame_212 = QFrame(self.frame_211)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setMinimumSize(QSize(0, 150))
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_212)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_159.addWidget(self.frame_212)

        self.frame_213 = QFrame(self.frame_211)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_213)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalSlider_15 = QSlider(self.frame_213)
        self.verticalSlider_15.setObjectName(u"verticalSlider_15")
        self.verticalSlider_15.setValue(40)
        self.verticalSlider_15.setOrientation(Qt.Vertical)

        self.verticalLayout_160.addWidget(self.verticalSlider_15)

        self.pushButton_74 = QPushButton(self.frame_213)
        self.pushButton_74.setObjectName(u"pushButton_74")

        self.verticalLayout_160.addWidget(self.pushButton_74)


        self.verticalLayout_159.addWidget(self.frame_213)


        self.horizontalLayout_73.addWidget(self.frame_211)


        self.verticalLayout_153.addWidget(self.frame_206)


        self.verticalLayout_152.addWidget(self.frame_205)

        self.stackedMusicPosts_2.addWidget(self.page_33)
        self.page_34 = QWidget()
        self.page_34.setObjectName(u"page_34")
        self.verticalLayout_161 = QVBoxLayout(self.page_34)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.frame_243 = QFrame(self.page_34)
        self.frame_243.setObjectName(u"frame_243")
        self.frame_243.setMinimumSize(QSize(0, 60))
        self.frame_243.setFrameShape(QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_243)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(130, -1, -1, -1)
        self.frame_244 = QFrame(self.frame_243)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setMaximumSize(QSize(300, 100))
        self.frame_244.setFrameShape(QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_244)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_63 = QLabel(self.frame_244)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setPixmap(QPixmap(u"laugh.png"))
        self.label_63.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_63, 0, 3, 1, 1)

        self.label_64 = QLabel(self.frame_244)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setPixmap(QPixmap(u"sad.png"))
        self.label_64.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_64, 0, 1, 1, 1)

        self.label_65 = QLabel(self.frame_244)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setPixmap(QPixmap(u"surprise.png"))
        self.label_65.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_65, 0, 2, 1, 1)

        self.label_66 = QLabel(self.frame_244)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setPixmap(QPixmap(u"love.png"))
        self.label_66.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_67 = QLabel(self.frame_244)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_67, 1, 0, 1, 1)

        self.label_68 = QLabel(self.frame_244)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_68, 1, 1, 1, 1)

        self.label_69 = QLabel(self.frame_244)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_69, 1, 2, 1, 1)

        self.label_70 = QLabel(self.frame_244)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_70, 1, 3, 1, 1)


        self.horizontalLayout_101.addWidget(self.frame_244)

        self.pushButton_75 = QPushButton(self.frame_243)
        self.pushButton_75.setObjectName(u"pushButton_75")

        self.horizontalLayout_101.addWidget(self.pushButton_75, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_161.addWidget(self.frame_243)

        self.frame_245 = QFrame(self.page_34)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setFrameShape(QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_245)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.frame_256 = QFrame(self.frame_245)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_256)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.pushButton_76 = QPushButton(self.frame_256)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_102.addWidget(self.pushButton_76, 0, Qt.AlignBottom)

        self.verticalLayout_177 = QVBoxLayout()
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.label_191 = QLabel(self.frame_256)
        self.label_191.setObjectName(u"label_191")

        self.verticalLayout_177.addWidget(self.label_191, 0, Qt.AlignHCenter)

        self.frame_270 = QFrame(self.frame_256)
        self.frame_270.setObjectName(u"frame_270")
        self.frame_270.setMinimumSize(QSize(0, 100))
        self.frame_270.setMaximumSize(QSize(16777215, 150))
        self.frame_270.setFrameShape(QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_270)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.frame_271 = QFrame(self.frame_270)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setFrameShape(QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_271)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_15 = QLabel(self.frame_271)
        self.label_Likes_15.setObjectName(u"label_Likes_15")

        self.horizontalLayout_103.addWidget(self.label_Likes_15)

        self.label_Title_12 = QLabel(self.frame_271)
        self.label_Title_12.setObjectName(u"label_Title_12")
        self.label_Title_12.setFont(font8)
        self.label_Title_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.label_Title_12, 0, Qt.AlignHCenter)

        self.label_Likes_6 = QLabel(self.frame_271)
        self.label_Likes_6.setObjectName(u"label_Likes_6")

        self.horizontalLayout_103.addWidget(self.label_Likes_6, 0, Qt.AlignRight)


        self.verticalLayout_178.addWidget(self.frame_271)

        self.label_201 = QLabel(self.frame_270)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMaximumSize(QSize(16777215, 30))
        self.label_201.setFont(font9)

        self.verticalLayout_178.addWidget(self.label_201, 0, Qt.AlignHCenter)

        self.frame_272 = QFrame(self.frame_270)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setFrameShape(QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_272)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.label_202 = QLabel(self.frame_272)
        self.label_202.setObjectName(u"label_202")

        self.horizontalLayout_104.addWidget(self.label_202, 0, Qt.AlignLeft)

        self.horizontalSlider_20 = QSlider(self.frame_272)
        self.horizontalSlider_20.setObjectName(u"horizontalSlider_20")
        self.horizontalSlider_20.setValue(25)
        self.horizontalSlider_20.setSliderPosition(25)
        self.horizontalSlider_20.setOrientation(Qt.Horizontal)

        self.horizontalLayout_104.addWidget(self.horizontalSlider_20)

        self.label_203 = QLabel(self.frame_272)
        self.label_203.setObjectName(u"label_203")

        self.horizontalLayout_104.addWidget(self.label_203, 0, Qt.AlignRight)


        self.verticalLayout_178.addWidget(self.frame_272)


        self.verticalLayout_177.addWidget(self.frame_270)


        self.horizontalLayout_102.addLayout(self.verticalLayout_177)

        self.frame_273 = QFrame(self.frame_256)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setMinimumSize(QSize(50, 0))
        self.frame_273.setMaximumSize(QSize(50, 16777215))
        self.frame_273.setFrameShape(QFrame.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_273)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.frame_274 = QFrame(self.frame_273)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setMinimumSize(QSize(0, 150))
        self.frame_274.setFrameShape(QFrame.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_274)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_179.addWidget(self.frame_274)

        self.frame_275 = QFrame(self.frame_273)
        self.frame_275.setObjectName(u"frame_275")
        self.frame_275.setFrameShape(QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.frame_275)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalSlider_20 = QSlider(self.frame_275)
        self.verticalSlider_20.setObjectName(u"verticalSlider_20")
        self.verticalSlider_20.setValue(40)
        self.verticalSlider_20.setOrientation(Qt.Vertical)

        self.verticalLayout_180.addWidget(self.verticalSlider_20)

        self.pushButton_77 = QPushButton(self.frame_275)
        self.pushButton_77.setObjectName(u"pushButton_77")

        self.verticalLayout_180.addWidget(self.pushButton_77)


        self.verticalLayout_179.addWidget(self.frame_275)


        self.horizontalLayout_102.addWidget(self.frame_273)


        self.verticalLayout_164.addWidget(self.frame_256)


        self.verticalLayout_161.addWidget(self.frame_245)

        self.stackedMusicPosts_2.addWidget(self.page_34)
        self.page_35 = QWidget()
        self.page_35.setObjectName(u"page_35")
        self.verticalLayout_165 = QVBoxLayout(self.page_35)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.frame_246 = QFrame(self.page_35)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setMinimumSize(QSize(0, 60))
        self.frame_246.setFrameShape(QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_246)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(130, -1, -1, -1)
        self.frame_251 = QFrame(self.frame_246)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMaximumSize(QSize(300, 100))
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_251)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_71 = QLabel(self.frame_251)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setPixmap(QPixmap(u"laugh.png"))
        self.label_71.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_71, 0, 3, 1, 1)

        self.label_72 = QLabel(self.frame_251)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setPixmap(QPixmap(u"sad.png"))
        self.label_72.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_72, 0, 1, 1, 1)

        self.label_73 = QLabel(self.frame_251)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setPixmap(QPixmap(u"surprise.png"))
        self.label_73.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_73, 0, 2, 1, 1)

        self.label_74 = QLabel(self.frame_251)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"*{border-radius:50\n"
"}")
        self.label_74.setPixmap(QPixmap(u"love.png"))
        self.label_74.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_74, 0, 0, 1, 1)

        self.label_75 = QLabel(self.frame_251)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_75, 1, 0, 1, 1)

        self.label_76 = QLabel(self.frame_251)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_76, 1, 1, 1, 1)

        self.label_77 = QLabel(self.frame_251)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_77, 1, 2, 1, 1)

        self.label_78 = QLabel(self.frame_251)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_78, 1, 3, 1, 1)


        self.horizontalLayout_106.addWidget(self.frame_251)

        self.pushButton_78 = QPushButton(self.frame_246)
        self.pushButton_78.setObjectName(u"pushButton_78")

        self.horizontalLayout_106.addWidget(self.pushButton_78, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_165.addWidget(self.frame_246)

        self.frame_214 = QFrame(self.page_35)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_214)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.frame_215 = QFrame(self.frame_214)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.pushButton_79 = QPushButton(self.frame_215)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_107.addWidget(self.pushButton_79, 0, Qt.AlignBottom)

        self.verticalLayout_167 = QVBoxLayout()
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.label_168 = QLabel(self.frame_215)
        self.label_168.setObjectName(u"label_168")

        self.verticalLayout_167.addWidget(self.label_168, 0, Qt.AlignHCenter)

        self.frame_216 = QFrame(self.frame_215)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setMinimumSize(QSize(0, 100))
        self.frame_216.setMaximumSize(QSize(16777215, 150))
        self.frame_216.setFrameShape(QFrame.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_216)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.frame_276 = QFrame(self.frame_216)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setFrameShape(QFrame.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_276)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_16 = QLabel(self.frame_276)
        self.label_Likes_16.setObjectName(u"label_Likes_16")

        self.horizontalLayout_108.addWidget(self.label_Likes_16)

        self.label_Title_13 = QLabel(self.frame_276)
        self.label_Title_13.setObjectName(u"label_Title_13")
        self.label_Title_13.setFont(font8)
        self.label_Title_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_108.addWidget(self.label_Title_13, 0, Qt.AlignHCenter)

        self.label_Likes_7 = QLabel(self.frame_276)
        self.label_Likes_7.setObjectName(u"label_Likes_7")

        self.horizontalLayout_108.addWidget(self.label_Likes_7, 0, Qt.AlignRight)


        self.verticalLayout_168.addWidget(self.frame_276)

        self.label_169 = QLabel(self.frame_216)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMaximumSize(QSize(16777215, 30))
        self.label_169.setFont(font9)

        self.verticalLayout_168.addWidget(self.label_169, 0, Qt.AlignHCenter)

        self.frame_277 = QFrame(self.frame_216)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setFrameShape(QFrame.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_277)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_170 = QLabel(self.frame_277)
        self.label_170.setObjectName(u"label_170")

        self.horizontalLayout_109.addWidget(self.label_170, 0, Qt.AlignLeft)

        self.horizontalSlider_21 = QSlider(self.frame_277)
        self.horizontalSlider_21.setObjectName(u"horizontalSlider_21")
        self.horizontalSlider_21.setValue(25)
        self.horizontalSlider_21.setSliderPosition(25)
        self.horizontalSlider_21.setOrientation(Qt.Horizontal)

        self.horizontalLayout_109.addWidget(self.horizontalSlider_21)

        self.label_171 = QLabel(self.frame_277)
        self.label_171.setObjectName(u"label_171")

        self.horizontalLayout_109.addWidget(self.label_171, 0, Qt.AlignRight)


        self.verticalLayout_168.addWidget(self.frame_277)


        self.verticalLayout_167.addWidget(self.frame_216)


        self.horizontalLayout_107.addLayout(self.verticalLayout_167)

        self.frame_278 = QFrame(self.frame_215)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setMinimumSize(QSize(50, 0))
        self.frame_278.setMaximumSize(QSize(50, 16777215))
        self.frame_278.setFrameShape(QFrame.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_278)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.frame_279 = QFrame(self.frame_278)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setMinimumSize(QSize(0, 150))
        self.frame_279.setFrameShape(QFrame.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_279)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_169.addWidget(self.frame_279)

        self.frame_280 = QFrame(self.frame_278)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setFrameShape(QFrame.StyledPanel)
        self.frame_280.setFrameShadow(QFrame.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_280)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalSlider_23 = QSlider(self.frame_280)
        self.verticalSlider_23.setObjectName(u"verticalSlider_23")
        self.verticalSlider_23.setValue(40)
        self.verticalSlider_23.setOrientation(Qt.Vertical)

        self.verticalLayout_181.addWidget(self.verticalSlider_23)

        self.pushButton_80 = QPushButton(self.frame_280)
        self.pushButton_80.setObjectName(u"pushButton_80")

        self.verticalLayout_181.addWidget(self.pushButton_80)


        self.verticalLayout_169.addWidget(self.frame_280)


        self.horizontalLayout_107.addWidget(self.frame_278)


        self.verticalLayout_166.addWidget(self.frame_215)


        self.verticalLayout_165.addWidget(self.frame_214)

        self.stackedMusicPosts_2.addWidget(self.page_35)

        self.horizontalLayout_72.addWidget(self.stackedMusicPosts_2)

        self.stackedPages_2.addWidget(self.page4_2)
        self.page5_2 = QWidget()
        self.page5_2.setObjectName(u"page5_2")
        self.horizontalLayout_38 = QHBoxLayout(self.page5_2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_78 = QFrame(self.page5_2)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(500, 300))
        self.frame_78.setMaximumSize(QSize(400, 400))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(300, 400))
        self.frame_79.setMaximumSize(QSize(600, 16777215))
        self.frame_79.setStyleSheet(u"*{\n"
"background-color: #6522f2;\n"
"}")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_79)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(50, 40, 50, 40)
        self.pushButton_81 = QPushButton(self.frame_79)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setMinimumSize(QSize(0, 50))
        self.pushButton_81.setFont(font7)
        self.pushButton_81.setStyleSheet(u"*{background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_50.addWidget(self.pushButton_81)

        self.pushButton_82 = QPushButton(self.frame_79)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setMinimumSize(QSize(0, 50))
        self.pushButton_82.setFont(font7)
        self.pushButton_82.setStyleSheet(u"*{background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_50.addWidget(self.pushButton_82)


        self.horizontalLayout_39.addWidget(self.frame_79)

        self.label_79 = QLabel(self.frame_78)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(200, 16777215))
        self.label_79.setCursor(QCursor(Qt.ArrowCursor))
        self.label_79.setTabletTracking(False)
        self.label_79.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_79.setPixmap(QPixmap(u"lp.png"))
        self.label_79.setScaledContents(True)
        self.label_79.setAlignment(Qt.AlignCenter)
        self.label_79.setWordWrap(False)

        self.horizontalLayout_39.addWidget(self.label_79)


        self.horizontalLayout_38.addWidget(self.frame_78, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages_2.addWidget(self.page5_2)
        self.page6_2 = QWidget()
        self.page6_2.setObjectName(u"page6_2")
        self.horizontalLayout_45 = QHBoxLayout(self.page6_2)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_80 = QFrame(self.page6_2)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMaximumSize(QSize(400, 300))
        self.frame_80.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setGeometry(QRect(20, 140, 371, 101))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_81)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, -1, -1, -1)
        self.label_80 = QLabel(self.frame_81)
        self.label_80.setObjectName(u"label_80")
        font10 = QFont()
        font10.setPointSize(11)
        self.label_80.setFont(font10)
        self.label_80.setStyleSheet(u"*{color:#ffffff;}")

        self.verticalLayout_51.addWidget(self.label_80)

        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(0, 50))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_82)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setStyleSheet(u"*{background-color:#ffffff;}")

        self.horizontalLayout_46.addWidget(self.lineEdit_3)

        self.pushButton_83 = QPushButton(self.frame_82)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setMinimumSize(QSize(0, 40))
        self.pushButton_83.setMaximumSize(QSize(50, 16777215))
        self.pushButton_83.setStyleSheet(u"*{background-color: #d9d9d9;}")

        self.horizontalLayout_46.addWidget(self.pushButton_83)


        self.verticalLayout_51.addWidget(self.frame_82)


        self.horizontalLayout_45.addWidget(self.frame_80)

        self.stackedPages_2.addWidget(self.page6_2)
        self.page7_2 = QWidget()
        self.page7_2.setObjectName(u"page7_2")
        self.verticalLayout_52 = QVBoxLayout(self.page7_2)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_81 = QLabel(self.page7_2)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 350))
        font11 = QFont()
        font11.setPointSize(16)
        self.label_81.setFont(font11)

        self.verticalLayout_52.addWidget(self.label_81, 0, Qt.AlignHCenter)

        self.frame_83 = QFrame(self.page7_2)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMaximumSize(QSize(16777215, 16777215))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(50, 0))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.pushButton_84 = QPushButton(self.frame_84)
        self.pushButton_84.setObjectName(u"pushButton_84")
        self.pushButton_84.setGeometry(QRect(0, 170, 50, 28))
        self.pushButton_84.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_47.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_83)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_85)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_252 = QFrame(self.frame_85)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setFrameShape(QFrame.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_252)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_Title_14 = QLabel(self.frame_252)
        self.label_Title_14.setObjectName(u"label_Title_14")
        self.label_Title_14.setFont(font4)
        self.label_Title_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.label_Title_14)


        self.verticalLayout_53.addWidget(self.frame_252)

        self.label_Artist_6 = QLabel(self.frame_85)
        self.label_Artist_6.setObjectName(u"label_Artist_6")
        self.label_Artist_6.setFont(font5)
        self.label_Artist_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Artist_6)

        self.frame_253 = QFrame(self.frame_85)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setFrameShape(QFrame.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_253)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_192 = QLabel(self.frame_253)
        self.label_192.setObjectName(u"label_192")

        self.horizontalLayout_112.addWidget(self.label_192, 0, Qt.AlignLeft)

        self.horizontalSlider_24 = QSlider(self.frame_253)
        self.horizontalSlider_24.setObjectName(u"horizontalSlider_24")
        self.horizontalSlider_24.setValue(25)
        self.horizontalSlider_24.setSliderPosition(25)
        self.horizontalSlider_24.setOrientation(Qt.Horizontal)

        self.horizontalLayout_112.addWidget(self.horizontalSlider_24)

        self.label_193 = QLabel(self.frame_253)
        self.label_193.setObjectName(u"label_193")

        self.horizontalLayout_112.addWidget(self.label_193, 0, Qt.AlignRight)


        self.verticalLayout_53.addWidget(self.frame_253)


        self.horizontalLayout_47.addWidget(self.frame_85)

        self.frame_254 = QFrame(self.frame_83)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setMaximumSize(QSize(50, 16777215))
        self.frame_254.setFrameShape(QFrame.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_254)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalSlider_24 = QSlider(self.frame_254)
        self.verticalSlider_24.setObjectName(u"verticalSlider_24")
        self.verticalSlider_24.setValue(40)
        self.verticalSlider_24.setOrientation(Qt.Vertical)

        self.verticalLayout_170.addWidget(self.verticalSlider_24, 0, Qt.AlignHCenter)

        self.pushButton_85 = QPushButton(self.frame_254)
        self.pushButton_85.setObjectName(u"pushButton_85")

        self.verticalLayout_170.addWidget(self.pushButton_85)


        self.horizontalLayout_47.addWidget(self.frame_254)


        self.verticalLayout_52.addWidget(self.frame_83)

        self.stackedPages_2.addWidget(self.page7_2)
        self.page8_2 = QWidget()
        self.page8_2.setObjectName(u"page8_2")
        self.verticalLayout_54 = QVBoxLayout(self.page8_2)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_86 = QFrame(self.page8_2)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(500, 0))
        self.frame_86.setMaximumSize(QSize(250, 300))
        self.frame_86.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_86)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 40, 0, 0)
        self.label_82 = QLabel(self.frame_86)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(100, 100))
        self.label_82.setMaximumSize(QSize(150, 150))
        font12 = QFont()
        font12.setPointSize(20)
        self.label_82.setFont(font12)
        self.label_82.setPixmap(QPixmap(u"qr.png"))
        self.label_82.setScaledContents(True)
        self.label_82.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.label_82, 0, Qt.AlignHCenter)

        self.label_83 = QLabel(self.frame_86)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font10)
        self.label_83.setStyleSheet(u"*{color:#ffffff;}")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.label_83)


        self.verticalLayout_54.addWidget(self.frame_86, 0, Qt.AlignHCenter)

        self.stackedPages_2.addWidget(self.page8_2)
        self.page9_2 = QWidget()
        self.page9_2.setObjectName(u"page9_2")
        self.verticalLayout_56 = QVBoxLayout(self.page9_2)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_87 = QFrame(self.page9_2)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_87)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 100))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.pushButton_86 = QPushButton(self.frame_88)
        self.pushButton_86.setObjectName(u"pushButton_86")
        self.pushButton_86.setGeometry(QRect(440, 70, 93, 28))
        self.pushButton_86.setStyleSheet(u"*{width: 91px;\n"
"  height: 34px;\n"
"  border-radius: 10px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}")
        self.label_84 = QLabel(self.frame_88)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(0, 0, 341, 41))
        font13 = QFont()
        font13.setFamilies([u"Arial"])
        font13.setPointSize(9)
        font13.setBold(True)
        self.label_84.setFont(font13)
        self.label_84.setStyleSheet(u"*{width: 312px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
"  background-color: #2ae2e2;}")
        self.label_84.setFrameShape(QFrame.Box)
        self.label_84.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.frame_88)

        self.tabWidget_2 = QTabWidget(self.frame_87)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_58 = QVBoxLayout(self.tab_3)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_89 = QFrame(self.tab_3)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_89)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 30))
        self.frame_90.setFrameShape(QFrame.Box)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(10, 0, 0, 0)
        self.label_85 = QLabel(self.frame_90)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_48.addWidget(self.label_85)

        self.pushButton_87 = QPushButton(self.frame_90)
        self.pushButton_87.setObjectName(u"pushButton_87")
        self.pushButton_87.setMaximumSize(QSize(30, 16777215))
        self.pushButton_87.setIconSize(QSize(20, 20))
        self.pushButton_87.setAutoRepeatDelay(305)

        self.horizontalLayout_48.addWidget(self.pushButton_87, 0, Qt.AlignRight)


        self.verticalLayout_59.addWidget(self.frame_90, 0, Qt.AlignVCenter)

        self.frame_91 = QFrame(self.frame_89)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)

        self.verticalLayout_59.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_89)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.radioButton_12 = QRadioButton(self.frame_92)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)

        self.horizontalLayout_51.addWidget(self.radioButton_12)

        self.label_86 = QLabel(self.frame_92)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_51.addWidget(self.label_86, 0, Qt.AlignRight)


        self.verticalLayout_59.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_89)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.radioButton_13 = QRadioButton(self.frame_93)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.horizontalLayout_52.addWidget(self.radioButton_13)

        self.label_87 = QLabel(self.frame_93)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_52.addWidget(self.label_87, 0, Qt.AlignRight)


        self.verticalLayout_59.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_89)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.radioButton_14 = QRadioButton(self.frame_94)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.horizontalLayout_113.addWidget(self.radioButton_14)

        self.label_88 = QLabel(self.frame_94)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_113.addWidget(self.label_88, 0, Qt.AlignRight)


        self.verticalLayout_59.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_89)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.radioButton_15 = QRadioButton(self.frame_95)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.horizontalLayout_114.addWidget(self.radioButton_15)

        self.label_89 = QLabel(self.frame_95)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_114.addWidget(self.label_89, 0, Qt.AlignRight)


        self.verticalLayout_59.addWidget(self.frame_95)


        self.verticalLayout_58.addWidget(self.frame_89)

        self.frame_96 = QFrame(self.tab_3)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)

        self.verticalLayout_58.addWidget(self.frame_96)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_60 = QVBoxLayout(self.tab_4)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_97 = QFrame(self.tab_4)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_97)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMaximumSize(QSize(16777215, 30))
        self.frame_98.setFrameShape(QFrame.Box)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(10, 0, 0, 0)
        self.label_90 = QLabel(self.frame_98)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_115.addWidget(self.label_90)

        self.pushButton_88 = QPushButton(self.frame_98)
        self.pushButton_88.setObjectName(u"pushButton_88")
        self.pushButton_88.setMaximumSize(QSize(30, 16777215))
        self.pushButton_88.setIconSize(QSize(20, 20))
        self.pushButton_88.setAutoRepeatDelay(305)

        self.horizontalLayout_115.addWidget(self.pushButton_88, 0, Qt.AlignRight)


        self.verticalLayout_61.addWidget(self.frame_98, 0, Qt.AlignVCenter)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)

        self.verticalLayout_61.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_97)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.radioButton_16 = QRadioButton(self.frame_100)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setChecked(True)

        self.horizontalLayout_116.addWidget(self.radioButton_16)

        self.label_91 = QLabel(self.frame_100)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_116.addWidget(self.label_91, 0, Qt.AlignRight)


        self.verticalLayout_61.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_97)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.radioButton_17 = QRadioButton(self.frame_101)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.horizontalLayout_117.addWidget(self.radioButton_17)

        self.label_92 = QLabel(self.frame_101)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_117.addWidget(self.label_92, 0, Qt.AlignRight)


        self.verticalLayout_61.addWidget(self.frame_101)

        self.frame_102 = QFrame(self.frame_97)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.radioButton_18 = QRadioButton(self.frame_102)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.horizontalLayout_118.addWidget(self.radioButton_18)

        self.label_93 = QLabel(self.frame_102)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_118.addWidget(self.label_93, 0, Qt.AlignRight)


        self.verticalLayout_61.addWidget(self.frame_102)

        self.frame_103 = QFrame(self.frame_97)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.radioButton_19 = QRadioButton(self.frame_103)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.horizontalLayout_119.addWidget(self.radioButton_19)

        self.label_94 = QLabel(self.frame_103)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_119.addWidget(self.label_94, 0, Qt.AlignRight)


        self.verticalLayout_61.addWidget(self.frame_103)


        self.verticalLayout_60.addWidget(self.frame_97)

        self.frame_104 = QFrame(self.tab_4)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)

        self.verticalLayout_60.addWidget(self.frame_104)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_57.addWidget(self.tabWidget_2)


        self.verticalLayout_56.addWidget(self.frame_87)

        self.stackedPages_2.addWidget(self.page9_2)
        self.page10_2 = QWidget()
        self.page10_2.setObjectName(u"page10_2")
        self.verticalLayout_62 = QVBoxLayout(self.page10_2)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_105 = QFrame(self.page10_2)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 80))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.label_95 = QLabel(self.frame_105)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(10, 10, 271, 41))
        font14 = QFont()
        font14.setPointSize(10)
        self.label_95.setFont(font14)
        self.label_95.setFrameShape(QFrame.Box)
        self.label_95.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.frame_105)

        self.label_96 = QLabel(self.page10_2)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(0, 200))
        font15 = QFont()
        font15.setPointSize(21)
        self.label_96.setFont(font15)
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.label_96)

        self.frame_106 = QFrame(self.page10_2)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.frame_217 = QFrame(self.frame_106)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_217)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(30, 0, 0, 0)
        self.label_172 = QLabel(self.frame_217)
        self.label_172.setObjectName(u"label_172")
        font16 = QFont()
        font16.setPointSize(19)
        font16.setBold(True)
        font16.setUnderline(False)
        self.label_172.setFont(font16)
        self.label_172.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_171.addWidget(self.label_172, 0, Qt.AlignBottom)


        self.horizontalLayout_120.addWidget(self.frame_217)

        self.frame_107 = QFrame(self.frame_106)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_107)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_281 = QFrame(self.frame_107)
        self.frame_281.setObjectName(u"frame_281")
        self.frame_281.setFrameShape(QFrame.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_281)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.label_Title_15 = QLabel(self.frame_281)
        self.label_Title_15.setObjectName(u"label_Title_15")
        self.label_Title_15.setFont(font4)
        self.label_Title_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_121.addWidget(self.label_Title_15)


        self.verticalLayout_63.addWidget(self.frame_281)

        self.label_Artist_10 = QLabel(self.frame_107)
        self.label_Artist_10.setObjectName(u"label_Artist_10")
        self.label_Artist_10.setFont(font6)
        self.label_Artist_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.label_Artist_10)

        self.frame_282 = QFrame(self.frame_107)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setFrameShape(QFrame.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.frame_282)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.label_204 = QLabel(self.frame_282)
        self.label_204.setObjectName(u"label_204")

        self.horizontalLayout_122.addWidget(self.label_204, 0, Qt.AlignLeft)

        self.horizontalSlider_25 = QSlider(self.frame_282)
        self.horizontalSlider_25.setObjectName(u"horizontalSlider_25")
        self.horizontalSlider_25.setValue(25)
        self.horizontalSlider_25.setSliderPosition(25)
        self.horizontalSlider_25.setOrientation(Qt.Horizontal)

        self.horizontalLayout_122.addWidget(self.horizontalSlider_25)

        self.label_205 = QLabel(self.frame_282)
        self.label_205.setObjectName(u"label_205")

        self.horizontalLayout_122.addWidget(self.label_205, 0, Qt.AlignRight)


        self.verticalLayout_63.addWidget(self.frame_282)


        self.horizontalLayout_120.addWidget(self.frame_107)

        self.frame_283 = QFrame(self.frame_106)
        self.frame_283.setObjectName(u"frame_283")
        self.frame_283.setMaximumSize(QSize(50, 16777215))
        self.frame_283.setFrameShape(QFrame.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frame_283)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalSlider_25 = QSlider(self.frame_283)
        self.verticalSlider_25.setObjectName(u"verticalSlider_25")
        self.verticalSlider_25.setValue(40)
        self.verticalSlider_25.setOrientation(Qt.Vertical)

        self.verticalLayout_182.addWidget(self.verticalSlider_25)

        self.pushButton_89 = QPushButton(self.frame_283)
        self.pushButton_89.setObjectName(u"pushButton_89")

        self.verticalLayout_182.addWidget(self.pushButton_89)


        self.horizontalLayout_120.addWidget(self.frame_283)


        self.verticalLayout_62.addWidget(self.frame_106)

        self.stackedPages_2.addWidget(self.page10_2)
        self.page11_2 = QWidget()
        self.page11_2.setObjectName(u"page11_2")
        self.verticalLayout_64 = QVBoxLayout(self.page11_2)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.frame_108 = QFrame(self.page11_2)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 80))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.label_97 = QLabel(self.frame_108)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(10, 10, 411, 41))
        self.label_97.setFont(font14)
        self.label_97.setFrameShape(QFrame.Box)
        self.label_97.setAlignment(Qt.AlignCenter)
        self.frame_109 = QFrame(self.frame_108)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setGeometry(QRect(50, 180, 481, 99))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_109)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, -1, -1, -1)
        self.label_98 = QLabel(self.frame_109)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font10)

        self.verticalLayout_65.addWidget(self.label_98)

        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(0, 50))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.frame_110)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_123.addWidget(self.lineEdit_4)

        self.pushButton_90 = QPushButton(self.frame_110)
        self.pushButton_90.setObjectName(u"pushButton_90")
        self.pushButton_90.setMinimumSize(QSize(0, 40))
        self.pushButton_90.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_123.addWidget(self.pushButton_90)


        self.verticalLayout_65.addWidget(self.frame_110)


        self.verticalLayout_64.addWidget(self.frame_108)

        self.stackedPages_2.addWidget(self.page11_2)
        self.page12_2 = QWidget()
        self.page12_2.setObjectName(u"page12_2")
        self.label_99 = QLabel(self.page12_2)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(90, 220, 411, 41))
        self.label_99.setFont(font14)
        self.label_99.setFrameShape(QFrame.Box)
        self.label_99.setAlignment(Qt.AlignCenter)
        self.stackedPages_2.addWidget(self.page12_2)

        self.verticalLayout_25.addWidget(self.frame_152)


        self.horizontalLayout_11.addWidget(self.menu_bar)

        self.main = QFrame(self.display1)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(600, 600))
        self.main.setMaximumSize(QSize(800, 600))
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedPages = QStackedWidget(self.main)
        self.stackedPages.setObjectName(u"stackedPages")
        self.stackedPages.setMaximumSize(QSize(580, 600))
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Tags = QFrame(self.frame_4)
        self.Tags.setObjectName(u"Tags")
        self.Tags.setMinimumSize(QSize(0, 50))
        self.Tags.setMaximumSize(QSize(16777215, 50))
        self.Tags.setFrameShape(QFrame.StyledPanel)
        self.Tags.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Tags)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tag1 = QPushButton(self.Tags)
        self.tag1.setObjectName(u"tag1")
        self.tag1.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag1)

        self.tag2 = QPushButton(self.Tags)
        self.tag2.setObjectName(u"tag2")
        self.tag2.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag2)

        self.tag3 = QPushButton(self.Tags)
        self.tag3.setObjectName(u"tag3")
        self.tag3.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag3)

        self.tag4 = QPushButton(self.Tags)
        self.tag4.setObjectName(u"tag4")
        self.tag4.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag4)

        self.tag5 = QPushButton(self.Tags)
        self.tag5.setObjectName(u"tag5")
        self.tag5.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag5)

        self.tag6 = QPushButton(self.Tags)
        self.tag6.setObjectName(u"tag6")
        self.tag6.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout_4.addWidget(self.tag6)


        self.verticalLayout.addWidget(self.Tags)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.priorityBox = QComboBox(self.frame_7)
        self.priorityBox.addItem("")
        self.priorityBox.addItem("")
        self.priorityBox.addItem("")
        self.priorityBox.setObjectName(u"priorityBox")
        self.priorityBox.setMinimumSize(QSize(0, 30))
        self.priorityBox.setFont(font2)
        self.priorityBox.setStyleSheet(u"*{width: 66px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}\n"
"")

        self.horizontalLayout.addWidget(self.priorityBox, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_220 = QFrame(self.frame)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setMinimumSize(QSize(30, 0))
        self.frame_220.setMaximumSize(QSize(50, 16777215))
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_220)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.leftButton_19 = QPushButton(self.frame_220)
        self.leftButton_19.setObjectName(u"leftButton_19")
        self.leftButton_19.setFont(font3)
        self.leftButton_19.setStyleSheet(u"")

        self.verticalLayout_155.addWidget(self.leftButton_19)


        self.horizontalLayout_3.addWidget(self.frame_220)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(202, 16777215))
        self.scrollArea.setStyleSheet(u"/*border: 0;*/\n"
"/*QScrollBar:horizontal{\n"
"border:none;\n"
"background-color:rgb(59,59,90);\n"
"width:14px;\n"
"border-radius:0px;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"border-radius: 7px;\n"
"background-color:rgb(80,80,122);\n"
"}*/\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1137, 203))
        self.horizontalLayout_127 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.pushButton_97 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_97.setObjectName(u"pushButton_97")
        self.pushButton_97.setMinimumSize(QSize(180, 180))
        self.pushButton_97.setStyleSheet(u"border-radius:; background-color:white;")
        icon = QIcon()
        icon.addFile(u"icons/ditto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_97.setIcon(icon)
        self.pushButton_97.setIconSize(QSize(180, 180))

        self.horizontalLayout_127.addWidget(self.pushButton_97)

        self.pushButton_40 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(180, 180))
        self.pushButton_40.setStyleSheet(u"border-radius:; background-color:white;")
        icon1 = QIcon()
        icon1.addFile(u"icons/hype_boy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_40.setIcon(icon1)
        self.pushButton_40.setIconSize(QSize(180, 180))

        self.horizontalLayout_127.addWidget(self.pushButton_40)

        self.pushButton_93 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_93.setObjectName(u"pushButton_93")
        self.pushButton_93.setMinimumSize(QSize(180, 180))
        self.pushButton_93.setStyleSheet(u"border-radius:90; background-color:white;")
        self.pushButton_93.setIconSize(QSize(100, 100))

        self.horizontalLayout_127.addWidget(self.pushButton_93)

        self.pushButton_94 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_94.setObjectName(u"pushButton_94")
        self.pushButton_94.setMinimumSize(QSize(180, 180))
        self.pushButton_94.setStyleSheet(u"border-radius:90; background-color:white;")
        self.pushButton_94.setIconSize(QSize(100, 100))

        self.horizontalLayout_127.addWidget(self.pushButton_94)

        self.pushButton_96 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_96.setObjectName(u"pushButton_96")
        self.pushButton_96.setMinimumSize(QSize(180, 180))
        self.pushButton_96.setStyleSheet(u"border-radius:90; background-color:white;")
        self.pushButton_96.setIconSize(QSize(100, 100))

        self.horizontalLayout_127.addWidget(self.pushButton_96)

        self.pushButton_95 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_95.setObjectName(u"pushButton_95")
        self.pushButton_95.setMinimumSize(QSize(180, 180))
        self.pushButton_95.setStyleSheet(u"border-radius:90; background-color:white;")
        self.pushButton_95.setIconSize(QSize(100, 100))

        self.horizontalLayout_127.addWidget(self.pushButton_95)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.frame_230 = QFrame(self.frame)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setMinimumSize(QSize(30, 0))
        self.frame_230.setMaximumSize(QSize(50, 16777215))
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_230)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.rightButton_19 = QPushButton(self.frame_230)
        self.rightButton_19.setObjectName(u"rightButton_19")
        self.rightButton_19.setFont(font3)
        self.rightButton_19.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.rightButton_19)


        self.horizontalLayout_3.addWidget(self.frame_230)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(500, 0))
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
        self.frame_116.setMinimumSize(QSize(100, 0))
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
        self.label_100.setPixmap(QPixmap(u"icons/mail.png"))
        self.label_100.setScaledContents(True)
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_131.addWidget(self.label_100)

        self.label_101 = QLabel(self.frame_116)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"border:none;")

        self.horizontalLayout_131.addWidget(self.label_101, 0, Qt.AlignRight)


        self.horizontalLayout_75.addWidget(self.frame_116, 0, Qt.AlignVCenter)

        self.label_Title_5 = QLabel(self.frame_222)
        self.label_Title_5.setObjectName(u"label_Title_5")
        self.label_Title_5.setFont(font4)
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
        self.label_102.setPixmap(QPixmap(u"icons/heart.png"))
        self.label_102.setScaledContents(True)
        self.label_102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_132.addWidget(self.label_102, 0, Qt.AlignLeft)

        self.label_103 = QLabel(self.frame_117)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"border:none;")

        self.horizontalLayout_132.addWidget(self.label_103, 0, Qt.AlignRight)


        self.horizontalLayout_75.addWidget(self.frame_117)


        self.verticalLayout_2.addWidget(self.frame_222)

        self.label_Artist_3 = QLabel(self.frame_15)
        self.label_Artist_3.setObjectName(u"label_Artist_3")
        self.label_Artist_3.setFont(font5)
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

        self.horizontalLayout_133.addWidget(self.label_184)

        self.label_185 = QLabel(self.frame_118)
        self.label_185.setObjectName(u"label_185")

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
        self.horizontalLayout_128 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalSlider_17 = QSlider(self.frame_11)
        self.horizontalSlider_17.setObjectName(u"horizontalSlider_17")
        self.horizontalSlider_17.setValue(25)
        self.horizontalSlider_17.setSliderPosition(25)
        self.horizontalSlider_17.setOrientation(Qt.Horizontal)

        self.horizontalLayout_128.addWidget(self.horizontalSlider_17)


        self.horizontalLayout_76.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_223)


        self.horizontalLayout_5.addWidget(self.frame_15)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(50, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        self.frame_12.setStyleSheet(u"border-radius: 10px;\n"
"  background-color: #6522f2;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.verticalSlider_16 = QSlider(self.frame_12)
        self.verticalSlider_16.setObjectName(u"verticalSlider_16")
        self.verticalSlider_16.setStyleSheet(u"")
        self.verticalSlider_16.setValue(40)
        self.verticalSlider_16.setOrientation(Qt.Vertical)

        self.horizontalLayout_129.addWidget(self.verticalSlider_16)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.pushButton_35 = QPushButton(self.frame_5)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"*{width: 66px;\n"
"  height: 30px;\n"
"  border-radius: 15px;\n"
"  color: #ffffff;\n"
"}  ")
        icon2 = QIcon()
        icon2.addFile(u"icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_35.setIcon(icon2)
        self.pushButton_35.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.pushButton_35, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedPages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_41 = QVBoxLayout(self.page2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_237 = QFrame(self.page2)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMaximumSize(QSize(16777215, 30))
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_237)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 50, 0)
        self.pushButton_23 = QPushButton(self.frame_237)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_79.addWidget(self.pushButton_23, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_41.addWidget(self.frame_237)

        self.frame_3 = QFrame(self.page2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_227 = QFrame(self.frame_3)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setMinimumSize(QSize(30, 0))
        self.frame_227.setMaximumSize(QSize(30, 16777215))
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.leftButton_11 = QPushButton(self.frame_227)
        self.leftButton_11.setObjectName(u"leftButton_11")
        self.leftButton_11.setGeometry(QRect(0, 200, 28, 36))
        self.leftButton_11.setFont(font3)
        self.leftButton_11.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.frame_227)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(480, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.frame_9)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(450, 0))
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_40 = QHBoxLayout(self.page_10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setSpacing(10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_111 = QLabel(self.page_10)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMaximumSize(QSize(140, 140))
        self.label_111.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_111.setPixmap(QPixmap(u"post2.jpg"))
        self.label_111.setScaledContents(True)
        self.label_111.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_111, 0, 1, 1, 1)

        self.label_113 = QLabel(self.page_10)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMaximumSize(QSize(140, 140))
        self.label_113.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_113.setPixmap(QPixmap(u"post4.jpg"))
        self.label_113.setScaledContents(True)
        self.label_113.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_113, 1, 0, 1, 1)

        self.label_112 = QLabel(self.page_10)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMaximumSize(QSize(140, 140))
        self.label_112.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_112.setPixmap(QPixmap(u"post5.jpg"))
        self.label_112.setScaledContents(True)
        self.label_112.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_112, 1, 1, 1, 1)

        self.label_116 = QLabel(self.page_10)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMaximumSize(QSize(140, 140))
        self.label_116.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_116.setPixmap(QPixmap(u"post6.jpg"))
        self.label_116.setScaledContents(True)
        self.label_116.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_116, 1, 2, 1, 1)

        self.label_115 = QLabel(self.page_10)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMaximumSize(QSize(140, 140))
        self.label_115.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_115.setPixmap(QPixmap(u"post3.jpg"))
        self.label_115.setScaledContents(True)
        self.label_115.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_115, 0, 2, 1, 1)

        self.label_114 = QLabel(self.page_10)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMaximumSize(QSize(140, 140))
        self.label_114.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_114.setPixmap(QPixmap(u"post1.jpg"))
        self.label_114.setScaledContents(True)
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_114, 0, 0, 1, 1)


        self.horizontalLayout_40.addLayout(self.gridLayout_11)

        self.stackedWidget_3.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_41 = QHBoxLayout(self.page_11)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setSpacing(10)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 10, 0, 10)
        self.label_129 = QLabel(self.page_11)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMaximumSize(QSize(120, 120))
        self.label_129.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_129, 1, 1, 1, 1)

        self.label_130 = QLabel(self.page_11)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMaximumSize(QSize(120, 120))
        self.label_130.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_130, 0, 1, 1, 1)

        self.label_131 = QLabel(self.page_11)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMaximumSize(QSize(120, 120))
        self.label_131.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_131.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_131, 1, 0, 1, 1)

        self.label_132 = QLabel(self.page_11)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMaximumSize(QSize(120, 120))
        self.label_132.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_132.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_132, 0, 0, 1, 1)

        self.label_134 = QLabel(self.page_11)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMaximumSize(QSize(120, 120))
        self.label_134.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_134.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_134, 0, 2, 1, 1)

        self.label_135 = QLabel(self.page_11)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMaximumSize(QSize(120, 120))
        self.label_135.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_135.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_135, 1, 2, 1, 1)


        self.horizontalLayout_41.addLayout(self.gridLayout_21)

        self.stackedWidget_3.addWidget(self.page_11)

        self.verticalLayout_7.addWidget(self.stackedWidget_3)

        self.frame_136 = QFrame(self.frame_9)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMaximumSize(QSize(16777215, 100))
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_137 = QFrame(self.frame_136)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_137)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_247 = QFrame(self.frame_137)
        self.frame_247.setObjectName(u"frame_247")
        self.frame_247.setFrameShape(QFrame.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_247)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_19 = QLabel(self.frame_247)
        self.label_Likes_19.setObjectName(u"label_Likes_19")

        self.horizontalLayout_91.addWidget(self.label_Likes_19)

        self.label_Title_10 = QLabel(self.frame_247)
        self.label_Title_10.setObjectName(u"label_Title_10")
        self.label_Title_10.setFont(font4)
        self.label_Title_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.label_Title_10)

        self.label_Likes_20 = QLabel(self.frame_247)
        self.label_Likes_20.setObjectName(u"label_Likes_20")

        self.horizontalLayout_91.addWidget(self.label_Likes_20, 0, Qt.AlignRight)


        self.verticalLayout_97.addWidget(self.frame_247)

        self.label_Artist_8 = QLabel(self.frame_137)
        self.label_Artist_8.setObjectName(u"label_Artist_8")
        self.label_Artist_8.setFont(font6)
        self.label_Artist_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.label_Artist_8)

        self.frame_248 = QFrame(self.frame_137)
        self.frame_248.setObjectName(u"frame_248")
        self.frame_248.setFrameShape(QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_248)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_194 = QLabel(self.frame_248)
        self.label_194.setObjectName(u"label_194")

        self.horizontalLayout_92.addWidget(self.label_194, 0, Qt.AlignLeft)

        self.horizontalSlider_22 = QSlider(self.frame_248)
        self.horizontalSlider_22.setObjectName(u"horizontalSlider_22")
        self.horizontalSlider_22.setValue(25)
        self.horizontalSlider_22.setSliderPosition(25)
        self.horizontalSlider_22.setOrientation(Qt.Horizontal)

        self.horizontalLayout_92.addWidget(self.horizontalSlider_22)

        self.label_195 = QLabel(self.frame_248)
        self.label_195.setObjectName(u"label_195")

        self.horizontalLayout_92.addWidget(self.label_195, 0, Qt.AlignRight)


        self.verticalLayout_97.addWidget(self.frame_248)


        self.horizontalLayout_49.addWidget(self.frame_137)


        self.verticalLayout_7.addWidget(self.frame_136)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(30, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalSlider_21 = QSlider(self.frame_10)
        self.verticalSlider_21.setObjectName(u"verticalSlider_21")
        self.verticalSlider_21.setGeometry(QRect(11, 320, 10, 181))
        sizePolicy.setHeightForWidth(self.verticalSlider_21.sizePolicy().hasHeightForWidth())
        self.verticalSlider_21.setSizePolicy(sizePolicy)
        self.verticalSlider_21.setValue(40)
        self.verticalSlider_21.setOrientation(Qt.Vertical)
        self.pushButton_47 = QPushButton(self.frame_10)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(1, 508, 30, 28))
        self.leftButton_13 = QPushButton(self.frame_10)
        self.leftButton_13.setObjectName(u"leftButton_13")
        self.leftButton_13.setGeometry(QRect(0, 200, 28, 36))
        self.leftButton_13.setFont(font3)
        self.leftButton_13.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.frame_10)


        self.verticalLayout_41.addWidget(self.frame_3)

        self.stackedPages.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.horizontalLayout_13 = QHBoxLayout(self.page3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.page3)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_16 = QFrame(self.page_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_133 = QLabel(self.frame_17)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMaximumSize(QSize(300, 70))
        self.label_133.setFont(font6)
        self.label_133.setStyleSheet(u"*{\n"
"  padding: 0px 10px 0 10px;\n"
"  border-radius: 33px;\n"
"  background-color: #6522f2;\n"
"color: #FFFFFF;\n"
"}")
        self.label_133.setFrameShape(QFrame.Box)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_133)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_25 = QFrame(self.frame_16)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 450))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_157 = QFrame(self.frame_25)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(50, 0))
        self.frame_157.setMaximumSize(QSize(50, 16777215))
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_157)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.leftButton_14 = QPushButton(self.frame_157)
        self.leftButton_14.setObjectName(u"leftButton_14")
        self.leftButton_14.setFont(font3)
        self.leftButton_14.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.leftButton_14)


        self.horizontalLayout_55.addWidget(self.frame_157)

        self.verticalLayout_113 = QVBoxLayout()
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.post2 = QPushButton(self.frame_25)
        self.post2.setObjectName(u"post2")
        self.post2.setMinimumSize(QSize(0, 100))
        self.post2.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.post2, 0, 1, 1, 1)

        self.post1 = QPushButton(self.frame_25)
        self.post1.setObjectName(u"post1")
        self.post1.setMinimumSize(QSize(0, 100))
        self.post1.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.post1, 0, 0, 1, 1)

        self.post3 = QPushButton(self.frame_25)
        self.post3.setObjectName(u"post3")
        self.post3.setMinimumSize(QSize(0, 100))
        self.post3.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.post3, 0, 2, 1, 1)

        self.post5 = QPushButton(self.frame_25)
        self.post5.setObjectName(u"post5")
        self.post5.setMinimumSize(QSize(0, 100))
        self.post5.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.post5, 1, 1, 1, 1)

        self.post4 = QPushButton(self.frame_25)
        self.post4.setObjectName(u"post4")
        self.post4.setMinimumSize(QSize(0, 100))
        self.post4.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.post4, 1, 0, 1, 1)

        self.post6 = QPushButton(self.frame_25)
        self.post6.setObjectName(u"post6")
        self.post6.setMinimumSize(QSize(0, 100))
        self.post6.setIconSize(QSize(20, 20))

        self.gridLayout_13.addWidget(self.post6, 1, 2, 1, 1)


        self.verticalLayout_113.addLayout(self.gridLayout_13)


        self.horizontalLayout_55.addLayout(self.verticalLayout_113)

        self.frame_160 = QFrame(self.frame_25)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(50, 0))
        self.frame_160.setMaximumSize(QSize(50, 16777215))
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_160)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.rightButton_14 = QPushButton(self.frame_160)
        self.rightButton_14.setObjectName(u"rightButton_14")
        self.rightButton_14.setFont(font3)
        self.rightButton_14.setStyleSheet(u"")

        self.verticalLayout_114.addWidget(self.rightButton_14)


        self.horizontalLayout_55.addWidget(self.frame_160)


        self.verticalLayout_11.addWidget(self.frame_25)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.stackedWidget_4.addWidget(self.page_5)
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.verticalLayout_116 = QVBoxLayout(self.page_25)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.frame_163 = QFrame(self.page_25)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_163)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.label_140 = QLabel(self.frame_163)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setFont(font7)
        self.label_140.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.label_140)

        self.frame_164 = QFrame(self.frame_163)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setMinimumSize(QSize(0, 350))
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_165 = QFrame(self.frame_164)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setMinimumSize(QSize(50, 0))
        self.frame_165.setMaximumSize(QSize(50, 16777215))
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_165)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.frame_166 = QFrame(self.frame_165)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMinimumSize(QSize(0, 150))
        self.frame_166.setMaximumSize(QSize(16777215, 150))
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)

        self.verticalLayout_118.addWidget(self.frame_166)

        self.leftButton_15 = QPushButton(self.frame_165)
        self.leftButton_15.setObjectName(u"leftButton_15")
        self.leftButton_15.setFont(font3)
        self.leftButton_15.setStyleSheet(u"")

        self.verticalLayout_118.addWidget(self.leftButton_15)

        self.frame_167 = QFrame(self.frame_165)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)

        self.verticalLayout_118.addWidget(self.frame_167)


        self.horizontalLayout_57.addWidget(self.frame_165)

        self.verticalLayout_119 = QVBoxLayout()
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setSpacing(10)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_164)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 100))
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_164)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 100))
        self.pushButton_13.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.pushButton_13, 1, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_164)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 100))
        self.pushButton_16.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.pushButton_16, 1, 2, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_164)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 100))
        self.pushButton_18.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.pushButton_18, 0, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_164)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 100))
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.pushButton_15, 1, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_164)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 100))
        self.pushButton_17.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.pushButton_17, 0, 2, 1, 1)


        self.verticalLayout_119.addLayout(self.gridLayout_14)


        self.horizontalLayout_57.addLayout(self.verticalLayout_119)

        self.frame_168 = QFrame(self.frame_164)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setMinimumSize(QSize(50, 0))
        self.frame_168.setMaximumSize(QSize(50, 16777215))
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_168)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.frame_169 = QFrame(self.frame_168)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setMinimumSize(QSize(0, 150))
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_169)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_120.addWidget(self.frame_169)

        self.rightButton_15 = QPushButton(self.frame_168)
        self.rightButton_15.setObjectName(u"rightButton_15")
        self.rightButton_15.setFont(font3)
        self.rightButton_15.setStyleSheet(u"")

        self.verticalLayout_120.addWidget(self.rightButton_15)

        self.frame_170 = QFrame(self.frame_168)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_170)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")

        self.verticalLayout_120.addWidget(self.frame_170)


        self.horizontalLayout_57.addWidget(self.frame_168)


        self.verticalLayout_117.addWidget(self.frame_164)


        self.verticalLayout_116.addWidget(self.frame_163)

        self.stackedWidget_4.addWidget(self.page_25)
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.verticalLayout_122 = QVBoxLayout(self.page_26)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.frame_171 = QFrame(self.page_26)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_171)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.label_147 = QLabel(self.frame_171)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font7)
        self.label_147.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.label_147)

        self.frame_172 = QFrame(self.frame_171)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setMinimumSize(QSize(0, 350))
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_173 = QFrame(self.frame_172)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMinimumSize(QSize(50, 0))
        self.frame_173.setMaximumSize(QSize(50, 16777215))
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_173)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.frame_174 = QFrame(self.frame_173)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setMinimumSize(QSize(0, 150))
        self.frame_174.setMaximumSize(QSize(16777215, 150))
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)

        self.verticalLayout_124.addWidget(self.frame_174)

        self.leftButton_16 = QPushButton(self.frame_173)
        self.leftButton_16.setObjectName(u"leftButton_16")
        self.leftButton_16.setFont(font3)
        self.leftButton_16.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.leftButton_16)

        self.frame_175 = QFrame(self.frame_173)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)

        self.verticalLayout_124.addWidget(self.frame_175)


        self.horizontalLayout_59.addWidget(self.frame_173)

        self.verticalLayout_125 = QVBoxLayout()
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(10)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_27 = QPushButton(self.frame_172)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(0, 100))
        self.pushButton_27.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.pushButton_27, 0, 2, 1, 1)

        self.pushButton_26 = QPushButton(self.frame_172)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 100))
        self.pushButton_26.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.pushButton_26, 0, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.frame_172)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 100))
        self.pushButton_22.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.pushButton_22, 0, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.frame_172)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 100))
        self.pushButton_21.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.pushButton_21, 1, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_172)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 100))
        self.pushButton_20.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.pushButton_20, 1, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_172)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 100))
        self.pushButton_19.setIconSize(QSize(20, 20))

        self.gridLayout_15.addWidget(self.pushButton_19, 1, 2, 1, 1)


        self.verticalLayout_125.addLayout(self.gridLayout_15)


        self.horizontalLayout_59.addLayout(self.verticalLayout_125)

        self.frame_176 = QFrame(self.frame_172)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(50, 0))
        self.frame_176.setMaximumSize(QSize(50, 16777215))
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_176)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.frame_177 = QFrame(self.frame_176)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setMinimumSize(QSize(0, 150))
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_126.addWidget(self.frame_177)

        self.rightButton_16 = QPushButton(self.frame_176)
        self.rightButton_16.setObjectName(u"rightButton_16")
        self.rightButton_16.setFont(font3)
        self.rightButton_16.setStyleSheet(u"")

        self.verticalLayout_126.addWidget(self.rightButton_16)

        self.frame_178 = QFrame(self.frame_176)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_178)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")

        self.verticalLayout_126.addWidget(self.frame_178)


        self.horizontalLayout_59.addWidget(self.frame_176)


        self.verticalLayout_123.addWidget(self.frame_172)


        self.verticalLayout_122.addWidget(self.frame_171)

        self.stackedWidget_4.addWidget(self.page_26)

        self.horizontalLayout_13.addWidget(self.stackedWidget_4)

        self.stackedPages.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.horizontalLayout_62 = QHBoxLayout(self.page4)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.stackedMusicPosts = QStackedWidget(self.page4)
        self.stackedMusicPosts.setObjectName(u"stackedMusicPosts")
        self.page_30 = QWidget()
        self.page_30.setObjectName(u"page_30")
        self.verticalLayout_133 = QVBoxLayout(self.page_30)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.frame_226 = QFrame(self.page_30)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setMinimumSize(QSize(0, 60))
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_226)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(130, -1, -1, -1)
        self.frame_235 = QFrame(self.frame_226)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setMaximumSize(QSize(300, 100))
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_235)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_46 = QLabel(self.frame_235)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setPixmap(QPixmap(u"laugh.png"))
        self.label_46.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_46, 0, 3, 1, 1)

        self.label_47 = QLabel(self.frame_235)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setPixmap(QPixmap(u"sad.png"))
        self.label_47.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_47, 0, 1, 1, 1)

        self.label_48 = QLabel(self.frame_235)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setPixmap(QPixmap(u"surprise.png"))
        self.label_48.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_48, 0, 2, 1, 1)

        self.label_49 = QLabel(self.frame_235)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setPixmap(QPixmap(u"love.png"))
        self.label_49.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_50 = QLabel(self.frame_235)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_50, 1, 0, 1, 1)

        self.label_51 = QLabel(self.frame_235)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_51, 1, 1, 1, 1)

        self.label_52 = QLabel(self.frame_235)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_52, 1, 2, 1, 1)

        self.label_53 = QLabel(self.frame_235)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_53, 1, 3, 1, 1)


        self.horizontalLayout_90.addWidget(self.frame_235)

        self.pushButton_65 = QPushButton(self.frame_226)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setStyleSheet(u"width:85px; height:35px;background-color:#6522f2; border-radius:15px;")

        self.horizontalLayout_90.addWidget(self.pushButton_65, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_133.addWidget(self.frame_226)

        self.frame_188 = QFrame(self.page_30)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_188)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.frame_189 = QFrame(self.frame_188)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_189)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(30, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_60 = QPushButton(self.frame_13)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setGeometry(QRect(0, 382, 31, 40))
        icon3 = QIcon()
        icon3.addFile(u"icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_60.setIcon(icon3)
        self.pushButton_60.setIconSize(QSize(35, 35))

        self.horizontalLayout_64.addWidget(self.frame_13)

        self.verticalLayout_137 = QVBoxLayout()
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.label_156 = QLabel(self.frame_189)
        self.label_156.setObjectName(u"label_156")

        self.verticalLayout_137.addWidget(self.label_156, 0, Qt.AlignHCenter)

        self.frame_193 = QFrame(self.frame_189)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setMinimumSize(QSize(0, 100))
        self.frame_193.setMaximumSize(QSize(16777215, 150))
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_193)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.frame_194 = QFrame(self.frame_193)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_194)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_Title_3 = QLabel(self.frame_194)
        self.label_Title_3.setObjectName(u"label_Title_3")
        self.label_Title_3.setFont(font8)
        self.label_Title_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_Title_3, 0, Qt.AlignHCenter)


        self.verticalLayout_138.addWidget(self.frame_194)

        self.label_157 = QLabel(self.frame_193)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMaximumSize(QSize(16777215, 30))
        self.label_157.setFont(font9)

        self.verticalLayout_138.addWidget(self.label_157, 0, Qt.AlignHCenter)

        self.frame_115 = QFrame(self.frame_193)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.label_158 = QLabel(self.frame_115)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setStyleSheet(u"*{color:#ffffff;}")

        self.horizontalLayout_130.addWidget(self.label_158)

        self.label_159 = QLabel(self.frame_115)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setStyleSheet(u"*{color:#ffffff;}")
        self.label_159.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_130.addWidget(self.label_159)


        self.verticalLayout_138.addWidget(self.frame_115)

        self.frame_195 = QFrame(self.frame_193)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setStyleSheet(u"*{\n"
"border-radius: 10px;\n"
"  background-color: #6522f2;\n"
"}")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_195)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_13 = QSlider(self.frame_195)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setStyleSheet(u"*{color: #FFFFFF;}")
        self.horizontalSlider_13.setValue(25)
        self.horizontalSlider_13.setSliderPosition(25)
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)

        self.horizontalLayout_66.addWidget(self.horizontalSlider_13)


        self.verticalLayout_138.addWidget(self.frame_195)


        self.verticalLayout_137.addWidget(self.frame_193)


        self.horizontalLayout_64.addLayout(self.verticalLayout_137)

        self.frame_196 = QFrame(self.frame_189)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(50, 0))
        self.frame_196.setMaximumSize(QSize(50, 16777215))
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_196)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.frame_197 = QFrame(self.frame_196)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMinimumSize(QSize(0, 150))
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_139.addWidget(self.frame_197)

        self.frame_198 = QFrame(self.frame_196)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_198)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalSlider_13 = QSlider(self.frame_198)
        self.verticalSlider_13.setObjectName(u"verticalSlider_13")
        self.verticalSlider_13.setValue(40)
        self.verticalSlider_13.setOrientation(Qt.Vertical)

        self.verticalLayout_140.addWidget(self.verticalSlider_13)


        self.verticalLayout_139.addWidget(self.frame_198)

        self.pushButton_2 = QPushButton(self.frame_196)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_139.addWidget(self.pushButton_2)


        self.horizontalLayout_64.addWidget(self.frame_196)


        self.verticalLayout_134.addWidget(self.frame_189)


        self.verticalLayout_133.addWidget(self.frame_188)

        self.stackedMusicPosts.addWidget(self.page_30)
        self.page_31 = QWidget()
        self.page_31.setObjectName(u"page_31")
        self.verticalLayout_141 = QVBoxLayout(self.page_31)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.frame_224 = QFrame(self.page_31)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setMinimumSize(QSize(0, 60))
        self.frame_224.setFrameShape(QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(130, -1, -1, -1)
        self.frame_225 = QFrame(self.frame_224)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setMaximumSize(QSize(300, 100))
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_225)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_33 = QLabel(self.frame_225)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setPixmap(QPixmap(u"laugh.png"))
        self.label_33.setScaledContents(True)

        self.gridLayout.addWidget(self.label_33, 0, 3, 1, 1)

        self.label_31 = QLabel(self.frame_225)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setPixmap(QPixmap(u"sad.png"))
        self.label_31.setScaledContents(True)

        self.gridLayout.addWidget(self.label_31, 0, 1, 1, 1)

        self.label_32 = QLabel(self.frame_225)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setPixmap(QPixmap(u"surprise.png"))
        self.label_32.setScaledContents(True)

        self.gridLayout.addWidget(self.label_32, 0, 2, 1, 1)

        self.label_24 = QLabel(self.frame_225)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u"love.png"))
        self.label_24.setScaledContents(True)

        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_34 = QLabel(self.frame_225)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_34, 1, 0, 1, 1)

        self.label_35 = QLabel(self.frame_225)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_35, 1, 1, 1, 1)

        self.label_36 = QLabel(self.frame_225)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_36, 1, 2, 1, 1)

        self.label_37 = QLabel(self.frame_225)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_37, 1, 3, 1, 1)


        self.horizontalLayout_77.addWidget(self.frame_225)

        self.pushButton_50 = QPushButton(self.frame_224)
        self.pushButton_50.setObjectName(u"pushButton_50")

        self.horizontalLayout_77.addWidget(self.pushButton_50, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_141.addWidget(self.frame_224)

        self.frame_236 = QFrame(self.page_31)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_236)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.frame_255 = QFrame(self.frame_236)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_255)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.pushButton_63 = QPushButton(self.frame_255)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_78.addWidget(self.pushButton_63, 0, Qt.AlignBottom)

        self.verticalLayout_172 = QVBoxLayout()
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.label_189 = QLabel(self.frame_255)
        self.label_189.setObjectName(u"label_189")

        self.verticalLayout_172.addWidget(self.label_189, 0, Qt.AlignHCenter)

        self.frame_259 = QFrame(self.frame_255)
        self.frame_259.setObjectName(u"frame_259")
        self.frame_259.setMinimumSize(QSize(0, 100))
        self.frame_259.setMaximumSize(QSize(16777215, 150))
        self.frame_259.setFrameShape(QFrame.StyledPanel)
        self.frame_259.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_259)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.frame_260 = QFrame(self.frame_259)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setFrameShape(QFrame.StyledPanel)
        self.frame_260.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_260)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_11 = QLabel(self.frame_260)
        self.label_Likes_11.setObjectName(u"label_Likes_11")

        self.horizontalLayout_85.addWidget(self.label_Likes_11)

        self.label_Title_4 = QLabel(self.frame_260)
        self.label_Title_4.setObjectName(u"label_Title_4")
        self.label_Title_4.setFont(font8)
        self.label_Title_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_Title_4, 0, Qt.AlignHCenter)

        self.label_Likes_4 = QLabel(self.frame_260)
        self.label_Likes_4.setObjectName(u"label_Likes_4")

        self.horizontalLayout_85.addWidget(self.label_Likes_4, 0, Qt.AlignRight)


        self.verticalLayout_173.addWidget(self.frame_260)

        self.label_198 = QLabel(self.frame_259)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMaximumSize(QSize(16777215, 30))
        self.label_198.setFont(font9)

        self.verticalLayout_173.addWidget(self.label_198, 0, Qt.AlignHCenter)

        self.frame_261 = QFrame(self.frame_259)
        self.frame_261.setObjectName(u"frame_261")
        self.frame_261.setFrameShape(QFrame.StyledPanel)
        self.frame_261.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_261)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.label_199 = QLabel(self.frame_261)
        self.label_199.setObjectName(u"label_199")

        self.horizontalLayout_96.addWidget(self.label_199, 0, Qt.AlignLeft)

        self.horizontalSlider_16 = QSlider(self.frame_261)
        self.horizontalSlider_16.setObjectName(u"horizontalSlider_16")
        self.horizontalSlider_16.setValue(25)
        self.horizontalSlider_16.setSliderPosition(25)
        self.horizontalSlider_16.setOrientation(Qt.Horizontal)

        self.horizontalLayout_96.addWidget(self.horizontalSlider_16)

        self.label_200 = QLabel(self.frame_261)
        self.label_200.setObjectName(u"label_200")

        self.horizontalLayout_96.addWidget(self.label_200, 0, Qt.AlignRight)


        self.verticalLayout_173.addWidget(self.frame_261)


        self.verticalLayout_172.addWidget(self.frame_259)


        self.horizontalLayout_78.addLayout(self.verticalLayout_172)

        self.frame_262 = QFrame(self.frame_255)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setMinimumSize(QSize(50, 0))
        self.frame_262.setMaximumSize(QSize(50, 16777215))
        self.frame_262.setFrameShape(QFrame.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_262)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.frame_263 = QFrame(self.frame_262)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setMinimumSize(QSize(0, 150))
        self.frame_263.setFrameShape(QFrame.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_263)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_174.addWidget(self.frame_263)

        self.frame_264 = QFrame(self.frame_262)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setFrameShape(QFrame.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.frame_264)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.verticalSlider_18 = QSlider(self.frame_264)
        self.verticalSlider_18.setObjectName(u"verticalSlider_18")
        self.verticalSlider_18.setValue(40)
        self.verticalSlider_18.setOrientation(Qt.Vertical)

        self.verticalLayout_175.addWidget(self.verticalSlider_18)

        self.pushButton_5 = QPushButton(self.frame_264)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_175.addWidget(self.pushButton_5)


        self.verticalLayout_174.addWidget(self.frame_264)


        self.horizontalLayout_78.addWidget(self.frame_262)


        self.verticalLayout_163.addWidget(self.frame_255)


        self.verticalLayout_141.addWidget(self.frame_236)

        self.stackedMusicPosts.addWidget(self.page_31)
        self.page_32 = QWidget()
        self.page_32.setObjectName(u"page_32")
        self.verticalLayout_148 = QVBoxLayout(self.page_32)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.frame_228 = QFrame(self.page_32)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setMinimumSize(QSize(0, 60))
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(130, -1, -1, -1)
        self.frame_238 = QFrame(self.frame_228)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setMaximumSize(QSize(300, 100))
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_238)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_38 = QLabel(self.frame_238)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setPixmap(QPixmap(u"laugh.png"))
        self.label_38.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_38, 0, 3, 1, 1)

        self.label_39 = QLabel(self.frame_238)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setPixmap(QPixmap(u"sad.png"))
        self.label_39.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_39, 0, 1, 1, 1)

        self.label_40 = QLabel(self.frame_238)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setPixmap(QPixmap(u"surprise.png"))
        self.label_40.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_40, 0, 2, 1, 1)

        self.label_41 = QLabel(self.frame_238)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"*{border-radius:50\n"
"}")
        self.label_41.setPixmap(QPixmap(u"love.png"))
        self.label_41.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_42 = QLabel(self.frame_238)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_42, 1, 0, 1, 1)

        self.label_43 = QLabel(self.frame_238)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_43, 1, 1, 1, 1)

        self.label_44 = QLabel(self.frame_238)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_44, 1, 2, 1, 1)

        self.label_45 = QLabel(self.frame_238)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_45, 1, 3, 1, 1)


        self.horizontalLayout_87.addWidget(self.frame_238)

        self.pushButton_64 = QPushButton(self.frame_228)
        self.pushButton_64.setObjectName(u"pushButton_64")

        self.horizontalLayout_87.addWidget(self.pushButton_64, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_148.addWidget(self.frame_228)

        self.frame_203 = QFrame(self.page_32)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_203)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.frame_204 = QFrame(self.frame_203)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_204)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.pushButton_62 = QPushButton(self.frame_204)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_69.addWidget(self.pushButton_62, 0, Qt.AlignBottom)

        self.verticalLayout_146 = QVBoxLayout()
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.label_162 = QLabel(self.frame_204)
        self.label_162.setObjectName(u"label_162")

        self.verticalLayout_146.addWidget(self.label_162, 0, Qt.AlignHCenter)

        self.frame_208 = QFrame(self.frame_204)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMinimumSize(QSize(0, 100))
        self.frame_208.setMaximumSize(QSize(16777215, 150))
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_208)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.frame_265 = QFrame(self.frame_208)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setFrameShape(QFrame.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_265)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_12 = QLabel(self.frame_265)
        self.label_Likes_12.setObjectName(u"label_Likes_12")

        self.horizontalLayout_70.addWidget(self.label_Likes_12)

        self.label_Title_6 = QLabel(self.frame_265)
        self.label_Title_6.setObjectName(u"label_Title_6")
        self.label_Title_6.setFont(font8)
        self.label_Title_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.label_Title_6, 0, Qt.AlignHCenter)

        self.label_Likes_5 = QLabel(self.frame_265)
        self.label_Likes_5.setObjectName(u"label_Likes_5")

        self.horizontalLayout_70.addWidget(self.label_Likes_5, 0, Qt.AlignRight)


        self.verticalLayout_147.addWidget(self.frame_265)

        self.label_163 = QLabel(self.frame_208)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(16777215, 30))
        self.label_163.setFont(font9)

        self.verticalLayout_147.addWidget(self.label_163, 0, Qt.AlignHCenter)

        self.frame_266 = QFrame(self.frame_208)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setFrameShape(QFrame.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_266)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.label_164 = QLabel(self.frame_266)
        self.label_164.setObjectName(u"label_164")

        self.horizontalLayout_98.addWidget(self.label_164, 0, Qt.AlignLeft)

        self.horizontalSlider_14 = QSlider(self.frame_266)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setValue(25)
        self.horizontalSlider_14.setSliderPosition(25)
        self.horizontalSlider_14.setOrientation(Qt.Horizontal)

        self.horizontalLayout_98.addWidget(self.horizontalSlider_14)

        self.label_165 = QLabel(self.frame_266)
        self.label_165.setObjectName(u"label_165")

        self.horizontalLayout_98.addWidget(self.label_165, 0, Qt.AlignRight)


        self.verticalLayout_147.addWidget(self.frame_266)


        self.verticalLayout_146.addWidget(self.frame_208)


        self.horizontalLayout_69.addLayout(self.verticalLayout_146)

        self.frame_267 = QFrame(self.frame_204)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setMinimumSize(QSize(50, 0))
        self.frame_267.setMaximumSize(QSize(50, 16777215))
        self.frame_267.setFrameShape(QFrame.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_267)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.frame_268 = QFrame(self.frame_267)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setMinimumSize(QSize(0, 150))
        self.frame_268.setFrameShape(QFrame.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_268)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_162.addWidget(self.frame_268)

        self.frame_269 = QFrame(self.frame_267)
        self.frame_269.setObjectName(u"frame_269")
        self.frame_269.setFrameShape(QFrame.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_269)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalSlider_14 = QSlider(self.frame_269)
        self.verticalSlider_14.setObjectName(u"verticalSlider_14")
        self.verticalSlider_14.setValue(40)
        self.verticalSlider_14.setOrientation(Qt.Vertical)

        self.verticalLayout_176.addWidget(self.verticalSlider_14)

        self.pushButton_6 = QPushButton(self.frame_269)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_176.addWidget(self.pushButton_6)


        self.verticalLayout_162.addWidget(self.frame_269)


        self.horizontalLayout_69.addWidget(self.frame_267)


        self.verticalLayout_143.addWidget(self.frame_204)


        self.verticalLayout_148.addWidget(self.frame_203)

        self.stackedMusicPosts.addWidget(self.page_32)

        self.horizontalLayout_62.addWidget(self.stackedMusicPosts)

        self.stackedPages.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.horizontalLayout_12 = QHBoxLayout(self.page5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_23 = QFrame(self.page5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(500, 300))
        self.frame_23.setMaximumSize(QSize(400, 400))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_23)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(300, 400))
        self.frame_6.setMaximumSize(QSize(600, 16777215))
        self.frame_6.setStyleSheet(u"*{\n"
"background-color: #6522f2;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 40, 50, 40)
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 50))
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet(u"*{color: black;background-color:#ffffff;\n"
"border-radius: 20px;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_7)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.label_21 = QLabel(self.frame_23)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(200, 16777215))
        self.label_21.setCursor(QCursor(Qt.ArrowCursor))
        self.label_21.setTabletTracking(False)
        self.label_21.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_21.setPixmap(QPixmap(u"lp.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.label_21)


        self.horizontalLayout_12.addWidget(self.frame_23, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedPages.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.horizontalLayout_14 = QHBoxLayout(self.page6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_8 = QFrame(self.page6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(400, 300))
        self.frame_8.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(20, 140, 371, 101))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setFont(font10)
        self.label.setStyleSheet(u"*{color:#ffffff;}")

        self.verticalLayout_9.addWidget(self.label)

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
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setStyleSheet(u"*{background-color:#ffffff;}")

        self.horizontalLayout_17.addWidget(self.lineEdit)

        self.pushButton_8 = QPushButton(self.frame_18)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setMaximumSize(QSize(50, 16777215))
        self.pushButton_8.setStyleSheet(u"*{color:black;background-color: #d9d9d9;}")

        self.horizontalLayout_17.addWidget(self.pushButton_8)


        self.verticalLayout_9.addWidget(self.frame_18)


        self.horizontalLayout_14.addWidget(self.frame_8)

        self.stackedPages.addWidget(self.page6)
        self.page7 = QWidget()
        self.page7.setObjectName(u"page7")
        self.verticalLayout_16 = QVBoxLayout(self.page7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_2 = QLabel(self.page7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 350))
        self.label_2.setFont(font11)

        self.verticalLayout_16.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_24 = QFrame(self.page7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_24)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(50, 0))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.pushButton_36 = QPushButton(self.frame_19)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(0, 170, 50, 28))
        self.pushButton_36.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.frame_19)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_27)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_229 = QFrame(self.frame_27)
        self.frame_229.setObjectName(u"frame_229")
        self.frame_229.setFrameShape(QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_229)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_Title_7 = QLabel(self.frame_229)
        self.label_Title_7.setObjectName(u"label_Title_7")
        self.label_Title_7.setFont(font4)
        self.label_Title_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.label_Title_7)


        self.verticalLayout_13.addWidget(self.frame_229)

        self.label_Artist_4 = QLabel(self.frame_27)
        self.label_Artist_4.setObjectName(u"label_Artist_4")
        self.label_Artist_4.setFont(font5)
        self.label_Artist_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_Artist_4)

        self.frame_231 = QFrame(self.frame_27)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_231)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_186 = QLabel(self.frame_231)
        self.label_186.setObjectName(u"label_186")

        self.horizontalLayout_82.addWidget(self.label_186, 0, Qt.AlignLeft)

        self.horizontalSlider_18 = QSlider(self.frame_231)
        self.horizontalSlider_18.setObjectName(u"horizontalSlider_18")
        self.horizontalSlider_18.setValue(25)
        self.horizontalSlider_18.setSliderPosition(25)
        self.horizontalSlider_18.setOrientation(Qt.Horizontal)

        self.horizontalLayout_82.addWidget(self.horizontalSlider_18)

        self.label_187 = QLabel(self.frame_231)
        self.label_187.setObjectName(u"label_187")

        self.horizontalLayout_82.addWidget(self.label_187, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_231)


        self.horizontalLayout_9.addWidget(self.frame_27)

        self.frame_219 = QFrame(self.frame_24)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMaximumSize(QSize(50, 16777215))
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_219)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalSlider_17 = QSlider(self.frame_219)
        self.verticalSlider_17.setObjectName(u"verticalSlider_17")
        self.verticalSlider_17.setValue(40)
        self.verticalSlider_17.setOrientation(Qt.Vertical)

        self.verticalLayout_157.addWidget(self.verticalSlider_17, 0, Qt.AlignHCenter)

        self.pushButton_39 = QPushButton(self.frame_219)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.verticalLayout_157.addWidget(self.pushButton_39)


        self.horizontalLayout_9.addWidget(self.frame_219)


        self.verticalLayout_16.addWidget(self.frame_24)

        self.stackedPages.addWidget(self.page7)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.verticalLayout_18 = QVBoxLayout(self.page8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_21 = QFrame(self.page8)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(500, 0))
        self.frame_21.setMaximumSize(QSize(250, 300))
        self.frame_21.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 40, 0, 0)
        self.label_4 = QLabel(self.frame_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 100))
        self.label_4.setMaximumSize(QSize(150, 150))
        self.label_4.setFont(font12)
        self.label_4.setPixmap(QPixmap(u"qr.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_21)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font10)
        self.label_3.setStyleSheet(u"*{color:#ffffff;}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_3)


        self.verticalLayout_18.addWidget(self.frame_21, 0, Qt.AlignHCenter)

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
        self.frame_46.setMinimumSize(QSize(0, 100))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.pushButton_9 = QPushButton(self.frame_46)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(440, 70, 93, 28))
        self.pushButton_9.setStyleSheet(u"*{width: 91px;\n"
"  height: 34px;\n"
"  border-radius: 10px;\n"
"  color: #ffffff;\n"
"  background-color: #6522f2;}")
        self.label_15 = QLabel(self.frame_46)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 341, 41))
        self.label_15.setFont(font13)
        self.label_15.setStyleSheet(u"*{width: 312px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
" color:black; background-color: #2ae2e2;}")
        self.label_15.setFrameShape(QFrame.Box)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.frame_46)

        self.tabWidget = QTabWidget(self.frame_22)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color:black;")
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_26 = QFrame(self.tab)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 30))
        self.frame_28.setStyleSheet(u"background-color:white;")
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.label_5 = QLabel(self.frame_28)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:black;")
        self.label_5.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_19.addWidget(self.label_5)

        self.pushButton_10 = QPushButton(self.frame_28)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_10.setAutoRepeatDelay(305)

        self.horizontalLayout_19.addWidget(self.pushButton_10, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_28, 0, Qt.AlignVCenter)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_26)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.radioButton_4 = QRadioButton(self.frame_31)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"border:none;")
        self.radioButton_4.setChecked(True)

        self.horizontalLayout_20.addWidget(self.radioButton_4)

        self.label_6 = QLabel(self.frame_31)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border:none;")

        self.horizontalLayout_20.addWidget(self.label_6, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_26)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton_5 = QRadioButton(self.frame_32)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"border:none;")

        self.horizontalLayout_21.addWidget(self.radioButton_5)

        self.label_7 = QLabel(self.frame_32)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border:none;")

        self.horizontalLayout_21.addWidget(self.label_7, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_26)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_6 = QRadioButton(self.frame_33)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"border:none;")

        self.horizontalLayout_22.addWidget(self.radioButton_6)

        self.label_8 = QLabel(self.frame_33)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border:none;")

        self.horizontalLayout_22.addWidget(self.label_8, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_26)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton_7 = QRadioButton(self.frame_34)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"border:none;")

        self.horizontalLayout_23.addWidget(self.radioButton_7)

        self.label_9 = QLabel(self.frame_34)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border:none;")

        self.horizontalLayout_23.addWidget(self.label_9, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_34)


        self.verticalLayout_20.addWidget(self.frame_26)

        self.frame_35 = QFrame(self.tab)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_35)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_36 = QFrame(self.tab_2)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_36)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 30))
        self.frame_39.setStyleSheet(u"background-color:white; color:black;")
        self.frame_39.setFrameShape(QFrame.Box)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 0, 0, 0)
        self.label_10 = QLabel(self.frame_39)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_24.addWidget(self.label_10)

        self.pushButton_11 = QPushButton(self.frame_39)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(30, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"icons/search_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setIconSize(QSize(20, 20))
        self.pushButton_11.setAutoRepeatDelay(305)

        self.horizontalLayout_24.addWidget(self.pushButton_11, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_39, 0, Qt.AlignVCenter)

        self.frame_40 = QFrame(self.frame_36)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_36)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.radioButton_8 = QRadioButton(self.frame_41)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"border:none;")
        self.radioButton_8.setChecked(True)

        self.horizontalLayout_25.addWidget(self.radioButton_8)

        self.label_11 = QLabel(self.frame_41)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border:none;")

        self.horizontalLayout_25.addWidget(self.label_11, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_36)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.radioButton_9 = QRadioButton(self.frame_42)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"border:none;")

        self.horizontalLayout_26.addWidget(self.radioButton_9)

        self.label_12 = QLabel(self.frame_42)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border:none;")

        self.horizontalLayout_26.addWidget(self.label_12, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_36)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.radioButton_10 = QRadioButton(self.frame_43)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"border:none;")

        self.horizontalLayout_27.addWidget(self.radioButton_10)

        self.label_13 = QLabel(self.frame_43)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border:none;")

        self.horizontalLayout_27.addWidget(self.label_13, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_36)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"border:2px solid #6522f2; border-radius: 10px;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.radioButton_11 = QRadioButton(self.frame_44)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"border:none;")

        self.horizontalLayout_28.addWidget(self.radioButton_11)

        self.label_14 = QLabel(self.frame_44)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border:none;")

        self.horizontalLayout_28.addWidget(self.label_14, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_44)


        self.verticalLayout_24.addWidget(self.frame_36)

        self.frame_45 = QFrame(self.tab_2)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_45)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_19.addWidget(self.tabWidget)


        self.verticalLayout_22.addWidget(self.frame_22)

        self.stackedPages.addWidget(self.page9)
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")
        self.verticalLayout_28 = QVBoxLayout(self.page10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_49 = QFrame(self.page10)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 80))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_49)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 271, 41))
        self.label_18.setFont(font14)
        self.label_18.setFrameShape(QFrame.Box)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.frame_49)

        self.label_16 = QLabel(self.page10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 200))
        self.label_16.setFont(font15)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_16)

        self.frame_111 = QFrame(self.page10)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMaximumSize(QSize(16777215, 16777215))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.frame_112 = QFrame(self.frame_111)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(50, 0))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.pushButton_91 = QPushButton(self.frame_112)
        self.pushButton_91.setObjectName(u"pushButton_91")
        self.pushButton_91.setGeometry(QRect(0, 220, 50, 28))
        self.pushButton_91.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_124.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_111)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_113)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_257 = QFrame(self.frame_113)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_257)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_Title_16 = QLabel(self.frame_257)
        self.label_Title_16.setObjectName(u"label_Title_16")
        self.label_Title_16.setFont(font4)
        self.label_Title_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_125.addWidget(self.label_Title_16)


        self.verticalLayout_66.addWidget(self.frame_257)

        self.label_Artist_7 = QLabel(self.frame_113)
        self.label_Artist_7.setObjectName(u"label_Artist_7")
        self.label_Artist_7.setFont(font5)
        self.label_Artist_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.label_Artist_7)

        self.frame_258 = QFrame(self.frame_113)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setFrameShape(QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_258)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_206 = QLabel(self.frame_258)
        self.label_206.setObjectName(u"label_206")

        self.horizontalLayout_126.addWidget(self.label_206, 0, Qt.AlignLeft)

        self.horizontalSlider_26 = QSlider(self.frame_258)
        self.horizontalSlider_26.setObjectName(u"horizontalSlider_26")
        self.horizontalSlider_26.setValue(25)
        self.horizontalSlider_26.setSliderPosition(25)
        self.horizontalSlider_26.setOrientation(Qt.Horizontal)

        self.horizontalLayout_126.addWidget(self.horizontalSlider_26)

        self.label_207 = QLabel(self.frame_258)
        self.label_207.setObjectName(u"label_207")

        self.horizontalLayout_126.addWidget(self.label_207, 0, Qt.AlignRight)


        self.verticalLayout_66.addWidget(self.frame_258)


        self.horizontalLayout_124.addWidget(self.frame_113)

        self.frame_284 = QFrame(self.frame_111)
        self.frame_284.setObjectName(u"frame_284")
        self.frame_284.setMaximumSize(QSize(50, 16777215))
        self.frame_284.setFrameShape(QFrame.StyledPanel)
        self.frame_284.setFrameShadow(QFrame.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.frame_284)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalSlider_26 = QSlider(self.frame_284)
        self.verticalSlider_26.setObjectName(u"verticalSlider_26")
        self.verticalSlider_26.setValue(40)
        self.verticalSlider_26.setOrientation(Qt.Vertical)

        self.verticalLayout_183.addWidget(self.verticalSlider_26, 0, Qt.AlignHCenter)

        self.pushButton_92 = QPushButton(self.frame_284)
        self.pushButton_92.setObjectName(u"pushButton_92")

        self.verticalLayout_183.addWidget(self.pushButton_92)


        self.horizontalLayout_124.addWidget(self.frame_284)


        self.verticalLayout_28.addWidget(self.frame_111)

        self.stackedPages.addWidget(self.page10)
        self.page11 = QWidget()
        self.page11.setObjectName(u"page11")
        self.verticalLayout_29 = QVBoxLayout(self.page11)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_50 = QFrame(self.page11)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 80))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_50)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 411, 41))
        self.label_19.setFont(font14)
        self.label_19.setFrameShape(QFrame.Box)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.frame_114 = QFrame(self.frame_50)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setGeometry(QRect(30, 150, 500, 300))
        self.frame_114.setMinimumSize(QSize(500, 0))
        self.frame_114.setMaximumSize(QSize(250, 300))
        self.frame_114.setStyleSheet(u"*{background-color: #6522f2;}")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_114)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 40, 0, 0)
        self.frame_52 = QFrame(self.frame_114)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_52)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, -1, -1, -1)
        self.label_17 = QLabel(self.frame_52)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"*{color:#ffffff;}")

        self.verticalLayout_30.addWidget(self.label_17)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 50))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.frame_53)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setStyleSheet(u"*{background-color:#ffffff;}")

        self.horizontalLayout_30.addWidget(self.lineEdit_2)

        self.pushButton_12 = QPushButton(self.frame_53)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setMaximumSize(QSize(50, 16777215))
        self.pushButton_12.setStyleSheet(u"*{background-color: #d9d9d9;}")

        self.horizontalLayout_30.addWidget(self.pushButton_12)


        self.verticalLayout_30.addWidget(self.frame_53)


        self.verticalLayout_67.addWidget(self.frame_52, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_29.addWidget(self.frame_50)

        self.stackedPages.addWidget(self.page11)
        self.page12 = QWidget()
        self.page12.setObjectName(u"page12")
        self.label_20 = QLabel(self.page12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(80, 260, 411, 41))
        self.label_20.setFont(font7)
        self.label_20.setStyleSheet(u"*{width: 356px;\n"
"  height: 36px;\n"
"  border-radius: 20px;\n"
"  background-color: #2ae2e2;}")
        self.label_20.setFrameShape(QFrame.Box)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.stackedPages.addWidget(self.page12)

        self.horizontalLayout_2.addWidget(self.stackedPages)


        self.horizontalLayout_11.addWidget(self.main)


        self.verticalLayout_31.addWidget(self.display1)

        self.display2 = QFrame(self.frame_51)
        self.display2.setObjectName(u"display2")
        self.display2.setFrameShape(QFrame.StyledPanel)
        self.display2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.display2)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.stackedPages2 = QStackedWidget(self.display2)
        self.stackedPages2.setObjectName(u"stackedPages2")
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.verticalLayout_32 = QVBoxLayout(self.page_draw)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.page_draw)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setGeometry(QRect(0, 2, 431, 61))
        self.frame_57.setStyleSheet(u"background-color:white;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.pushButton_28 = QPushButton(self.frame_57)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setStyleSheet(u"*{width:40px; height:40px;background:#000000;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_28)

        self.pushButton_31 = QPushButton(self.frame_57)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"*{width:40px; height:40px;background:#F53333;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.frame_57)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"*{width:40px; height:40px;background:#EE6A1F;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.frame_57)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"*{width:40px; height:40px;background:#E7EA5B;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.frame_57)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setStyleSheet(u"*{width:40px; height:40px;background:#1ACB16;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_34)

        self.pushButton_52 = QPushButton(self.frame_57)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setStyleSheet(u"*{width:40px; height:40px;background:#4C25E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_52)

        self.pushButton_51 = QPushButton(self.frame_57)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setStyleSheet(u"*{width:40px; height:40px;background:#B525E8;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_51)

        self.pushButton_38 = QPushButton(self.frame_57)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setStyleSheet(u"*{width:40px; height:40px;background:#E8258E;color:#FFFFFF;border-radius:20;}")

        self.horizontalLayout_32.addWidget(self.pushButton_38)

        self.pushButton_25 = QPushButton(self.frame_57)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"*{width:40px; height:40px;background:#FFFFFF;color:#000000; border-radius:20;border:1px solid black;}")

        self.horizontalLayout_32.addWidget(self.pushButton_25)

        self.pushButton_37 = QPushButton(self.frame_55)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(650, 19, 121, 41))
        self.pushButton_37.setFont(font7)
        self.pushButton_37.setStyleSheet(u"background-color:white; color:black;")

        self.verticalLayout_32.addWidget(self.frame_55)

        self.painter_widget = painter.PainterWidget()
        self.painter_widget.setObjectName(u"painter_widget")
        self.painter_widget.setMinimumSize(QSize(0, 430))
        self.painter_widget.setStyleSheet(u"background-color:white;")

        self.verticalLayout_32.addWidget(self.painter_widget)

        self.frame_56 = QFrame(self.page_draw)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_56)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 20, 521, 31))
        self.label_22.setFont(font10)
        self.label_22.setToolTipDuration(0)
        self.pushButton_53 = QPushButton(self.frame_56)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setGeometry(QRect(660, 10, 111, 41))
        self.pushButton_53.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_53.setStyleSheet(u"width: 102px;\n"
"height: 45px;\n"
"left: 548px;\n"
"top: 902px;\n"
"\n"
"background: #6522F2;\n"
"border-radius: 20px;")

        self.verticalLayout_32.addWidget(self.frame_56)

        self.stackedPages2.addWidget(self.page_draw)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_33 = QVBoxLayout(self.page_search)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_58 = QFrame(self.page_search)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_58)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(11, 11, 11, 11)
        self.label_23 = QLabel(self.frame_58)
        self.label_23.setObjectName(u"label_23")
        font17 = QFont()
        font17.setPointSize(13)
        self.label_23.setFont(font17)

        self.verticalLayout_34.addWidget(self.label_23)

        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 400))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(500, 0))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.pushButton_54 = QPushButton(self.frame_61)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setGeometry(QRect(140, 130, 211, 101))
        self.pushButton_54.setFont(font1)

        self.horizontalLayout_33.addWidget(self.frame_61)

        self.label_27 = QLabel(self.frame_59)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(200, 16777215))
        self.label_27.setPixmap(QPixmap(u"lp.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_27)


        self.verticalLayout_34.addWidget(self.frame_59)


        self.verticalLayout_33.addWidget(self.frame_58)

        self.stackedPages2.addWidget(self.page_search)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_173 = QHBoxLayout(self.page)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.lineEdit_8 = QLineEdit(self.page)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 600))

        self.horizontalLayout_173.addWidget(self.lineEdit_8)

        self.stackedPages2.addWidget(self.page)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout_35 = QVBoxLayout(self.page_login)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.pushButton_24 = QPushButton(self.page_login)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_35.addWidget(self.pushButton_24, 0, Qt.AlignLeft)

        self.frame_62 = QFrame(self.page_login)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 400))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_62)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 30, 0, 0)
        self.label_25 = QLabel(self.frame_62)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 300))
        font18 = QFont()
        font18.setPointSize(28)
        self.label_25.setFont(font18)
        self.label_25.setPixmap(QPixmap(u"qr.png"))

        self.verticalLayout_36.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.label_26 = QLabel(self.frame_62)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(430, 0))
        self.label_26.setFont(font17)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_26, 0, Qt.AlignHCenter)


        self.verticalLayout_35.addWidget(self.frame_62)

        self.stackedPages2.addWidget(self.page_login)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_60 = QFrame(self.page_3)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setGeometry(QRect(0, 0, 760, 438))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_60)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(11, 11, 11, 11)
        self.frame_65 = QFrame(self.frame_60)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 400))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(500, 0))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.pushButton_57 = QPushButton(self.frame_66)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setGeometry(QRect(140, 130, 211, 101))
        self.pushButton_57.setFont(font1)

        self.horizontalLayout_35.addWidget(self.frame_66)

        self.label_30 = QLabel(self.frame_65)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(200, 16777215))
        self.label_30.setPixmap(QPixmap(u"lp.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_30)


        self.verticalLayout_38.addWidget(self.frame_65)

        self.stackedPages2.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_174 = QHBoxLayout(self.page_2)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.frame_63 = QFrame(self.page_2)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 0))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.frame_64 = QFrame(self.frame_63)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(500, 0))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_64)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.pushButton_55 = QPushButton(self.frame_64)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setMinimumSize(QSize(200, 100))
        self.pushButton_55.setFont(font1)

        self.verticalLayout_37.addWidget(self.pushButton_55, 0, Qt.AlignHCenter)

        self.pushButton_56 = QPushButton(self.frame_64)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMinimumSize(QSize(200, 100))
        self.pushButton_56.setFont(font1)

        self.verticalLayout_37.addWidget(self.pushButton_56, 0, Qt.AlignHCenter)


        self.horizontalLayout_34.addWidget(self.frame_64)

        self.label_28 = QLabel(self.frame_63)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(200, 16777215))
        self.label_28.setPixmap(QPixmap(u"lp.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_28)


        self.horizontalLayout_174.addWidget(self.frame_63)

        self.stackedPages2.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_39 = QVBoxLayout(self.page_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_29 = QLabel(self.page_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setPixmap(QPixmap(u"../../../Users/snghs/PycharmProjects/audiro/venv/keyboard.jpg"))
        self.label_29.setScaledContents(True)

        self.verticalLayout_39.addWidget(self.label_29)

        self.stackedPages2.addWidget(self.page_4)

        self.horizontalLayout_54.addWidget(self.stackedPages2)


        self.verticalLayout_31.addWidget(self.display2)


        self.horizontalLayout_31.addWidget(self.frame_51)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_toolBox.currentChanged.connect(MainWindow.changeMenu)
        self.pushButton_57.clicked.connect(MainWindow.draw)
        self.pushButton_24.clicked.connect(MainWindow.login)
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
        self.pushButton_53.clicked.connect(MainWindow.painterClear)
        self.pushButton_64.clicked.connect(MainWindow.backToPosts)
        self.pushButton_8.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_65.clicked.connect(MainWindow.backToPosts)
        self.pushButton_12.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_4.clicked.connect(MainWindow.moveToReceivedMail)
        self.pushButton_7.clicked.connect(MainWindow.moveToSendMail)
        self.pushButton_9.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_50.clicked.connect(MainWindow.backToPosts)
        self.pushButton_23.clicked.connect(MainWindow.backToChart)
        self.pushButton_97.clicked.connect(MainWindow.playMusic1_chart)
        self.pushButton_40.clicked.connect(MainWindow.playMusic2_chart)

        self.menu_toolBox.setCurrentIndex(2)
        self.menu_toolBox.layout().setSpacing(7)
        self.stackedPages_2.setCurrentIndex(3)
        self.stackedWidget_5.setCurrentIndex(1)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedMusicPosts_2.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedPages.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedMusicPosts.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Name_4.setText(QCoreApplication.translate("MainWindow", u"Audi:ro", None))
        self.menu_toolBox.setItemText(self.menu_toolBox.indexOf(self.menuPage1), QCoreApplication.translate("MainWindow", u"\uba40\ucea0:\ub85c\uc758 \uc778\uae30\ucc28\ud2b8", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \ucd94\ucc9c\ud558\uae30", None))
        self.menu_toolBox.setItemText(self.menu_toolBox.indexOf(self.menuPage2), QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \uc120\ubb3c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ud655\uc778\ud558\uae30", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30", None))
        self.menu_toolBox.setItemText(self.menu_toolBox.indexOf(self.menuPage3), QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0\ud568", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.label_54.setText("")
        self.tag1_2.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\uadfc", None))
        self.tag2_2.setText(QCoreApplication.translate("MainWindow", u"\ud1f4\uadfc", None))
        self.tag3_2.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\ub0a8", None))
        self.tag4_2.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\uc6b8", None))
        self.tag5_2.setText(QCoreApplication.translate("MainWindow", u"\uc6b4\ub3d9", None))
        self.tag6_2.setText(QCoreApplication.translate("MainWindow", u"\ud734\uc2dd", None))
        self.priorityBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\ucd94\ucc9c\uc21c", None))
        self.priorityBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\ucd5c\uc2e0\uc21c", None))
        self.priorityBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc154\ud50c", None))

        self.full_listBox_2.setText(QCoreApplication.translate("MainWindow", u"\ub354\ubcf4\uae30", None))
        self.leftButton_20.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_41.setText("")
        self.rightButton_20.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_13.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_8.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Likes_14.setText(QCoreApplication.translate("MainWindow", u"\u2764  251450", None))
        self.label_Artist_5.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.leftButton_12.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_117.setText("")
        self.label_118.setText("")
        self.label_119.setText("")
        self.label_120.setText("")
        self.label_121.setText("")
        self.label_122.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_Likes_21.setText(QCoreApplication.translate("MainWindow", u"\u2764  48123", None))
        self.label_Title_11.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_22.setText(QCoreApplication.translate("MainWindow", u"\u2764  211450", None))
        self.label_Artist_9.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.rightButton_12.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_17.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.post2_2.setText(QCoreApplication.translate("MainWindow", u"Hype Boy \ucd94\ucc9c", None))
        self.post1_2.setText(QCoreApplication.translate("MainWindow", u"DItto \ucd94\ucc9c", None))
        self.post3_2.setText(QCoreApplication.translate("MainWindow", u"Love Dive \ucd94\ucc9c", None))
        self.post5_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post4_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post6_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_17.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_18.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_18.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_21.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_21.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_55.setText("")
        self.label_56.setText("")
        self.label_57.setText("")
        self.label_58.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.pushButton_72.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.pushButton_73.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Ditto\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Title_9.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_74.setText("")
        self.label_63.setText("")
        self.label_64.setText("")
        self.label_65.setText("")
        self.label_66.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.pushButton_75.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Hype Boy\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Likes_15.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_12.setText(QCoreApplication.translate("MainWindow", u"Hype Boy", None))
        self.label_Likes_6.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_71.setText("")
        self.label_72.setText("")
        self.label_73.setText("")
        self.label_74.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.pushButton_79.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Love Dive\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Likes_16.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_13.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_7.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_81.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ud655\uc778\ud558\uae30", None))
        self.pushButton_82.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30", None))
        self.label_79.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\ubb38\uc790\ub85c \ubc1b\uc740 \uc778\uc99d \ucf54\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_83.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ub0b4\uc6a9(\ub2e4\ub978 \uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \uc791\uc131\ud55c \uc5fd\uc11c)", None))
        self.pushButton_84.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.label_Title_14.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Artist_6.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_85.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_82.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30\ub97c \uc6d0\ud558\uc2dc\uba74 \ub85c\uadf8\uc778\uc744 \ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_86.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc644\ub8cc", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"1\ub2e8\uacc4. \ud3b8\uc9c0\uc5d0 \ucca8\ubd80\ud560 \ub178\ub798\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.pushButton_87.setText(QCoreApplication.translate("MainWindow", u"\u2714", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\uac00\uc218 \uc774\ub984\uc73c\ub85c \uac80\uc0c9", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.pushButton_88.setText(QCoreApplication.translate("MainWindow", u"\u2714", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\ub178\ub798 \uc81c\ubaa9\uc73c\ub85c \uac80\uc0c9", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"2\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \uc791\uc131\ud574\uc8fc\uc138\uc694.", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Ditto \uc568\ubc94 \ucee4\ubc84", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Title_15.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Artist_10.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_89.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"3\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \ubcf4\ub0bc \uc0ac\ub78c\uc758 \uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694.", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.(-\ub294 \ube7c\uace0 \uc791\uc131\ud574\uc8fc\uc138\uc694)", None))
        self.pushButton_90.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc911\ud55c \ud3b8\uc9c0\uac00 \uc798 \uc804\ub2ec\ub418\uc5c8\uc2b5\ub2c8\ub2e4!", None))
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
        self.pushButton_97.setText("")
        self.pushButton_40.setText("")
        self.pushButton_93.setText("")
        self.pushButton_94.setText("")
        self.pushButton_96.setText("")
        self.pushButton_95.setText("")
        self.rightButton_19.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_100.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_Title_5.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_102.setText("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_Artist_3.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_35.setText("")
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.leftButton_11.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_111.setText("")
        self.label_113.setText("")
        self.label_112.setText("")
        self.label_116.setText("")
        self.label_115.setText("")
        self.label_114.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_Likes_19.setText(QCoreApplication.translate("MainWindow", u"\u2764  48123", None))
        self.label_Title_10.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_20.setText(QCoreApplication.translate("MainWindow", u"\u2764  211450", None))
        self.label_Artist_8.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.leftButton_13.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_14.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.post2.setText(QCoreApplication.translate("MainWindow", u"Hype Boy \ucd94\ucc9c", None))
        self.post1.setText(QCoreApplication.translate("MainWindow", u"DItto \ucd94\ucc9c", None))
        self.post3.setText(QCoreApplication.translate("MainWindow", u"Love Dive \ucd94\ucc9c", None))
        self.post5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.post6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_14.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_15.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_15.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545\uc744 \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\ub4e4\uc758 \uc5fd\uc11c \uae30\ub85d", None))
        self.leftButton_16.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightButton_16.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_46.setText("")
        self.label_47.setText("")
        self.label_48.setText("")
        self.label_49.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.pushButton_60.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Ditto\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Title_3.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_2.setText("")
        self.label_33.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_24.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Hype Boy\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Likes_11.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_4.setText(QCoreApplication.translate("MainWindow", u"Hype Boy", None))
        self.label_Likes_4.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.label_41.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"60126", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Love Dive\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Likes_12.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_6.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_5.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ud655\uc778\ud558\uae30", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30", None))
        self.label_21.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubb38\uc790\ub85c \ubc1b\uc740 \uc778\uc99d \ucf54\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ub0b4\uc6a9(\ub2e4\ub978 \uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \uc791\uc131\ud55c \uc5fd\uc11c)", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.label_Title_7.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Artist_4.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30\ub97c \uc6d0\ud558\uc2dc\uba74 \ub85c\uadf8\uc778\uc744 \ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc644\ub8cc", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1\ub2e8\uacc4. \ud3b8\uc9c0\uc5d0 \ucca8\ubd80\ud560 \ub178\ub798\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.pushButton_10.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uac00\uc218 \uc774\ub984\uc73c\ub85c \uac80\uc0c9", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.pushButton_11.setText("")
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ditto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\ub178\ub798 \uc81c\ubaa9\uc73c\ub85c \uac80\uc0c9", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"2\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \uc791\uc131\ud574\uc8fc\uc138\uc694.", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ditto \uc568\ubc94 \ucee4\ubc84", None))
        self.pushButton_91.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.label_Title_16.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Artist_7.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"3\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \ubcf4\ub0bc \uc0ac\ub78c\uc758 \uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694.", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.(-\ub294 \ube7c\uace0 \uc791\uc131\ud574\uc8fc\uc138\uc694)", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
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
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \uac80\uc0c9\ud558\uae30", None))
        self.label_27.setText("")
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30\uc640 \ub178\ub798\ucd94\ucc9c\ud558\uae30\ub294 \ub85c\uadf8\uc778 \ud6c4 \uc774\uc6a9 \uac00\ub2a5\ud569\ub2c8\ub2e4. \uc0c1\ub2e8 QR\ub85c \uc774\ub3d9\ud558\uc5ec \ub85c\uadf8\uc778 \ud68c\uc6d0\uac00\uc785\uc744 \uc9c4\ud589\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"\ub2f5\uc7a5\ud558\uae30", None))
        self.label_30.setText("")
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \ucd94\ucc9c\ud558\uae30", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ud558\uae30", None))
        self.label_28.setText("")
        self.label_29.setText("")
    # retranslateUi

