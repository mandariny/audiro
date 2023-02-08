import json
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtCore import Qt
from kiosk_main_monitor import Ui_MainWindow

# 사용자 모듈 - painter 추가
import painter
import Keyboard

import time

# 사용자 모듈 - player 추가
from player import VLC
import pafy
import urllib.request

import requests

spot_id = 1    # 기기 번호

# http get 요청

# local_url -> 추후 서버 주소로 변경
local_url = "http://localhost:8080"

request_header = {
    'Auth': 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiUk9MRV9VU0VSIiwidXNlcklkIjo1LCJuaWNrTmFtZSI6IuyCrOyaqeyekDUiLCJpYXQiOjE2NzU3NjU2NDYsImV4cCI6MTY3NTc3MTY0Nn0.b66aiYT0VmVFJzsRV1t2o3JCoINxuhFCixKwJ0jm5N8'
}


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
        self.keyboard_widget = Keyboard.AlphaNeumericVirtualKeyboard(self.lineEdit_4)
        self.keyboard_widget.setObjectName(u"keyboard_widget")
        self.keyboard_widget.setStyleSheet(u"color:black")

        self.verticalLayout_104.addWidget(self.keyboard_widget, 0, Qt.AlignHCenter)
        self.keyboard_widget.display()

        #플레이어 선언
        pafy.set_api_key(hy_key)
        self.music_index = 0
        self.music_list = [ditto, hype_boy,love_dive,omg, one_page]

        self.player = VLC()
        #self.new_music(self.music_list[self.music_index][0])
        self.new_music(self.music_list[self.music_index])
        #self.player.add_callback(vlc.EventType.MediaPlayerEndReached, self.nextMusic)  ## 종료 됬을대 다음곡

        #유저 정보
        sendId = ""
        nickname = ""
        passwd = ""

        songId = 0
        postcardImg = ""

        # 차트 scroll 세팅
        QScroller.grabGesture(
            self.scrollArea.viewport(), QScroller.LeftMouseButtonGesture
        )
        """
        # 차트 정보 불러오기
        postcard_url = local_url + "/api/postcard"
        for i in range(10):
            postcard_param = {'postcardId': i}
            response = requests.get(postcard_url, headers=request_header, params=postcard_param)
            res_json = response.json()
            self.music_list.append([res_json.get('id'), res_json.get('postcardImg'), res_json.get('song'), res_json.get('singer'), res_json.get('song_Url'), res_json.get('regTime')])

        # 차트 이미지 넣기
        chart_button_list = [self.chart_img_Button1, self.chart_img_Button2, self.chart_img_Button3, self.chart_img_Button4, self.chart_img_Button5, self.chart_img_Button6, self.chart_img_Button7, self.chart_img_Button8, self.chart_img_Button9, self.chart_img_Button10]
        for i in range(10):
            qix = QPixmap()
            qix.loadFromData(self.music_list[i][1])
            chart_button_list[i].setIcon(QIcon(qix))
            chart_button_list[i].setIconSize(qix.rect().size())
        """

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
        self.label_185.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))
        self.player.play()

    """def playMusic(self, index):
        self.video = pafy.new(self.music_list[index][4])  # pafy + youtube-dl 사용 direct link 변환
        audio_url = self.video.getbestaudio(preftype="m4a").url  # direct link에서 음성만 추출
        self.player.set_uri(audio_url)

        ## 곡변경 시 슬라이더 초기설정 (0과 초기볼륨 설정)
        # self.horizontalSlider_20.setValue(0)
        # self.verticalSlider_19.setValue(70)
        self.player.set_volume(70)

        # 이미지 선처리
        img = self.music_list[index][1]
        qix = QPixmap()
        qix.loadFromData(img)

        ## 곡정보(제목,가수,재생시간) 변경 - UI 파일 내놔!!
        self.label_Artist_3.setText(self.music_list[index][3])  # singer
        self.label_Title_5.setText(self.music_list[index][2])   # song
        self.pushButton_97.setIcon(QIcon(qix))
        self.pushButton_97.setIconSize(qix.rect().size())
        self.label_185.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))
        self.player.play()
    """
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
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic2_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic3_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic4_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic5_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic6_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic7_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic8_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic9_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])
    def playMusic10_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 0
        postcard_url = local_url + "/song/gifts/:" + song_id + "/:" + spot_id
        response = requests.get(postcard_url, headers=request_header, params=None)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(gift_list[0])
        self.music_post2.pixmap(gift_list[1])
        self.music_post3.pixmap(gift_list[2])
        self.music_post4.pixmap(gift_list[3])
        self.music_post5.pixmap(gift_list[4])
        self.music_post6.pixmap(gift_list[5])

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

        if self.stackedPages.currentIndex() == 8:
            self.stackedPages2.setCurrentIndex(0)
        elif self.stackedPages.currentIndex() == 9:
            self.stackedPages2.setCurrentIndex(6)
        elif self.stackedPages.currentIndex() == 10:
            self.stackedPages2.setCurrentIndex(10)

        elif self.stackedPages.currentIndex() == 3:
            self.stackedPages2.setCurrentIndex(5)
        elif self.stackedPages.currentIndex() == 4:
            self.stackedPages2.setCurrentIndex(9)
        elif self.stackedPages2.currentIndex() == 12:
            self.stackedPages2.setCurrentIndex(2)

        if self.stackedPages.currentIndex() == 3 and self.stackedPages2.currentIndex() == 0:
            pass
        elif self.stackedPages.currentIndex() == 1:
            self.stackedPages.setCurrentIndex(0)
            self.stackedPages2.setCurrentIndex(2)
        else:
            self.stackedPages.setCurrentIndex(currentPage + 1)

    def reply(self):
        self.stackedPages.setCurrentIndex(3)
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

    def save_postcard(self):
        self.painter_widget_4.save("../resource/saved_images/postcardImg.png")
        print("postcard saved!")
        self.sent_postcard_image.setPixmap(QPixmap("../resource/saved_images/postcardImg.png"))
        self.stackedPages.setCurrentIndex(12)
        self.stackedPages2.setCurrentIndex(7)

    def input_code(self):
        pass

    def send_message(self):
        phone_number = self.lineEdit_3.text()
        postcard_url = local_url + "/api/postcard"
        postcard_data = {'sendId': self.sendId, 'nickname': self.nickname, 'phoneNumber': self.phone_number, 'passwd': self.passwd, 'songId': self.songId, 'spotId': self.spotId, 'postcardImg': self.postcardImg}
        pd = json.dumps(postcard_data)
        response = requests.post(postcard_url, headers=request_header, data=postcard_data)

        self.sent_postcard_image.pixmap(postcard_data['postcardImg'])
        pass

    def volumeChange(self):
        pass

    def colorChange1(self):
        self.painter_widget.pen.setColor(QColor(0, 0, 0))
        self.painter_widget_2.pen.setColor(QColor(0, 0, 0))
        self.painter_widget_3.pen.setColor(QColor(0, 0, 0))
        self.painter_widget_4.pen.setColor(QColor(0, 0, 0))

    def colorChange2(self):
        self.painter_widget.pen.setColor(QColor(245, 51, 51))
        self.painter_widget_2.pen.setColor(QColor(245, 51, 51))
        self.painter_widget_3.pen.setColor(QColor(245, 51, 51))
        self.painter_widget_4.pen.setColor(QColor(245, 51, 51))

    def colorChange3(self):
        self.painter_widget.pen.setColor(QColor(238, 106, 31))
        self.painter_widget_2.pen.setColor(QColor(238, 106, 31))
        self.painter_widget_3.pen.setColor(QColor(238, 106, 31))
        self.painter_widget_4.pen.setColor(QColor(238, 106, 31))


    def colorChange4(self):
        self.painter_widget.pen.setColor(QColor(231, 234, 91))
        self.painter_widget_2.pen.setColor(QColor(231, 234, 91))
        self.painter_widget_3.pen.setColor(QColor(231, 234, 91))
        self.painter_widget_4.pen.setColor(QColor(231, 234, 91))

    def colorChange5(self):
        self.painter_widget.pen.setColor(QColor(26, 203, 22))
        self.painter_widget_2.pen.setColor(QColor(26, 203, 22))
        self.painter_widget_3.pen.setColor(QColor(26, 203, 22))
        self.painter_widget_4.pen.setColor(QColor(26, 203, 22))

    def colorChange6(self):
        self.painter_widget.pen.setColor(QColor(76, 37, 232))
        self.painter_widget_2.pen.setColor(QColor(76, 37, 232))
        self.painter_widget_3.pen.setColor(QColor(76, 37, 232))
        self.painter_widget_4.pen.setColor(QColor(76, 37, 232))

    def colorChange7(self):
        self.painter_widget.pen.setColor(QColor(181, 37, 232))
        self.painter_widget_2.pen.setColor(QColor(181, 37, 232))
        self.painter_widget_3.pen.setColor(QColor(181, 37, 232))
        self.painter_widget_4.pen.setColor(QColor(181, 37, 232))

    def colorChange8(self):
        self.painter_widget.pen.setColor(QColor(232, 37, 142))
        self.painter_widget_2.pen.setColor(QColor(232, 37, 142))
        self.painter_widget_3.pen.setColor(QColor(232, 37, 142))
        self.painter_widget_4.pen.setColor(QColor(232, 37, 142))

    def colorChange9(self):
        self.painter_widget.pen.setColor(QColor(255,255,255))
        self.painter_widget_2.pen.setColor(QColor(255, 255, 255))
        self.painter_widget_3.pen.setColor(QColor(255, 255, 255))
        self.painter_widget_4.pen.setColor(QColor(255, 255, 255))

    def painterClear(self):
        self.painter_widget.clear()
        self.painter_widget_2.clear()
        self.painter_widget_3.clear()
        self.painter_widget_4.clear()

app = QApplication(sys.argv)
screen_rect = app.desktop().screenGeometry()
print(screen_rect.width(), screen_rect.height())
window = MyWindow()
window.setFixedWidth(1080)
window.setFixedHeight(1920)
window.showFullScreen()

app.exec()

