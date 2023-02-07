import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor
from kiosk_main_monitor import Ui_MainWindow

# 사용자 모듈 - painter 추가
import painter
import Keyboard

# 사용자 모듈 - player 추가
from player import VLC
import pafy
import urllib.request


# 변수 처리해야함
hy_key = "AIzaSyC6_1JJhtq8uJgPDSLEAjA8OEBwQUa60vo"

hype_boy = "https://www.youtube.com/watch?v=11cta61wi0g"
ditto = "https://www.youtube.com/watch?v=Km71Rr9K-Bw"
omg = "https://www.youtube.com/watch?v=-p1ftgMVWOc"
one_page = "https://www.youtube.com/watch?v=_78CYlWmigI"
love_dive = "https://www.youtube.com/watch?v=Y8JFxS1HlDo"


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.stackedPages.setCurrentIndex(0)
        self.menu_toolBox.setCurrentIndex(0)

        #self.stackedWidget_4.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(2)
        ##스택페이지2 index(
        # 0: 그림판 text,
        # 1: 음악검색 text,
        # 2: none,
        # 3: QR code text,
        # 4: 그림판(버튼으로 연동해야되는 그림판)
        # 5: 키보드

        #self.painter_widget.set_color(QColor(rgb(255,255,255)))

        #그림판 선언
        #self.painter_widget = PainterWidget()
        #self.stackedPages2.addWidget(self.painter_widget)
        #self.stackedPages2.setCurrentIndex(4) # 내가 원하는 위젯 뿌리기 - 다음에는 ui 파일도 올려줘...

        #키보드 선언
        self.keyboard_widget.display()

        self.temp_line = QLineEdit()

        self.virtual_keyboard = Keyboard.AlphaNeumericVirtualKeyboard(self.temp_line)

        self.stackedPages2.addWidget(self.virtual_keyboard)
        self.virtual_keyboard.display()
        self.virtual_keyboard.setFixedSize(800, 960)

        #플레이어 선언
        pafy.set_api_key(hy_key)
        self.music_index = 0
        self.music_list = [ditto, hype_boy,love_dive,omg, one_page]

        self.player = VLC()
        self.new_music(self.music_list[self.music_index])
        #self.player.add_callback(vlc.EventType.MediaPlayerEndReached, self.nextMusic)  ## 종료 됬을대 다음곡

        #self.stackedPages2.setCurrentIndex(5)


        # 차트 이미지 설정
        icon1 = QPixmap("ditto.jpg")
        icon2 = QPixmap("hype_boy.jpg")
        icon3 = QPixmap("love_dive.jpg")

        self.pushButton_40.setIcon(QIcon(icon1))
        self.pushButton_40.setIconSize(icon1.size())
        self.pushButton_93.setIcon(QIcon(icon2))
        self.pushButton_93.setIconSize(icon2.size())
        self.pushButton_94.setIcon(QIcon(icon3))
        self.pushButton_94.setIconSize(icon3.rect().size())
        self.pushButton_95.setIcon(QIcon(icon1))
        self.pushButton_95.setIconSize(icon1.rect().size())
        self.pushButton_96.setIcon(QIcon(icon2))
        self.pushButton_96.setIconSize(icon2.rect().size())

        # 차트 scroll 세팅
        QScroller.grabGesture(
            self.scrollArea.viewport(), QScroller.LeftMouseButtonGesture
        )

    # 플레이어 함수들
    def new_music(self, url):
        self.video = pafy.new(url)  # pafy + youtube-dl 사용 direct link 변환
        audio_url = self.video.getbestaudio(preftype="m4a").url  # direct link에서 음성만 추출
        self.player.set_uri(audio_url)

        ## 곡변경 시 슬라이더 초기설정 (0과 초기볼륨 설정)
        #self.horizontalSlider_20.setValue(0)
        #self.verticalSlider_19.setValue(70)
        self.player.set_volume(70)

        # 이미지 선처리
        img = urllib.request.urlopen("https://img.youtube.com/vi/" + url.split('=', 1)[1] + "/0.jpg").read()
        qix = QPixmap()
        qix.loadFromData(img)

        ## 곡정보(제목,가수,재생시간) 변경 - UI 파일 내놔!!
        self.label_Artist_3.setText(self.video.author)  # 0-diito
        self.label_Title_5.setText(self.video.title)
        self.pushButton_97.setIcon(QIcon(qix))
        self.pushButton_97.setIconSize(qix.rect().size())
        self.label_185.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))
        self.player.play()

    def nextMusic(self):
        pass

        #플레이어 추가코드
        #self.new_music(self.music_list[self.stackedCharts.currentIndex()])

    def prevMusic(self):
        pass

        # 플레이어 추가코드
        #self.new_music(self.music_list[self.stackedCharts.currentIndex()])


    # nextMemos, prevMemos -> hard coding
    def nextMemos(self):
        currentPage = self.stackedWidget_3.currentIndex()
        countPage = self.stackedWidget_3.count()
        if currentPage + 1 >= countPage:
            self.stackedWidget_3.setCurrentIndex(0)
        else:
            self.stackedWidget_3.setCurrentIndex(currentPage + 1)

    def prevMemos(self):
        currentPage = self.stackedWidget_3.currentIndex()
        countPage = self.stackedWidget_3.count()
        if currentPage - 1 < 0:
            self.stackedWidget_3.setCurrentIndex(countPage - 1)
        else:
            self.stackedWidget_3.setCurrentIndex(currentPage - 1)

    def playMusic1_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)

    def playMusic2_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)

    def playMusic3_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)

    def playMusic1_post(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedPages2.setCurrentIndex(3)

    def playMusic2_post(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedPages2.setCurrentIndex(3)

    def playMusic3_post(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedPages2.setCurrentIndex(3)

    def backToChart(self):
        self.stackedPages.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(2)

    def backToPosts(self):
        self.stackedPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(2)

    def changeMenu(self, ind):
        if ind == 0:
            self.stackedPages.setCurrentIndex(0)
            self.stackedPages2.setCurrentIndex(2)
        elif ind == 1:
            self.stackedPages.setCurrentIndex(2)
            self.stackedPages2.setCurrentIndex(2)
        else:
            self.stackedPages.setCurrentIndex(6)

    def moveToReceivedMail(self):
        self.stackedPages.setCurrentIndex(7)
        self.stackedPages2.setCurrentIndex(2)

    def moveToSendMail(self):
        self.stackedPages.setCurrentIndex(9)
        self.stackedPages2.setCurrentIndex(2)

    def moveToNextStep(self):
        currentPage = self.stackedPages.currentIndex()

        if self.stackedPages.currentIndex()==8:
            self.stackedPages2.setCurrentIndex(0)
        elif self.stackedPages.currentIndex()==9:
            self.stackedPages2.setCurrentIndex(6)
        elif self.stackedPages.currentIndex()==10:
            self.stackedPages2.setCurrentIndex(10)

        elif self.stackedPages.currentIndex()==3:
            self.stackedPages2.setCurrentIndex(5)
        elif self.stackedPages.currentIndex()==4:
            self.stackedPages2.setCurrentIndex(9)

        if self.stackedPages.currentIndex()==3 and self.stackedPages2.currentIndex()==0:
            pass
        elif self.stackedPages.currentIndex() == 1:
            self.stackedPages.setCurrentIndex(0)
            self.stackedPages2.setCurrentIndex(2)
        else:
            self.stackedPages.setCurrentIndex(currentPage + 1)

    def reply(self):
        self.stackedPages2.setCurrentIndex(0)

    def draw(self):
        self.stackedPages2.setCurrentIndex(0)

    def login(self):
        self.stackedPages2.setCurrentIndex(4)

    def postMusic(self):
        self.stackedPages2.setCurrentIndex(1)

    def searchMusic(self):
        self.stackedPages.setCurrentIndex(4)
        self.stackedPages2.setCurrentIndex(6)

    def volumeChange(self):
        pass

    def colorChange1(self):
        self.painter_widget.pen.setColor(QColor(0, 0, 0))
        self.painter_widget_2.pen.setColor(QColor(0, 0, 0))
        self.painter_widget_3.pen.setColor(QColor(0, 0, 0))

    def colorChange2(self):
        self.painter_widget.pen.setColor(QColor(245, 51, 51))
        self.painter_widget_2.pen.setColor(QColor(245, 51, 51))
        self.painter_widget_3.pen.setColor(QColor(245, 51, 51))

    def colorChange3(self):
        self.painter_widget.pen.setColor(QColor(238, 106, 31))
        self.painter_widget_2.pen.setColor(QColor(238, 106, 31))
        self.painter_widget_3.pen.setColor(QColor(238, 106, 31))

    def colorChange4(self):
        self.painter_widget.pen.setColor(QColor(231, 234, 91))
        self.painter_widget_2.pen.setColor(QColor(231, 234, 91))
        self.painter_widget_3.pen.setColor(QColor(231, 234, 91))

    def colorChange5(self):
        self.painter_widget.pen.setColor(QColor(26, 203, 22))
        self.painter_widget_2.pen.setColor(QColor(26, 203, 22))
        self.painter_widget_3.pen.setColor(QColor(26, 203, 22))

    def colorChange6(self):
        self.painter_widget.pen.setColor(QColor(76, 37, 232))
        self.painter_widget_2.pen.setColor(QColor(76, 37, 232))
        self.painter_widget_3.pen.setColor(QColor(76, 37, 232))

    def colorChange7(self):
        self.painter_widget.pen.setColor(QColor(181, 37, 232))
        self.painter_widget_2.pen.setColor(QColor(181, 37, 232))
        self.painter_widget_3.pen.setColor(QColor(181, 37, 232))

    def colorChange8(self):
        self.painter_widget.pen.setColor(QColor(232, 37, 142))
        self.painter_widget_2.pen.setColor(QColor(232, 37, 142))
        self.painter_widget_3.pen.setColor(QColor(232, 37, 142))

    def colorChange9(self):
        self.painter_widget.pen.setColor(QColor(255,255,255))
        self.painter_widget_2.pen.setColor(QColor(255, 255, 255))
        self.painter_widget_3.pen.setColor(QColor(255, 255, 255))

    def painterClear(self):
        self.painter_widget.clear()
        self.painter_widget_2.clear()
        self.painter_widget_3.clear()

app = QApplication(sys.argv)
screen_rect = app.desktop().screenGeometry()
print(screen_rect.width(), screen_rect.height())
window = MyWindow()
window.setFixedWidth(1080)
window.setFixedHeight(1920)
window.showFullScreen()

app.exec()

