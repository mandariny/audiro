# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
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
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QStackedWidget, QStatusBar, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1122, 1089)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_31 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_51 = QFrame(self.centralwidget)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(800, 960))
        self.frame_51.setMaximumSize(QSize(800, 960))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_51)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_51)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(800, 480))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_5)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(200, 0))
        self.frame_37.setMaximumSize(QSize(200, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_37)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 220))
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
        self.menu_toolBox.setInputMethodHints(Qt.ImhNone)
        self.menu_toolBox.setLineWidth(1)
        self.menuPage1 = QWidget()
        self.menuPage1.setObjectName(u"menuPage1")
        self.menuPage1.setGeometry(QRect(0, 0, 194, 70))
        self.verticalLayout_26 = QVBoxLayout(self.menuPage1)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.menu_toolBox.addItem(self.menuPage1, u"\uba40\ucea0:\ub85c\uc758 \uc778\uae30\ucc28\ud2b8")
        self.menuPage2 = QWidget()
        self.menuPage2.setObjectName(u"menuPage2")
        self.menuPage2.setGeometry(QRect(0, 0, 194, 70))
        self.verticalLayout_107 = QVBoxLayout(self.menuPage2)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.pushButton_29 = QPushButton(self.menuPage2)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.verticalLayout_107.addWidget(self.pushButton_29, 0, Qt.AlignTop)

        self.pushButton_30 = QPushButton(self.menuPage2)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.verticalLayout_107.addWidget(self.pushButton_30, 0, Qt.AlignTop)

        self.menu_toolBox.addItem(self.menuPage2, u"\uc74c\uc545 \uc120\ubb3c")
        self.menuPage3 = QWidget()
        self.menuPage3.setObjectName(u"menuPage3")
        self.menuPage3.setGeometry(QRect(0, 0, 173, 85))
        self.verticalLayout_4 = QVBoxLayout(self.menuPage3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.menuPage3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton, 0, Qt.AlignTop)

        self.pushButton_3 = QPushButton(self.menuPage3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3, 0, Qt.AlignTop)

        self.menu_toolBox.addItem(self.menuPage3, u"\ud3b8\uc9c0\ud568")

        self.verticalLayout_106.addWidget(self.menu_toolBox)


        self.verticalLayout_105.addWidget(self.frame_151)


        self.verticalLayout_25.addWidget(self.frame_38)

        self.frame_152 = QFrame(self.frame_37)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_152)


        self.horizontalLayout_11.addWidget(self.frame_37)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 480))
        self.frame_2.setMaximumSize(QSize(800, 480))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedPages = QStackedWidget(self.frame_2)
        self.stackedPages.setObjectName(u"stackedPages")
        self.stackedPages.setMaximumSize(QSize(800, 480))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_3 = QVBoxLayout(self.page1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.page1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
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
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(100, 30))
        self.frame_9.setMaximumSize(QSize(100, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
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
        self.frame_11.setMinimumSize(QSize(100, 30))
        self.frame_11.setMaximumSize(QSize(100, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.full_listBox = QPushButton(self.frame_11)
        self.full_listBox.setObjectName(u"full_listBox")

        self.horizontalLayout_3.addWidget(self.full_listBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_7)

        self.stackedCharts = QStackedWidget(self.frame_4)
        self.stackedCharts.setObjectName(u"stackedCharts")
        self.chart1 = QWidget()
        self.chart1.setObjectName(u"chart1")
        self.verticalLayout_156 = QVBoxLayout(self.chart1)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.frame_12 = QFrame(self.chart1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 230))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_220 = QFrame(self.frame_12)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setMinimumSize(QSize(50, 0))
        self.frame_220.setMaximumSize(QSize(50, 16777215))
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_220)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.leftButton_19 = QPushButton(self.frame_220)
        self.leftButton_19.setObjectName(u"leftButton_19")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.leftButton_19.setFont(font2)
        self.leftButton_19.setStyleSheet(u"")

        self.verticalLayout_155.addWidget(self.leftButton_19)


        self.horizontalLayout_5.addWidget(self.frame_220)

        self.pushButton_40 = QPushButton(self.frame_12)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(200, 150))
        self.pushButton_40.setIconSize(QSize(100, 100))

        self.horizontalLayout_5.addWidget(self.pushButton_40)

        self.frame_230 = QFrame(self.frame_12)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setMinimumSize(QSize(50, 0))
        self.frame_230.setMaximumSize(QSize(50, 16777215))
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_230)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.rightButton_19 = QPushButton(self.frame_230)
        self.rightButton_19.setObjectName(u"rightButton_19")
        self.rightButton_19.setFont(font2)
        self.rightButton_19.setStyleSheet(u"")

        self.horizontalLayout_81.addWidget(self.rightButton_19)


        self.horizontalLayout_5.addWidget(self.frame_230)


        self.verticalLayout_156.addWidget(self.frame_12)

        self.frame = QFrame(self.chart1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 0, 0, 0)
        self.frame_222 = QFrame(self.frame_15)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setFrameShape(QFrame.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_222)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_9 = QLabel(self.frame_222)
        self.label_Likes_9.setObjectName(u"label_Likes_9")

        self.horizontalLayout_75.addWidget(self.label_Likes_9)

        self.label_Title_5 = QLabel(self.frame_222)
        self.label_Title_5.setObjectName(u"label_Title_5")
        font3 = QFont()
        font3.setPointSize(23)
        font3.setBold(True)
        self.label_Title_5.setFont(font3)
        self.label_Title_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_Title_5)

        self.label_Likes_10 = QLabel(self.frame_222)
        self.label_Likes_10.setObjectName(u"label_Likes_10")

        self.horizontalLayout_75.addWidget(self.label_Likes_10, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_222)

        self.label_Artist_3 = QLabel(self.frame_15)
        self.label_Artist_3.setObjectName(u"label_Artist_3")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_Artist_3.setFont(font4)
        self.label_Artist_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_Artist_3)

        self.frame_223 = QFrame(self.frame_15)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setFrameShape(QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_223)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_184 = QLabel(self.frame_223)
        self.label_184.setObjectName(u"label_184")

        self.horizontalLayout_76.addWidget(self.label_184, 0, Qt.AlignLeft)

        self.horizontalSlider_17 = QSlider(self.frame_223)
        self.horizontalSlider_17.setObjectName(u"horizontalSlider_17")
        self.horizontalSlider_17.setValue(25)
        self.horizontalSlider_17.setSliderPosition(25)
        self.horizontalSlider_17.setOrientation(Qt.Horizontal)

        self.horizontalLayout_76.addWidget(self.horizontalSlider_17)

        self.label_185 = QLabel(self.frame_223)
        self.label_185.setObjectName(u"label_185")

        self.horizontalLayout_76.addWidget(self.label_185, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_223)


        self.horizontalLayout_8.addWidget(self.frame_15)

        self.frame_219 = QFrame(self.frame)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMaximumSize(QSize(50, 16777215))
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_219)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalSlider_16 = QSlider(self.frame_219)
        self.verticalSlider_16.setObjectName(u"verticalSlider_16")
        self.verticalSlider_16.setValue(40)
        self.verticalSlider_16.setOrientation(Qt.Vertical)

        self.verticalLayout_157.addWidget(self.verticalSlider_16)

        self.pushButton_39 = QPushButton(self.frame_219)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.verticalLayout_157.addWidget(self.pushButton_39)


        self.horizontalLayout_8.addWidget(self.frame_219)


        self.verticalLayout_156.addWidget(self.frame)

        self.stackedCharts.addWidget(self.chart1)
        self.chart2 = QWidget()
        self.chart2.setObjectName(u"chart2")
        self.verticalLayout_158 = QVBoxLayout(self.chart2)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.frame_16 = QFrame(self.chart2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_138 = QFrame(self.frame_17)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(0, 230))
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_250 = QFrame(self.frame_138)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setMinimumSize(QSize(50, 0))
        self.frame_250.setMaximumSize(QSize(50, 16777215))
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_250)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.leftButton_23 = QPushButton(self.frame_250)
        self.leftButton_23.setObjectName(u"leftButton_23")
        self.leftButton_23.setFont(font2)
        self.leftButton_23.setStyleSheet(u"")

        self.verticalLayout_169.addWidget(self.leftButton_23)


        self.horizontalLayout_50.addWidget(self.frame_250)

        self.pushButton_48 = QPushButton(self.frame_138)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(200, 150))
        self.pushButton_48.setIconSize(QSize(100, 100))

        self.horizontalLayout_50.addWidget(self.pushButton_48)

        self.frame_251 = QFrame(self.frame_138)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(50, 0))
        self.frame_251.setMaximumSize(QSize(50, 16777215))
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_251)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.rightButton_23 = QPushButton(self.frame_251)
        self.rightButton_23.setObjectName(u"rightButton_23")
        self.rightButton_23.setFont(font2)
        self.rightButton_23.setStyleSheet(u"")

        self.horizontalLayout_93.addWidget(self.rightButton_23)


        self.horizontalLayout_50.addWidget(self.frame_251)


        self.verticalLayout_5.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.frame_17)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.frame_139)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_140)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(50, 0, 0, 0)
        self.frame_252 = QFrame(self.frame_140)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setFrameShape(QFrame.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_252)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_21 = QLabel(self.frame_252)
        self.label_Likes_21.setObjectName(u"label_Likes_21")

        self.horizontalLayout_94.addWidget(self.label_Likes_21)

        self.label_Title_11 = QLabel(self.frame_252)
        self.label_Title_11.setObjectName(u"label_Title_11")
        self.label_Title_11.setFont(font3)
        self.label_Title_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_Title_11)

        self.label_Likes_22 = QLabel(self.frame_252)
        self.label_Likes_22.setObjectName(u"label_Likes_22")

        self.horizontalLayout_94.addWidget(self.label_Likes_22, 0, Qt.AlignRight)


        self.verticalLayout_86.addWidget(self.frame_252)

        self.label_Artist_9 = QLabel(self.frame_140)
        self.label_Artist_9.setObjectName(u"label_Artist_9")
        self.label_Artist_9.setFont(font4)
        self.label_Artist_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_86.addWidget(self.label_Artist_9)

        self.frame_253 = QFrame(self.frame_140)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setFrameShape(QFrame.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_253)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_196 = QLabel(self.frame_253)
        self.label_196.setObjectName(u"label_196")

        self.horizontalLayout_95.addWidget(self.label_196, 0, Qt.AlignLeft)

        self.horizontalSlider_23 = QSlider(self.frame_253)
        self.horizontalSlider_23.setObjectName(u"horizontalSlider_23")
        self.horizontalSlider_23.setValue(25)
        self.horizontalSlider_23.setSliderPosition(25)
        self.horizontalSlider_23.setOrientation(Qt.Horizontal)

        self.horizontalLayout_95.addWidget(self.horizontalSlider_23)

        self.label_197 = QLabel(self.frame_253)
        self.label_197.setObjectName(u"label_197")

        self.horizontalLayout_95.addWidget(self.label_197, 0, Qt.AlignRight)


        self.verticalLayout_86.addWidget(self.frame_253)


        self.horizontalLayout_51.addWidget(self.frame_140)

        self.frame_254 = QFrame(self.frame_139)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setMaximumSize(QSize(50, 16777215))
        self.frame_254.setFrameShape(QFrame.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_254)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalSlider_22 = QSlider(self.frame_254)
        self.verticalSlider_22.setObjectName(u"verticalSlider_22")
        self.verticalSlider_22.setValue(40)
        self.verticalSlider_22.setOrientation(Qt.Vertical)

        self.verticalLayout_170.addWidget(self.verticalSlider_22)

        self.pushButton_49 = QPushButton(self.frame_254)
        self.pushButton_49.setObjectName(u"pushButton_49")

        self.verticalLayout_170.addWidget(self.pushButton_49)


        self.horizontalLayout_51.addWidget(self.frame_254)


        self.verticalLayout_5.addWidget(self.frame_139)


        self.horizontalLayout_10.addWidget(self.frame_17)


        self.verticalLayout_158.addWidget(self.frame_16)

        self.stackedCharts.addWidget(self.chart2)
        self.chart3 = QWidget()
        self.chart3.setObjectName(u"chart3")
        self.verticalLayout_160 = QVBoxLayout(self.chart3)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.frame_13 = QFrame(self.chart3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 230))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_221 = QFrame(self.frame_13)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setMinimumSize(QSize(50, 0))
        self.frame_221.setMaximumSize(QSize(50, 16777215))
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_221)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.leftButton_20 = QPushButton(self.frame_221)
        self.leftButton_20.setObjectName(u"leftButton_20")
        self.leftButton_20.setFont(font2)
        self.leftButton_20.setStyleSheet(u"")

        self.verticalLayout_164.addWidget(self.leftButton_20)


        self.horizontalLayout_9.addWidget(self.frame_221)

        self.pushButton_41 = QPushButton(self.frame_13)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(200, 150))
        self.pushButton_41.setIconSize(QSize(100, 100))

        self.horizontalLayout_9.addWidget(self.pushButton_41)

        self.frame_231 = QFrame(self.frame_13)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setMinimumSize(QSize(50, 0))
        self.frame_231.setMaximumSize(QSize(50, 16777215))
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_231)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.rightButton_20 = QPushButton(self.frame_231)
        self.rightButton_20.setObjectName(u"rightButton_20")
        self.rightButton_20.setFont(font2)
        self.rightButton_20.setStyleSheet(u"")

        self.horizontalLayout_82.addWidget(self.rightButton_20)


        self.horizontalLayout_9.addWidget(self.frame_231)


        self.verticalLayout_160.addWidget(self.frame_13)

        self.frame_141 = QFrame(self.chart3)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_142 = QFrame(self.frame_141)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_142)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(50, 0, 0, 0)
        self.frame_232 = QFrame(self.frame_142)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_232)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_15 = QLabel(self.frame_232)
        self.label_Likes_15.setObjectName(u"label_Likes_15")

        self.horizontalLayout_83.addWidget(self.label_Likes_15)

        self.label_Title_8 = QLabel(self.frame_232)
        self.label_Title_8.setObjectName(u"label_Title_8")
        self.label_Title_8.setFont(font3)
        self.label_Title_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_83.addWidget(self.label_Title_8)

        self.label_Likes_16 = QLabel(self.frame_232)
        self.label_Likes_16.setObjectName(u"label_Likes_16")

        self.horizontalLayout_83.addWidget(self.label_Likes_16, 0, Qt.AlignRight)


        self.verticalLayout_99.addWidget(self.frame_232)

        self.label_Artist_4 = QLabel(self.frame_142)
        self.label_Artist_4.setObjectName(u"label_Artist_4")
        self.label_Artist_4.setFont(font4)
        self.label_Artist_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_99.addWidget(self.label_Artist_4)

        self.frame_233 = QFrame(self.frame_142)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_233)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_186 = QLabel(self.frame_233)
        self.label_186.setObjectName(u"label_186")

        self.horizontalLayout_84.addWidget(self.label_186, 0, Qt.AlignLeft)

        self.horizontalSlider_18 = QSlider(self.frame_233)
        self.horizontalSlider_18.setObjectName(u"horizontalSlider_18")
        self.horizontalSlider_18.setValue(25)
        self.horizontalSlider_18.setSliderPosition(25)
        self.horizontalSlider_18.setOrientation(Qt.Horizontal)

        self.horizontalLayout_84.addWidget(self.horizontalSlider_18)

        self.label_187 = QLabel(self.frame_233)
        self.label_187.setObjectName(u"label_187")

        self.horizontalLayout_84.addWidget(self.label_187, 0, Qt.AlignRight)


        self.verticalLayout_99.addWidget(self.frame_233)


        self.horizontalLayout_52.addWidget(self.frame_142)

        self.frame_234 = QFrame(self.frame_141)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setMaximumSize(QSize(50, 16777215))
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_234)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalSlider_17 = QSlider(self.frame_234)
        self.verticalSlider_17.setObjectName(u"verticalSlider_17")
        self.verticalSlider_17.setValue(40)
        self.verticalSlider_17.setOrientation(Qt.Vertical)

        self.verticalLayout_168.addWidget(self.verticalSlider_17)

        self.pushButton_42 = QPushButton(self.frame_234)
        self.pushButton_42.setObjectName(u"pushButton_42")

        self.verticalLayout_168.addWidget(self.pushButton_42)


        self.horizontalLayout_52.addWidget(self.frame_234)


        self.verticalLayout_160.addWidget(self.frame_141)

        self.stackedCharts.addWidget(self.chart3)

        self.verticalLayout.addWidget(self.stackedCharts)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedPages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_41 = QVBoxLayout(self.page2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_3 = QFrame(self.page2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(600, 480))
        self.frame_3.setMaximumSize(QSize(800, 480))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedMemoPages = QStackedWidget(self.frame_3)
        self.stackedMemoPages.setObjectName(u"stackedMemoPages")
        self.MemoPage1 = QWidget()
        self.MemoPage1.setObjectName(u"MemoPage1")
        self.verticalLayout_84 = QVBoxLayout(self.MemoPage1)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.frame_27 = QFrame(self.MemoPage1)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 300))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_27)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_27)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_24)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_237 = QFrame(self.frame_24)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMaximumSize(QSize(16777215, 30))
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_237)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 50, 0)
        self.pushButton_23 = QPushButton(self.frame_237)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_79.addWidget(self.pushButton_23, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_237)

        self.frame_122 = QFrame(self.frame_24)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_227 = QFrame(self.frame_122)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setMaximumSize(QSize(30, 16777215))
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_227)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.leftButton_11 = QPushButton(self.frame_227)
        self.leftButton_11.setObjectName(u"leftButton_11")
        self.leftButton_11.setFont(font2)
        self.leftButton_11.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.leftButton_11)


        self.horizontalLayout_15.addWidget(self.frame_227)

        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 10, 0, 10)
        self.label_100 = QLabel(self.frame_123)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(120, 120))
        self.label_100.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_100, 0, 1, 1, 1)

        self.label_105 = QLabel(self.frame_123)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(120, 120))
        self.label_105.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_105.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_105, 1, 1, 1, 1)

        self.label_103 = QLabel(self.frame_123)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(120, 120))
        self.label_103.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_103.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_103, 1, 0, 1, 1)

        self.label_101 = QLabel(self.frame_123)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMaximumSize(QSize(120, 120))
        self.label_101.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_101.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_101, 0, 0, 1, 1)

        self.label_102 = QLabel(self.frame_123)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(120, 120))
        self.label_102.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_102.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_102, 0, 2, 1, 1)

        self.label_104 = QLabel(self.frame_123)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMaximumSize(QSize(120, 120))
        self.label_104.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_104.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_104, 1, 2, 1, 1)


        self.horizontalLayout_16.addLayout(self.gridLayout_10)


        self.horizontalLayout_15.addWidget(self.frame_123)

        self.frame_29 = QFrame(self.frame_122)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(30, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_29)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rightButton_11 = QPushButton(self.frame_29)
        self.rightButton_11.setObjectName(u"rightButton_11")
        self.rightButton_11.setFont(font2)
        self.rightButton_11.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.rightButton_11)


        self.horizontalLayout_15.addWidget(self.frame_29)


        self.verticalLayout_12.addWidget(self.frame_122)

        self.frame_120 = QFrame(self.frame_24)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMaximumSize(QSize(16777215, 100))
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.frame_120)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_121)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(50, 0, 0, 0)
        self.frame_240 = QFrame(self.frame_121)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_240)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_13 = QLabel(self.frame_240)
        self.label_Likes_13.setObjectName(u"label_Likes_13")

        self.horizontalLayout_80.addWidget(self.label_Likes_13)

        self.label_Title_7 = QLabel(self.frame_240)
        self.label_Title_7.setObjectName(u"label_Title_7")
        self.label_Title_7.setFont(font3)
        self.label_Title_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.label_Title_7)

        self.label_Likes_14 = QLabel(self.frame_240)
        self.label_Likes_14.setObjectName(u"label_Likes_14")

        self.horizontalLayout_80.addWidget(self.label_Likes_14, 0, Qt.AlignRight)


        self.verticalLayout_85.addWidget(self.frame_240)

        self.label_Artist_6 = QLabel(self.frame_121)
        self.label_Artist_6.setObjectName(u"label_Artist_6")
        self.label_Artist_6.setFont(font4)
        self.label_Artist_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_Artist_6)

        self.frame_241 = QFrame(self.frame_121)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_190 = QLabel(self.frame_241)
        self.label_190.setObjectName(u"label_190")

        self.horizontalLayout_86.addWidget(self.label_190, 0, Qt.AlignLeft)

        self.horizontalSlider_20 = QSlider(self.frame_241)
        self.horizontalSlider_20.setObjectName(u"horizontalSlider_20")
        self.horizontalSlider_20.setValue(25)
        self.horizontalSlider_20.setSliderPosition(25)
        self.horizontalSlider_20.setOrientation(Qt.Horizontal)

        self.horizontalLayout_86.addWidget(self.horizontalSlider_20)

        self.label_191 = QLabel(self.frame_241)
        self.label_191.setObjectName(u"label_191")

        self.horizontalLayout_86.addWidget(self.label_191, 0, Qt.AlignRight)


        self.verticalLayout_85.addWidget(self.frame_241)


        self.horizontalLayout_44.addWidget(self.frame_121)

        self.frame_242 = QFrame(self.frame_120)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMaximumSize(QSize(50, 16777215))
        self.frame_242.setFrameShape(QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_242)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalSlider_19 = QSlider(self.frame_242)
        self.verticalSlider_19.setObjectName(u"verticalSlider_19")
        self.verticalSlider_19.setValue(40)
        self.verticalSlider_19.setOrientation(Qt.Vertical)

        self.verticalLayout_161.addWidget(self.verticalSlider_19)

        self.pushButton_45 = QPushButton(self.frame_242)
        self.pushButton_45.setObjectName(u"pushButton_45")

        self.verticalLayout_161.addWidget(self.pushButton_45)


        self.horizontalLayout_44.addWidget(self.frame_242, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_120)


        self.verticalLayout_11.addWidget(self.frame_24)


        self.verticalLayout_84.addWidget(self.frame_27)

        self.stackedMemoPages.addWidget(self.MemoPage1)
        self.MemoPage2 = QWidget()
        self.MemoPage2.setObjectName(u"MemoPage2")
        self.verticalLayout_91 = QVBoxLayout(self.MemoPage2)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_130 = QFrame(self.MemoPage2)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_130)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.frame_130)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(0, 300))
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_124)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_124)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_125)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_238 = QFrame(self.frame_125)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setMaximumSize(QSize(16777215, 30))
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_238)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 50, 0)
        self.pushButton_24 = QPushButton(self.frame_238)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_87.addWidget(self.pushButton_24, 0, Qt.AlignRight)


        self.verticalLayout_88.addWidget(self.frame_238)

        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_228 = QFrame(self.frame_126)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setMaximumSize(QSize(30, 16777215))
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_228)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.leftButton_22 = QPushButton(self.frame_228)
        self.leftButton_22.setObjectName(u"leftButton_22")
        self.leftButton_22.setFont(font2)
        self.leftButton_22.setStyleSheet(u"")

        self.verticalLayout_89.addWidget(self.leftButton_22)


        self.horizontalLayout_45.addWidget(self.frame_228)

        self.frame_127 = QFrame(self.frame_126)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setSpacing(10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 10, 0, 10)
        self.label_106 = QLabel(self.frame_127)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(120, 120))
        self.label_106.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_106, 0, 1, 1, 1)

        self.label_107 = QLabel(self.frame_127)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMaximumSize(QSize(120, 120))
        self.label_107.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_107.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_107, 1, 1, 1, 1)

        self.label_108 = QLabel(self.frame_127)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(120, 120))
        self.label_108.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_108.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_108, 1, 0, 1, 1)

        self.label_109 = QLabel(self.frame_127)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMaximumSize(QSize(120, 120))
        self.label_109.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_109.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_109, 0, 0, 1, 1)

        self.label_110 = QLabel(self.frame_127)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMaximumSize(QSize(120, 120))
        self.label_110.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_110.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_110, 0, 2, 1, 1)

        self.label_182 = QLabel(self.frame_127)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMaximumSize(QSize(120, 120))
        self.label_182.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_182.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_182, 1, 2, 1, 1)


        self.horizontalLayout_46.addLayout(self.gridLayout_19)


        self.horizontalLayout_45.addWidget(self.frame_127)

        self.frame_128 = QFrame(self.frame_126)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMaximumSize(QSize(30, 16777215))
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_128)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.rightButton_22 = QPushButton(self.frame_128)
        self.rightButton_22.setObjectName(u"rightButton_22")
        self.rightButton_22.setFont(font2)
        self.rightButton_22.setStyleSheet(u"")

        self.verticalLayout_90.addWidget(self.rightButton_22)


        self.horizontalLayout_45.addWidget(self.frame_128)


        self.verticalLayout_88.addWidget(self.frame_126)

        self.frame_129 = QFrame(self.frame_125)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMaximumSize(QSize(16777215, 100))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_229 = QFrame(self.frame_129)
        self.frame_229.setObjectName(u"frame_229")
        self.frame_229.setFrameShape(QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_229)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(50, 0, 0, 0)
        self.frame_243 = QFrame(self.frame_229)
        self.frame_243.setObjectName(u"frame_243")
        self.frame_243.setFrameShape(QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_243)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_17 = QLabel(self.frame_243)
        self.label_Likes_17.setObjectName(u"label_Likes_17")

        self.horizontalLayout_88.addWidget(self.label_Likes_17)

        self.label_Title_9 = QLabel(self.frame_243)
        self.label_Title_9.setObjectName(u"label_Title_9")
        self.label_Title_9.setFont(font3)
        self.label_Title_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_88.addWidget(self.label_Title_9)

        self.label_Likes_18 = QLabel(self.frame_243)
        self.label_Likes_18.setObjectName(u"label_Likes_18")

        self.horizontalLayout_88.addWidget(self.label_Likes_18, 0, Qt.AlignRight)


        self.verticalLayout_159.addWidget(self.frame_243)

        self.label_Artist_7 = QLabel(self.frame_229)
        self.label_Artist_7.setObjectName(u"label_Artist_7")
        self.label_Artist_7.setFont(font4)
        self.label_Artist_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_159.addWidget(self.label_Artist_7)

        self.frame_244 = QFrame(self.frame_229)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setFrameShape(QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_244)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_192 = QLabel(self.frame_244)
        self.label_192.setObjectName(u"label_192")

        self.horizontalLayout_89.addWidget(self.label_192, 0, Qt.AlignLeft)

        self.horizontalSlider_21 = QSlider(self.frame_244)
        self.horizontalSlider_21.setObjectName(u"horizontalSlider_21")
        self.horizontalSlider_21.setValue(25)
        self.horizontalSlider_21.setSliderPosition(25)
        self.horizontalSlider_21.setOrientation(Qt.Horizontal)

        self.horizontalLayout_89.addWidget(self.horizontalSlider_21)

        self.label_193 = QLabel(self.frame_244)
        self.label_193.setObjectName(u"label_193")

        self.horizontalLayout_89.addWidget(self.label_193, 0, Qt.AlignRight)


        self.verticalLayout_159.addWidget(self.frame_244)


        self.horizontalLayout_74.addWidget(self.frame_229)

        self.frame_245 = QFrame(self.frame_129)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setMaximumSize(QSize(50, 16777215))
        self.frame_245.setFrameShape(QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_245)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalSlider_20 = QSlider(self.frame_245)
        self.verticalSlider_20.setObjectName(u"verticalSlider_20")
        self.verticalSlider_20.setValue(40)
        self.verticalSlider_20.setOrientation(Qt.Vertical)

        self.verticalLayout_166.addWidget(self.verticalSlider_20)

        self.pushButton_46 = QPushButton(self.frame_245)
        self.pushButton_46.setObjectName(u"pushButton_46")

        self.verticalLayout_166.addWidget(self.pushButton_46)


        self.horizontalLayout_74.addWidget(self.frame_245, 0, Qt.AlignRight)


        self.verticalLayout_88.addWidget(self.frame_129)


        self.verticalLayout_87.addWidget(self.frame_125)


        self.verticalLayout_92.addWidget(self.frame_124)


        self.verticalLayout_91.addWidget(self.frame_130)

        self.stackedMemoPages.addWidget(self.MemoPage2)
        self.MemoPage3 = QWidget()
        self.MemoPage3.setObjectName(u"MemoPage3")
        self.verticalLayout_98 = QVBoxLayout(self.MemoPage3)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.frame_131 = QFrame(self.MemoPage3)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setMinimumSize(QSize(0, 300))
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_131)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_132 = QFrame(self.frame_131)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_132)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.frame_239 = QFrame(self.frame_132)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setMaximumSize(QSize(16777215, 30))
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_239)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 50, 0)
        self.pushButton_25 = QPushButton(self.frame_239)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_90.addWidget(self.pushButton_25, 0, Qt.AlignRight)


        self.verticalLayout_94.addWidget(self.frame_239)

        self.frame_133 = QFrame(self.frame_132)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_246 = QFrame(self.frame_133)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setMaximumSize(QSize(30, 16777215))
        self.frame_246.setFrameShape(QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_246)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.leftButton_12 = QPushButton(self.frame_246)
        self.leftButton_12.setObjectName(u"leftButton_12")
        self.leftButton_12.setFont(font2)
        self.leftButton_12.setStyleSheet(u"")

        self.verticalLayout_95.addWidget(self.leftButton_12)


        self.horizontalLayout_47.addWidget(self.frame_246)

        self.frame_134 = QFrame(self.frame_133)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setSpacing(10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 10, 0, 10)
        self.label_111 = QLabel(self.frame_134)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMaximumSize(QSize(120, 120))
        self.label_111.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_111.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_111, 0, 1, 1, 1)

        self.label_112 = QLabel(self.frame_134)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMaximumSize(QSize(120, 120))
        self.label_112.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_112.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_112, 1, 1, 1, 1)

        self.label_113 = QLabel(self.frame_134)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMaximumSize(QSize(120, 120))
        self.label_113.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_113.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_113, 1, 0, 1, 1)

        self.label_114 = QLabel(self.frame_134)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMaximumSize(QSize(120, 120))
        self.label_114.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_114, 0, 0, 1, 1)

        self.label_115 = QLabel(self.frame_134)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMaximumSize(QSize(120, 120))
        self.label_115.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_115.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_115, 0, 2, 1, 1)

        self.label_116 = QLabel(self.frame_134)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMaximumSize(QSize(120, 120))
        self.label_116.setStyleSheet(u"*{background: rgb(255, 243, 149)\n"
"}")
        self.label_116.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_116, 1, 2, 1, 1)


        self.horizontalLayout_48.addLayout(self.gridLayout_11)


        self.horizontalLayout_47.addWidget(self.frame_134)

        self.frame_135 = QFrame(self.frame_133)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMaximumSize(QSize(30, 16777215))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_135)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.rightButton_12 = QPushButton(self.frame_135)
        self.rightButton_12.setObjectName(u"rightButton_12")
        self.rightButton_12.setFont(font2)
        self.rightButton_12.setStyleSheet(u"")

        self.verticalLayout_96.addWidget(self.rightButton_12)


        self.horizontalLayout_47.addWidget(self.frame_135)


        self.verticalLayout_94.addWidget(self.frame_133)

        self.frame_136 = QFrame(self.frame_132)
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
        self.verticalLayout_97.setContentsMargins(50, 0, 0, 0)
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
        self.label_Title_10.setFont(font3)
        self.label_Title_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.label_Title_10)

        self.label_Likes_20 = QLabel(self.frame_247)
        self.label_Likes_20.setObjectName(u"label_Likes_20")

        self.horizontalLayout_91.addWidget(self.label_Likes_20, 0, Qt.AlignRight)


        self.verticalLayout_97.addWidget(self.frame_247)

        self.label_Artist_8 = QLabel(self.frame_137)
        self.label_Artist_8.setObjectName(u"label_Artist_8")
        self.label_Artist_8.setFont(font4)
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

        self.frame_249 = QFrame(self.frame_136)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setMaximumSize(QSize(50, 16777215))
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_249)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalSlider_21 = QSlider(self.frame_249)
        self.verticalSlider_21.setObjectName(u"verticalSlider_21")
        self.verticalSlider_21.setValue(40)
        self.verticalSlider_21.setOrientation(Qt.Vertical)

        self.verticalLayout_167.addWidget(self.verticalSlider_21)

        self.pushButton_47 = QPushButton(self.frame_249)
        self.pushButton_47.setObjectName(u"pushButton_47")

        self.verticalLayout_167.addWidget(self.pushButton_47)


        self.horizontalLayout_49.addWidget(self.frame_249, 0, Qt.AlignRight)


        self.verticalLayout_94.addWidget(self.frame_136)


        self.verticalLayout_93.addWidget(self.frame_132)


        self.verticalLayout_98.addWidget(self.frame_131)

        self.stackedMemoPages.addWidget(self.MemoPage3)

        self.horizontalLayout_7.addWidget(self.stackedMemoPages)


        self.verticalLayout_41.addWidget(self.frame_3)

        self.stackedPages.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.horizontalLayout_13 = QHBoxLayout(self.page3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.stackedWidget_4 = QStackedWidget(self.page3)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_23 = QFrame(self.page_5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_133 = QLabel(self.frame_23)
        self.label_133.setObjectName(u"label_133")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_133.setFont(font5)
        self.label_133.setFrameShape(QFrame.Box)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_133, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 350))
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
        self.frame_158 = QFrame(self.frame_157)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(0, 150))
        self.frame_158.setMaximumSize(QSize(16777215, 150))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_158)

        self.leftButton_14 = QPushButton(self.frame_157)
        self.leftButton_14.setObjectName(u"leftButton_14")
        self.leftButton_14.setFont(font2)
        self.leftButton_14.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.leftButton_14)

        self.frame_159 = QFrame(self.frame_157)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_159)


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
        self.frame_161 = QFrame(self.frame_160)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(0, 150))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_114.addWidget(self.frame_161)

        self.rightButton_14 = QPushButton(self.frame_160)
        self.rightButton_14.setObjectName(u"rightButton_14")
        self.rightButton_14.setFont(font2)
        self.rightButton_14.setStyleSheet(u"")

        self.verticalLayout_114.addWidget(self.rightButton_14)

        self.frame_162 = QFrame(self.frame_160)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_162)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")

        self.verticalLayout_114.addWidget(self.frame_162)


        self.horizontalLayout_55.addWidget(self.frame_160)


        self.verticalLayout_13.addWidget(self.frame_25)


        self.verticalLayout_10.addWidget(self.frame_23)

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
        self.label_140.setFont(font5)
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
        self.leftButton_15.setFont(font2)
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
        self.rightButton_15.setFont(font2)
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
        self.label_147.setFont(font5)
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
        self.leftButton_16.setFont(font2)
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
        self.rightButton_16.setFont(font2)
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
        self.frame_184 = QFrame(self.page_30)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(0, 60))
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_63.addWidget(self.frame_185)

        self.label_154 = QLabel(self.frame_184)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_63.addWidget(self.label_154, 0, Qt.AlignHCenter)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_186 = QFrame(self.frame_184)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)

        self.gridLayout_16.addWidget(self.frame_186, 1, 0, 1, 1)

        self.pushButton_35 = QPushButton(self.frame_184)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.gridLayout_16.addWidget(self.pushButton_35, 1, 1, 1, 1)

        self.frame_187 = QFrame(self.frame_184)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)

        self.gridLayout_16.addWidget(self.frame_187, 0, 1, 1, 1)


        self.horizontalLayout_63.addLayout(self.gridLayout_16)


        self.verticalLayout_133.addWidget(self.frame_184)

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
        self.frame_190 = QFrame(self.frame_189)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setMinimumSize(QSize(50, 0))
        self.frame_190.setMaximumSize(QSize(50, 16777215))
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_190)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.frame_191 = QFrame(self.frame_190)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(0, 150))
        self.frame_191.setMaximumSize(QSize(16777215, 150))
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)

        self.verticalLayout_135.addWidget(self.frame_191)

        self.frame_192 = QFrame(self.frame_190)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_192)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.label_155 = QLabel(self.frame_192)
        self.label_155.setObjectName(u"label_155")
        font6 = QFont()
        font6.setPointSize(19)
        font6.setBold(True)
        font6.setUnderline(False)
        self.label_155.setFont(font6)
        self.label_155.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_136.addWidget(self.label_155, 0, Qt.AlignBottom)


        self.verticalLayout_135.addWidget(self.frame_192)


        self.horizontalLayout_64.addWidget(self.frame_190)

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
        self.label_Likes_8 = QLabel(self.frame_194)
        self.label_Likes_8.setObjectName(u"label_Likes_8")

        self.horizontalLayout_65.addWidget(self.label_Likes_8)

        self.label_Title_3 = QLabel(self.frame_194)
        self.label_Title_3.setObjectName(u"label_Title_3")
        font7 = QFont()
        font7.setPointSize(21)
        font7.setBold(True)
        self.label_Title_3.setFont(font7)
        self.label_Title_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_Title_3, 0, Qt.AlignHCenter)

        self.label_Likes_3 = QLabel(self.frame_194)
        self.label_Likes_3.setObjectName(u"label_Likes_3")

        self.horizontalLayout_65.addWidget(self.label_Likes_3, 0, Qt.AlignRight)


        self.verticalLayout_138.addWidget(self.frame_194)

        self.label_157 = QLabel(self.frame_193)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        self.label_157.setFont(font8)

        self.verticalLayout_138.addWidget(self.label_157, 0, Qt.AlignHCenter)

        self.frame_195 = QFrame(self.frame_193)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_195)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_158 = QLabel(self.frame_195)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_66.addWidget(self.label_158, 0, Qt.AlignLeft)

        self.horizontalSlider_13 = QSlider(self.frame_195)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setValue(25)
        self.horizontalSlider_13.setSliderPosition(25)
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)

        self.horizontalLayout_66.addWidget(self.horizontalSlider_13)

        self.label_159 = QLabel(self.frame_195)
        self.label_159.setObjectName(u"label_159")

        self.horizontalLayout_66.addWidget(self.label_159, 0, Qt.AlignRight)


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

        self.pushButton_2 = QPushButton(self.frame_198)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_140.addWidget(self.pushButton_2)


        self.verticalLayout_139.addWidget(self.frame_198)


        self.horizontalLayout_64.addWidget(self.frame_196)


        self.verticalLayout_134.addWidget(self.frame_189)


        self.verticalLayout_133.addWidget(self.frame_188)

        self.stackedMusicPosts.addWidget(self.page_30)
        self.page_31 = QWidget()
        self.page_31.setObjectName(u"page_31")
        self.verticalLayout_141 = QVBoxLayout(self.page_31)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.frame_236 = QFrame(self.page_31)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_236)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.frame_224 = QFrame(self.frame_236)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setMinimumSize(QSize(0, 60))
        self.frame_224.setFrameShape(QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.frame_225 = QFrame(self.frame_224)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_77.addWidget(self.frame_225)

        self.label_183 = QLabel(self.frame_224)
        self.label_183.setObjectName(u"label_183")

        self.horizontalLayout_77.addWidget(self.label_183, 0, Qt.AlignHCenter)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_226 = QFrame(self.frame_224)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)

        self.gridLayout_20.addWidget(self.frame_226, 1, 0, 1, 1)

        self.pushButton_50 = QPushButton(self.frame_224)
        self.pushButton_50.setObjectName(u"pushButton_50")

        self.gridLayout_20.addWidget(self.pushButton_50, 1, 1, 1, 1)

        self.frame_235 = QFrame(self.frame_224)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)

        self.gridLayout_20.addWidget(self.frame_235, 0, 1, 1, 1)


        self.horizontalLayout_77.addLayout(self.gridLayout_20)


        self.verticalLayout_163.addWidget(self.frame_224)

        self.frame_255 = QFrame(self.frame_236)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_255)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_256 = QFrame(self.frame_255)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setMinimumSize(QSize(50, 0))
        self.frame_256.setMaximumSize(QSize(50, 16777215))
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_256)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.frame_257 = QFrame(self.frame_256)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setMinimumSize(QSize(0, 150))
        self.frame_257.setMaximumSize(QSize(16777215, 150))
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)

        self.verticalLayout_165.addWidget(self.frame_257)

        self.frame_258 = QFrame(self.frame_256)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setFrameShape(QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_258)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.label_188 = QLabel(self.frame_258)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setFont(font6)
        self.label_188.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_171.addWidget(self.label_188, 0, Qt.AlignBottom)


        self.verticalLayout_165.addWidget(self.frame_258)


        self.horizontalLayout_78.addWidget(self.frame_256)

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
        self.label_Title_4.setFont(font7)
        self.label_Title_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.label_Title_4, 0, Qt.AlignHCenter)

        self.label_Likes_4 = QLabel(self.frame_260)
        self.label_Likes_4.setObjectName(u"label_Likes_4")

        self.horizontalLayout_85.addWidget(self.label_Likes_4, 0, Qt.AlignRight)


        self.verticalLayout_173.addWidget(self.frame_260)

        self.label_198 = QLabel(self.frame_259)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMaximumSize(QSize(16777215, 30))
        self.label_198.setFont(font8)

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
        self.frame_203 = QFrame(self.page_32)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_203)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.frame_199 = QFrame(self.frame_203)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setMinimumSize(QSize(0, 60))
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_199)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(11, 11, 11, 11)
        self.frame_200 = QFrame(self.frame_199)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_68.addWidget(self.frame_200)

        self.label_160 = QLabel(self.frame_199)
        self.label_160.setObjectName(u"label_160")

        self.horizontalLayout_68.addWidget(self.label_160, 0, Qt.AlignHCenter)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_201 = QFrame(self.frame_199)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)

        self.gridLayout_17.addWidget(self.frame_201, 1, 0, 1, 1)

        self.pushButton_36 = QPushButton(self.frame_199)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.gridLayout_17.addWidget(self.pushButton_36, 1, 1, 1, 1)

        self.frame_202 = QFrame(self.frame_199)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)

        self.gridLayout_17.addWidget(self.frame_202, 0, 1, 1, 1)


        self.horizontalLayout_68.addLayout(self.gridLayout_17)


        self.verticalLayout_143.addWidget(self.frame_199)

        self.frame_204 = QFrame(self.frame_203)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_204)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setMinimumSize(QSize(50, 0))
        self.frame_205.setMaximumSize(QSize(50, 16777215))
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_205)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.frame_206 = QFrame(self.frame_205)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMinimumSize(QSize(0, 150))
        self.frame_206.setMaximumSize(QSize(16777215, 150))
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)

        self.verticalLayout_144.addWidget(self.frame_206)

        self.frame_207 = QFrame(self.frame_205)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_207)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.label_161 = QLabel(self.frame_207)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font6)
        self.label_161.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_145.addWidget(self.label_161, 0, Qt.AlignBottom)


        self.verticalLayout_144.addWidget(self.frame_207)


        self.horizontalLayout_69.addWidget(self.frame_205)

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
        self.label_Title_6.setFont(font7)
        self.label_Title_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.label_Title_6, 0, Qt.AlignHCenter)

        self.label_Likes_5 = QLabel(self.frame_265)
        self.label_Likes_5.setObjectName(u"label_Likes_5")

        self.horizontalLayout_70.addWidget(self.label_Likes_5, 0, Qt.AlignRight)


        self.verticalLayout_147.addWidget(self.frame_265)

        self.label_163 = QLabel(self.frame_208)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(16777215, 30))
        self.label_163.setFont(font8)

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
        self.frame_6 = QFrame(self.page5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 400))
        self.frame_6.setMaximumSize(QSize(400, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 100))

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 100))

        self.verticalLayout_6.addWidget(self.pushButton_7)


        self.horizontalLayout_12.addWidget(self.frame_6)

        self.stackedPages.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.horizontalLayout_14 = QHBoxLayout(self.page6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_8 = QFrame(self.page6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(70, 170, 421, 91))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        font9 = QFont()
        font9.setPointSize(11)
        self.label.setFont(font9)

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

        self.horizontalLayout_17.addWidget(self.lineEdit)

        self.pushButton_8 = QPushButton(self.frame_18)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setMaximumSize(QSize(50, 16777215))

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
        font10 = QFont()
        font10.setPointSize(16)
        self.label_2.setFont(font10)

        self.verticalLayout_16.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_19 = QFrame(self.page7)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_209 = QFrame(self.frame_19)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_209)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(30, 0, 0, 0)
        self.label_166 = QLabel(self.frame_209)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setFont(font6)
        self.label_166.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_142.addWidget(self.label_166, 0, Qt.AlignBottom)


        self.horizontalLayout_18.addWidget(self.frame_209)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_270 = QFrame(self.frame_20)
        self.frame_270.setObjectName(u"frame_270")
        self.frame_270.setFrameShape(QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_270)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_Likes_23 = QLabel(self.frame_270)
        self.label_Likes_23.setObjectName(u"label_Likes_23")

        self.horizontalLayout_100.addWidget(self.label_Likes_23)

        self.label_Title_12 = QLabel(self.frame_270)
        self.label_Title_12.setObjectName(u"label_Title_12")
        self.label_Title_12.setFont(font3)
        self.label_Title_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.label_Title_12)

        self.label_Likes_24 = QLabel(self.frame_270)
        self.label_Likes_24.setObjectName(u"label_Likes_24")

        self.horizontalLayout_100.addWidget(self.label_Likes_24, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_270)

        self.label_Artist_5 = QLabel(self.frame_20)
        self.label_Artist_5.setObjectName(u"label_Artist_5")
        self.label_Artist_5.setFont(font4)
        self.label_Artist_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_Artist_5)

        self.frame_271 = QFrame(self.frame_20)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setFrameShape(QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_271)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_201 = QLabel(self.frame_271)
        self.label_201.setObjectName(u"label_201")

        self.horizontalLayout_101.addWidget(self.label_201, 0, Qt.AlignLeft)

        self.horizontalSlider_19 = QSlider(self.frame_271)
        self.horizontalSlider_19.setObjectName(u"horizontalSlider_19")
        self.horizontalSlider_19.setValue(25)
        self.horizontalSlider_19.setSliderPosition(25)
        self.horizontalSlider_19.setOrientation(Qt.Horizontal)

        self.horizontalLayout_101.addWidget(self.horizontalSlider_19)

        self.label_202 = QLabel(self.frame_271)
        self.label_202.setObjectName(u"label_202")

        self.horizontalLayout_101.addWidget(self.label_202, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_271)


        self.horizontalLayout_18.addWidget(self.frame_20)

        self.frame_272 = QFrame(self.frame_19)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setMaximumSize(QSize(50, 16777215))
        self.frame_272.setFrameShape(QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_272)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalSlider_23 = QSlider(self.frame_272)
        self.verticalSlider_23.setObjectName(u"verticalSlider_23")
        self.verticalSlider_23.setValue(40)
        self.verticalSlider_23.setOrientation(Qt.Vertical)

        self.verticalLayout_177.addWidget(self.verticalSlider_23)

        self.pushButton_43 = QPushButton(self.frame_272)
        self.pushButton_43.setObjectName(u"pushButton_43")

        self.verticalLayout_177.addWidget(self.pushButton_43)


        self.horizontalLayout_18.addWidget(self.frame_272)


        self.verticalLayout_16.addWidget(self.frame_19)

        self.stackedPages.addWidget(self.page7)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.verticalLayout_18 = QVBoxLayout(self.page8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_21 = QFrame(self.page8)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(100, 100, 100, 100)
        self.label_4 = QLabel(self.frame_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 100))
        font11 = QFont()
        font11.setPointSize(20)
        self.label_4.setFont(font11)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_21)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font9)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_3)


        self.verticalLayout_18.addWidget(self.frame_21)

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
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.pushButton_9 = QPushButton(self.frame_46)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(450, 20, 93, 28))
        self.label_15 = QLabel(self.frame_46)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 341, 41))
        font12 = QFont()
        font12.setPointSize(10)
        self.label_15.setFont(font12)
        self.label_15.setFrameShape(QFrame.Box)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.frame_46)

        self.tabWidget = QTabWidget(self.frame_22)
        self.tabWidget.setObjectName(u"tabWidget")
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
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.label_5 = QLabel(self.frame_28)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_19.addWidget(self.label_5)

        self.pushButton_10 = QPushButton(self.frame_28)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(30, 16777215))
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
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.radioButton_4 = QRadioButton(self.frame_31)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setChecked(True)

        self.horizontalLayout_20.addWidget(self.radioButton_4)

        self.label_6 = QLabel(self.frame_31)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_20.addWidget(self.label_6, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_26)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton_5 = QRadioButton(self.frame_32)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_21.addWidget(self.radioButton_5)

        self.label_7 = QLabel(self.frame_32)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_21.addWidget(self.label_7, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_26)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_6 = QRadioButton(self.frame_33)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_22.addWidget(self.radioButton_6)

        self.label_8 = QLabel(self.frame_33)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_22.addWidget(self.label_8, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_26)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton_7 = QRadioButton(self.frame_34)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_23.addWidget(self.radioButton_7)

        self.label_9 = QLabel(self.frame_34)
        self.label_9.setObjectName(u"label_9")

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
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.radioButton_8 = QRadioButton(self.frame_41)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setChecked(True)

        self.horizontalLayout_25.addWidget(self.radioButton_8)

        self.label_11 = QLabel(self.frame_41)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_25.addWidget(self.label_11, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_36)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.radioButton_9 = QRadioButton(self.frame_42)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_26.addWidget(self.radioButton_9)

        self.label_12 = QLabel(self.frame_42)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_26.addWidget(self.label_12, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_36)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.radioButton_10 = QRadioButton(self.frame_43)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_27.addWidget(self.radioButton_10)

        self.label_13 = QLabel(self.frame_43)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_27.addWidget(self.label_13, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_36)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.radioButton_11 = QRadioButton(self.frame_44)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_28.addWidget(self.radioButton_11)

        self.label_14 = QLabel(self.frame_44)
        self.label_14.setObjectName(u"label_14")

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
        self.label_18.setFont(font12)
        self.label_18.setFrameShape(QFrame.Box)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.frame_49)

        self.label_16 = QLabel(self.page10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 200))
        font13 = QFont()
        font13.setPointSize(21)
        self.label_16.setFont(font13)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_16)

        self.frame_47 = QFrame(self.page10)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_210 = QFrame(self.frame_47)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_210)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(30, 0, 0, 0)
        self.label_167 = QLabel(self.frame_210)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font6)
        self.label_167.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_149.addWidget(self.label_167, 0, Qt.AlignBottom)


        self.horizontalLayout_29.addWidget(self.frame_210)

        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_48)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_273 = QFrame(self.frame_48)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setFrameShape(QFrame.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_273)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_Title_13 = QLabel(self.frame_273)
        self.label_Title_13.setObjectName(u"label_Title_13")
        self.label_Title_13.setFont(font3)
        self.label_Title_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_Title_13)


        self.verticalLayout_27.addWidget(self.frame_273)

        self.label_Artist_10 = QLabel(self.frame_48)
        self.label_Artist_10.setObjectName(u"label_Artist_10")
        self.label_Artist_10.setFont(font4)
        self.label_Artist_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_Artist_10)

        self.frame_274 = QFrame(self.frame_48)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setFrameShape(QFrame.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_274)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.label_203 = QLabel(self.frame_274)
        self.label_203.setObjectName(u"label_203")

        self.horizontalLayout_103.addWidget(self.label_203, 0, Qt.AlignLeft)

        self.horizontalSlider_24 = QSlider(self.frame_274)
        self.horizontalSlider_24.setObjectName(u"horizontalSlider_24")
        self.horizontalSlider_24.setValue(25)
        self.horizontalSlider_24.setSliderPosition(25)
        self.horizontalSlider_24.setOrientation(Qt.Horizontal)

        self.horizontalLayout_103.addWidget(self.horizontalSlider_24)

        self.label_204 = QLabel(self.frame_274)
        self.label_204.setObjectName(u"label_204")

        self.horizontalLayout_103.addWidget(self.label_204, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_274)


        self.horizontalLayout_29.addWidget(self.frame_48)

        self.frame_275 = QFrame(self.frame_47)
        self.frame_275.setObjectName(u"frame_275")
        self.frame_275.setMaximumSize(QSize(50, 16777215))
        self.frame_275.setFrameShape(QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_275)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalSlider_24 = QSlider(self.frame_275)
        self.verticalSlider_24.setObjectName(u"verticalSlider_24")
        self.verticalSlider_24.setValue(40)
        self.verticalSlider_24.setOrientation(Qt.Vertical)

        self.verticalLayout_178.addWidget(self.verticalSlider_24)

        self.pushButton_44 = QPushButton(self.frame_275)
        self.pushButton_44.setObjectName(u"pushButton_44")

        self.verticalLayout_178.addWidget(self.pushButton_44)


        self.horizontalLayout_29.addWidget(self.frame_275)


        self.verticalLayout_28.addWidget(self.frame_47)

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
        self.label_19.setFont(font12)
        self.label_19.setFrameShape(QFrame.Box)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(50, 180, 481, 99))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_52)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, -1, -1, -1)
        self.label_17 = QLabel(self.frame_52)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font9)

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

        self.horizontalLayout_30.addWidget(self.lineEdit_2)

        self.pushButton_12 = QPushButton(self.frame_53)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_30.addWidget(self.pushButton_12)


        self.verticalLayout_30.addWidget(self.frame_53)


        self.verticalLayout_29.addWidget(self.frame_50)

        self.stackedPages.addWidget(self.page11)
        self.page12 = QWidget()
        self.page12.setObjectName(u"page12")
        self.label_20 = QLabel(self.page12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(90, 220, 411, 41))
        self.label_20.setFont(font12)
        self.label_20.setFrameShape(QFrame.Box)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.stackedPages.addWidget(self.page12)

        self.horizontalLayout_2.addWidget(self.stackedPages)


        self.horizontalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_31.addWidget(self.frame_5)

        self.frame_54 = QFrame(self.frame_51)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.stackedPages2 = QStackedWidget(self.frame_54)
        self.stackedPages2.setObjectName(u"stackedPages2")
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.horizontalLayout_170 = QHBoxLayout(self.page_draw)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.lineEdit_5 = QLineEdit(self.page_draw)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 400))
        font14 = QFont()
        font14.setPointSize(19)
        self.lineEdit_5.setFont(font14)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_170.addWidget(self.lineEdit_5)

        self.stackedPages2.addWidget(self.page_draw)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.horizontalLayout_172 = QHBoxLayout(self.page_search)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.lineEdit_7 = QLineEdit(self.page_search)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 400))
        self.lineEdit_7.setFont(font14)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_172.addWidget(self.lineEdit_7)

        self.stackedPages2.addWidget(self.page_search)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_173 = QHBoxLayout(self.page)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.lineEdit_8 = QLineEdit(self.page)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 400))

        self.horizontalLayout_173.addWidget(self.lineEdit_8)

        self.stackedPages2.addWidget(self.page)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_171 = QHBoxLayout(self.page_login)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.lineEdit_6 = QLineEdit(self.page_login)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 400))
        self.lineEdit_6.setFont(font14)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_171.addWidget(self.lineEdit_6)

        self.stackedPages2.addWidget(self.page_login)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_174 = QHBoxLayout(self.page_2)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.label_41 = QLabel(self.page_2)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_174.addWidget(self.label_41)

        self.stackedPages2.addWidget(self.page_2)

        self.horizontalLayout_54.addWidget(self.stackedPages2)


        self.verticalLayout_31.addWidget(self.frame_54)


        self.horizontalLayout_31.addWidget(self.frame_51)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1122, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_40.clicked.connect(MainWindow.playMusic1_chart)
        self.rightButton_19.clicked.connect(MainWindow.nextMusic)
        self.leftButton_19.clicked.connect(MainWindow.prevMusic)
        self.rightButton_23.clicked.connect(MainWindow.nextMusic)
        self.leftButton_23.clicked.connect(MainWindow.prevMusic)
        self.pushButton_48.clicked.connect(MainWindow.playMusic2_chart)
        self.rightButton_20.clicked.connect(MainWindow.nextMusic)
        self.leftButton_20.clicked.connect(MainWindow.prevMusic)
        self.pushButton_41.clicked.connect(MainWindow.playMusic3_chart)
        self.pushButton_23.clicked.connect(MainWindow.backToChart)
        self.pushButton_24.clicked.connect(MainWindow.backToChart)
        self.pushButton_25.clicked.connect(MainWindow.backToChart)
        self.post1.clicked.connect(MainWindow.playMusic1_post)
        self.post2.clicked.connect(MainWindow.playMusic2_post)
        self.post3.clicked.connect(MainWindow.playMusic3_post)
        self.pushButton_35.clicked.connect(MainWindow.backToPosts)
        self.pushButton_50.clicked.connect(MainWindow.backToPosts)
        self.pushButton_36.clicked.connect(MainWindow.backToPosts)
        self.menu_toolBox.currentChanged.connect(MainWindow.changeMenu)
        self.pushButton_4.clicked.connect(MainWindow.moveToReceivedMail)
        self.pushButton_7.clicked.connect(MainWindow.moveToSendMail)
        self.pushButton_9.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_12.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton_8.clicked.connect(MainWindow.moveToNextStep)
        self.pushButton.clicked.connect(MainWindow.moveToReceivedMail)
        self.pushButton_3.clicked.connect(MainWindow.moveToSendMail)
        self.pushButton_29.clicked.connect(MainWindow.reply)
        self.pushButton_30.clicked.connect(MainWindow.postMusic)

        self.menu_toolBox.setCurrentIndex(0)
        self.menu_toolBox.layout().setSpacing(7)
        self.stackedPages.setCurrentIndex(0)
        self.stackedCharts.setCurrentIndex(0)
        self.stackedMemoPages.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedMusicPosts.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(4)


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
        self.leftButton_19.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\uc568\ubc94\uc544\ud2b8", None))
        self.rightButton_19.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_9.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_5.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Likes_10.setText(QCoreApplication.translate("MainWindow", u"\u2764  251450", None))
        self.label_Artist_3.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.leftButton_23.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"\uc568\ubc94\uc544\ud2b8", None))
        self.rightButton_23.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_21.setText(QCoreApplication.translate("MainWindow", u"\u2764  58123", None))
        self.label_Title_11.setText(QCoreApplication.translate("MainWindow", u"Hype Boy", None))
        self.label_Likes_22.setText(QCoreApplication.translate("MainWindow", u"\u2764  231450", None))
        self.label_Artist_9.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.leftButton_20.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"\uc568\ubc94\uc544\ud2b8", None))
        self.rightButton_20.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_15.setText(QCoreApplication.translate("MainWindow", u"\u2764  48123", None))
        self.label_Title_8.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_16.setText(QCoreApplication.translate("MainWindow", u"\u2764  211450", None))
        self.label_Artist_4.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.leftButton_11.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.rightButton_11.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_13.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_7.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Likes_14.setText(QCoreApplication.translate("MainWindow", u"\u2764  251450", None))
        self.label_Artist_6.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.leftButton_22.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.rightButton_22.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_17.setText(QCoreApplication.translate("MainWindow", u"\u2764  58123", None))
        self.label_Title_9.setText(QCoreApplication.translate("MainWindow", u"Hype Boy", None))
        self.label_Likes_18.setText(QCoreApplication.translate("MainWindow", u"\u2764  231450", None))
        self.label_Artist_7.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.leftButton_12.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.rightButton_12.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_19.setText(QCoreApplication.translate("MainWindow", u"\u2764  48123", None))
        self.label_Title_10.setText(QCoreApplication.translate("MainWindow", u"Love Dive", None))
        self.label_Likes_20.setText(QCoreApplication.translate("MainWindow", u"\u2764  211450", None))
        self.label_Artist_8.setText(QCoreApplication.translate("MainWindow", u"IVE", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"@", None))
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
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"\u2764    \u2764    \u2764    \u2764", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Ditto\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Likes_8.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_3.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Likes_3.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"\u2764    \u2764    \u2764    \u2764", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Hype Boy\ub97c \ucd94\ucc9c\ud558\ub294 \uc0ac\ub78c\uc774 \uadf8\ub9b0 \uc5fd\uc11c", None))
        self.label_Likes_11.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_4.setText(QCoreApplication.translate("MainWindow", u"Hype Boy", None))
        self.label_Likes_4.setText(QCoreApplication.translate("MainWindow", u"\u2764  213450", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"\u2764    \u2764    \u2764    \u2764", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9cc\ub4e3\uae30", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u">", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubb38\uc790\ub85c \ubc1b\uc740 \uc778\uc99d \ucf54\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ub0b4\uc6a9(\ub2e4\ub978 \uc0ac\ub78c\uc774 \ub098\uc5d0\uac8c \uc791\uc131\ud55c \uc5fd\uc11c)", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Likes_23.setText(QCoreApplication.translate("MainWindow", u"\u2764  60123", None))
        self.label_Title_12.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Likes_24.setText(QCoreApplication.translate("MainWindow", u"\u2764  251450", None))
        self.label_Artist_5.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"QR Code", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9c0 \ubcf4\ub0b4\uae30\ub97c \uc6d0\ud558\uc2dc\uba74 \ub85c\uadf8\uc778\uc744 \ud574\uc8fc\uc138\uc694.", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc644\ub8cc", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1\ub2e8\uacc4. \ud3b8\uc9c0\uc5d0 \ucca8\ubd80\ud560 \ub178\ub798\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ub274\uc9c4\uc2a4", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u2714", None))
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
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u2714", None))
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
        self.label_167.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_Title_13.setText(QCoreApplication.translate("MainWindow", u"Ditto", None))
        self.label_Artist_10.setText(QCoreApplication.translate("MainWindow", u"New Jeans", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"3:34", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"3\ub2e8\uacc4. \ud3b8\uc9c0\ub97c \ubcf4\ub0bc \uc0ac\ub78c\uc758 \uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694.", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud654\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.(-\ub294 \ube7c\uace0 \uc791\uc131\ud574\uc8fc\uc138\uc694)", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc911\ud55c \ud3b8\uc9c0\uac00 \uc798 \uc804\ub2ec\ub418\uc5c8\uc2b5\ub2c8\ub2e4!", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9bc\ud310", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc545 \uac80\uc0c9\ud558\uae30", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"QR Code", None))
        self.label_41.setText("")
    # retranslateUi

