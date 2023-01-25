import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor

from main_page import Ui_MainWindow


# 사용자 모듈 - painter 추가
from painter import PainterWidget
import Keyboard

# 사용자 모듈 - player 추가
import vlc
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
        self.stackedPages2.setCurrentIndex(1)
        ##스택페이지2 index(
        # 0: 그림판 text,
        # 1: 음악검색 text,
        # 2: none,
        # 3: QR code text,
        # 4: 그림판(버튼으로 연동해야되는 그림판)
        # 5: 키보드

        #self.painter_widget.set_color(QColor(rgb(255,255,255)))

        #그림판 선언
        self.painter_widget = PainterWidget()
        self.stackedPages2.addWidget(self.painter_widget)
        #self.stackedPages2.setCurrentIndex(4) # 내가 원하는 위젯 뿌리기 - 다음에는 ui 파일도 올려줘...

        #키보드 선언
        self.temp_line = QLineEdit()

        self.virtual_keyboard = Keyboard.AlphaNeumericVirtualKeyboard(self.temp_line)
        self.stackedPages2.addWidget(self.virtual_keyboard)
        #self.virtual_keyboard.display()
        #self.virtual_keyboard.setFixedSize(800, 960)

        #플레이어 선언
        pafy.set_api_key(hy_key)
        self.music_index = 0
        self.music_list = [ditto, hype_boy,love_dive,omg, one_page]

        self.player = VLC()
        self.new_music(self.music_list[self.music_index])
        #self.player.add_callback(vlc.EventType.MediaPlayerEndReached, self.nextMusic)  ## 종료 됬을대 다음곡

        #self.stackedPages2.setCurrentIndex(5)

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
        if self.stackedCharts.currentIndex()==0:
            self.label_Artist_3.setText(self.video.author)  # 0-diito
            self.label_Title_7.setText(self.video.title)
            self.pushButton_40.setIcon(QIcon(qix))
            self.pushButton_40.setIconSize(qix.rect().size())
            self.label_185.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))

        elif self.stackedCharts.currentIndex() == 1:
            self.label_Artist_9.setText(self.video.author)  # 1-hype boy
            self.label_Title_11.setText(self.video.title)
            self.pushButton_48.setIcon(QIcon(qix))
            self.pushButton_48.setIconSize(qix.rect().size())
            self.label_197.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))

        elif self.stackedCharts.currentIndex() == 2:
            self.label_Artist_4.setText(self.video.author)  # 2-러브다이브
            self.label_Title_8.setText(self.video.title)
            self.pushButton_41.setIcon(QIcon(qix))
            self.pushButton_41.setIconSize(qix.rect().size())
            self.label_187.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))

        self.player.play()


    def nextMusic(self):
        currentPage = self.stackedCharts.currentIndex()
        countPage = self.stackedCharts.count()
        if currentPage+1 >= countPage:
            self.stackedCharts.setCurrentIndex(0)
        else:
            self.stackedCharts.setCurrentIndex(currentPage + 1)

        #플레이어 추가코드
        self.new_music(self.music_list[self.stackedCharts.currentIndex()])

    def prevMusic(self):
        currentPage = self.stackedCharts.currentIndex()
        countPage = self.stackedCharts.count()
        if currentPage-1 < 0:
            self.stackedCharts.setCurrentIndex(countPage-1)
        else:
            self.stackedCharts.setCurrentIndex(currentPage-1)

        # 플레이어 추가코드
        self.new_music(self.music_list[self.stackedCharts.currentIndex()])

    def playMusic1_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedMemoPages.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(4)

    def playMusic2_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedMemoPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(4)

    def playMusic3_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedMemoPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(4)

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

app = QApplication(sys.argv)
window = MyWindow()
#window.setFixedWidth(1000)
#window.setFixedHeight(1000)
window.show()

app.exec()

