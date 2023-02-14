from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtCore import Qt, QObject
from kiosk_main_monitor import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QGuiApplication, QRegion
from PyQt5.QtCore import *

# 사용자 모듈 - painter 추가
import painter

import json
import sys
import os
import time

# 사용자 모듈 - player 추가
from player import VLC
import pafy

import urllib.request
from urllib.error import URLError, HTTPError

import requests

from client import Client
import logging

# http get 요청
# local_url -> 추후 서버 주소로 변경
#local_url = "http://localhost:8080"
local_url = "http://i8a402.p.ssafy.io:80"

request_header = {
    'Auth': 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiUk9MRV9VU0VSIiwidXNlcklkIjoxOSwibmlja05hbWUiOiLsgqzsmqnsnpAxOSIsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE2NzYzODI2MTksImV4cCI6MTY3NjQ0MjYxOX0.jUQivPZtELGUagd9xxLnNX1poMRyggns33QvFIoqLzI'
}

# 변수 처리해야함
hy_key = "AIzaSyC6_1JJhtq8uJgPDSLEAjA8OEBwQUa60vo"
sh_key = "AIzaSyDX1YbuvwTj-vb6FAZyxplVxBnjwryQRyA"

hype_boy = "https://www.youtube.com/watch?v=11cta61wi0g"
ditto = "https://www.youtube.com/watch?v=Km71Rr9K-Bw"
omg = "https://www.youtube.com/watch?v=-p1ftgMVWOc"
one_page = "https://www.youtube.com/watch?v=_78CYlWmigI"
love_dive = "https://www.youtube.com/watch?v=Y8JFxS1HlDo"

song_id = 1

spot_id = 1    # 기기 번호

# 가상 키보드 불러오기
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

# virtualkeyboard 윈도우가 메인 윈도우를 가리는 문제 해결
def handleVisibleChanged():
    if not QGuiApplication.inputMethod().isVisible():
        return
    for w in QGuiApplication.allWindows():
        if w.metaObject().className() == "QtVirtualKeyboard::InputView":
            keyboard = w.findChild(QObject, "keyboard")
            if keyboard is not None:
                r = w.geometry()
                r.moveTop(keyboard.property("y"))
                w.setMask(QRegion(r))
                return

#QThread 클래스 선언하기, QThread 클래스를 쓰려면 QtCore 모듈을 import 해야함.
class Thread(QThread):
    def __init__(self, parent): #parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스)
        super().__init__(parent)
        self.parent = parent    #self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다.
        self.num = 0
        self.running = True

    def pause(self):
        self.running = False

    def run(self):
        while self.running:
            self.move_slider.emit(self.num)
            self.num += 1
            self.sleep(1)

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

        #플레이어 선언
        pafy.set_api_key(sh_key)
        self.music_index = 0
        self.music_list = [ditto, hype_boy,love_dive,omg, one_page]
        self.music_chart = []
        self.player = VLC()
        #self.new_music(self.music_list[self.music_index][0])
        #self.new_music(self.music_list[self.music_index])
        #self.player.add_callback(vlc.EventType.MediaPlayerEndReached, self.nextMusic)  ## 종료 됬을대 다음곡

        #유저 정보
        sendId = ""
        nickname = ""
        passwd = ""

        songId = 0
        postcardImg = ""
        gift_id = 1

        # 차트 이미지
        self.chart_button_list = [self.chart_img_Button1, self.chart_img_Button2, self.chart_img_Button3,
                             self.chart_img_Button4, self.chart_img_Button5, self.chart_img_Button6,
                             self.chart_img_Button7, self.chart_img_Button8, self.chart_img_Button9,
                             self.chart_img_Button10]

        # 차트 scroll 세팅
        QScroller.grabGesture(
            self.scrollArea.viewport(), QScroller.LeftMouseButtonGesture
        )
        QScroller.grabGesture(
            self.post_scroll_area.viewport(), QScroller.LeftMouseButtonGesture
        )

        # 차트 정보 불러오기
        song_list_url = local_url + "/api/song/chart/giftcnt/"
        self.get_chart(song_list_url)

        """# 마니또 목록 불러오기
        manito_post_list = [
            self.post1,self.post2, self.post3, self.post4,
            self.post5, self.post6, self.post7, self.post8,
            self.post9, self.post10
        ]

        manito_list_url = local_url + '/api/manito/1'
        response = requests.get(manito_list_url, headers=request_header, params=None)
        res_json = response.json()
        print('마니또 목록:')
        print(res_json[0])

        for i in range(len(res_json)):
            pixmap = self.show_image(res_json[i].get('giftImg'))
            pixmap = pixmap.scaled(300, 300, Qt.IgnoreAspectRatio)
            icon = QIcon()
            icon.addPixmap(pixmap)
            manito_post_list[i].setIcon(icon)
            manito_post_list[i].setIconSize(pixmap.rect().size())"""

        #self.scrollArea.horizontalScrollBar().valueChanged.connect(lambda: swipe_music())

        # 스와이프로 차트 음악 넘겨 재생
        def swipe_music():
            value = self.scrollArea.horizontalScrollBar().value()

            if value < 10:
                self.play_music(self.music_chart[0])
            elif value < 20:
                self.play_music(self.music_chart[0])
            elif value < 30:
                self.play_music(self.music_chart[0])
            elif value < 40:
                self.play_music(self.music_chart[0])
            elif value < 50:
                self.play_music(self.music_chart[0])
            elif value < 60:
                self.play_music(self.music_chart[0])
            elif value < 70:
                self.play_music(self.music_chart[0])
            elif value < 80:
                self.play_music(self.music_chart[0])
            elif value < 90:
                self.play_music(self.music_chart[0])
            else:
                self.play_music(self.music_chart[0])

    def play_chart_scroll(self):
        value = self.scrollArea.horizontalScrollBar().value()
        #position_ratio = value / 1
        if value < 0.1:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.2:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.3:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.4:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.5:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.6:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.7:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.8:
            self.play_music(self.music_chart[0].get('song_url'))
        elif value < 0.9:
            self.play_music(self.music_chart[0].get('song_url'))
        else:
            self.play_music(self.music_chart[0].get('song_url'))

        self.scrollArea.horizontalScrollBar().valueChanged.connect(lambda: swipe_music())

        # 스와이프로 차트 음악 넘겨 재생
        def swipe_music():
            value = self.scrollArea.horizontalScrollBar().value()

            if value < 10:
                self.play_music(self.music_chart[0])
            elif value < 20:
                self.play_music(self.music_chart[0])
            elif value < 30:
                self.play_music(self.music_chart[0])
            elif value < 40:
                self.play_music(self.music_chart[0])
            elif value < 50:
                self.play_music(self.music_chart[0])
            elif value < 60:
                self.play_music(self.music_chart[0])
            elif value < 70:
                self.play_music(self.music_chart[0])
            elif value < 80:
                self.play_music(self.music_chart[0])
            elif value < 90:
                self.play_music(self.music_chart[0])
            else:
                self.play_music(self.music_chart[0])

    def move_slider(self, num):
        x = Thread(self)    #self는 WindowClass의 인스턴스, Thread 클래스에서 parent로 전달
        x.start()           #쓰레드 클래스의 run 메서드를 동작시키는 부분
        self.chart_music_slider.setValue(num)

    def get_chart(self, url):
        # 차트 정보 불러오기
        song_list_url = url
        song_list_param = {'spotId': spot_id}
        response = requests.get(song_list_url, headers=request_header, params=song_list_param)
        self.music_chart.clear()
        self.music_chart = response.json()

        for i in range(len(self.music_chart)):
            img_url = self.music_chart[i].get('song_img')
            pixmap = self.show_image(img_url)
            pixmap = pixmap.scaled(300, 300, Qt.IgnoreAspectRatio)

            icon = QIcon()
            icon.addPixmap(pixmap)
            ## 곡정보(제목,가수,재생시간) 변경
            self.label_Artist_3.setText(self.music_chart[i].get('singer'))  # singer
            self.label_Title_5.setText(self.music_chart[i].get('song_title'))  # song
            self.chart_button_list[i].setIcon(icon)
            self.chart_button_list[i].setIconSize(pixmap.rect().size())

        self.play_music(self.music_chart[i].get('song_url'))

    def align_chart(self, index):
        if index == 0:
            align_url = local_url + "/api/song/chart/giftcnt/"
        elif index == 1:
            align_url = local_url + "/api/song/chart/updatetime/"
        else:
            align_url = local_url + "/api/song/chart/random/"

        self.get_chart(align_url)

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

    def show_image(self, url):
        try:
            # 403 방지
            headers = {'User-Agent': 'Chrome/66.0.3359.181'}
            req = urllib.request.Request(url, headers=headers)
            img = urllib.request.urlopen(req)

        except HTTPError as e:
            err = e.read()
            code = e.getcode()

        source = img.read()
        img.close()

        img = requests.get(url)

        pixmap = QPixmap()
        pixmap.loadFromData(source)

        return pixmap

    def play_music(self, url):
        #self.video = pafy.new(self.music_chart[0].get('song_url'))  # pafy + youtube-dl 사용 direct link 변환
        #self.video = pafy.new(ditto)  # pafy + youtube-dl 사용 direct link 변환
        self.video = pafy.new(url)
        audio_url = self.video.getbestaudio(preftype="m4a").url  # direct link에서 음성만 추출
        self.player.set_uri(audio_url)

        ## 곡변경 시 슬라이더 초기설정 (0과 초기볼륨 설정)
        # self.horizontalSlider_20.setValue(0)
        # self.verticalSlider_19.setValue(70)
        self.player.set_volume(70)

        # 이미지 선처리
        img_url = self.music_chart[0].get('song_img')
        """
        try:
            #403 방지
            headers = {'User-Agent': 'Chrome/66.0.3359.181'}
            req = urllib.request.Request(img_url, headers=headers)
            img = urllib.request.urlopen(req)

        except HTTPError as e:
            err = e.read()
            code = e.getcode()

        source = img.read()
        img.close()

        img = requests.get(img_url)

        pixmap = QPixmap()
        pixmap.loadFromData(source)"""

        pixmap = self.show_image(img_url)
        pixmap = pixmap.scaled(300, 300, Qt.IgnoreAspectRatio)
        icon = QIcon()
        icon.addPixmap(pixmap)

        ## 곡정보(제목,가수,재생시간) 변경 - UI 파일 내놔!!
        self.label_Artist_3.setText(self.music_chart[0].get('singer'))  # singer
        self.label_Title_5.setText(self.music_chart[0].get('song_title'))   # song
        self.chart_img_Button1.setIcon(icon)
        self.chart_img_Button1.setIconSize(pixmap.rect().size())
        self.label_185.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))
        self.player.play()

        # 슬라이더 위치 설정
        self.chart_music_slider.setSliderPosition(int(self.player.get_position()))
        self.song_music_slider.setSliderPosition(int(self.player.get_position()))
        self.manito_music_slider.setSliderPosition(int(self.player.get_position()))
        self.manito_post_music_slider.setSliderPosition(int(self.player.get_position()))
        self.postcard_music_slider.setSliderPosition(int(self.player.get_position()))
        self.postcard_send_music_slider.setSliderPosition(int(self.player.get_position()))
        #self.move_slider(0)

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

        song_id = 1
        song_gift_url = local_url + "/api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()

        gift_list = res_json.get('giftList')

        self.music_post1.setPixmap(self.show_image(gift_list[0]))
        self.music_post2.setPixmap(self.show_image(gift_list[1]))
        self.music_post3.setPixmap(self.show_image(gift_list[2]))
        self.music_post4.setPixmap(self.show_image(gift_list[3]))
        self.music_post5.setPixmap(self.show_image(gift_list[4]))
        self.music_post6.setPixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('songTitle'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(str(res_json.get('giftCnt')))
        self.song_liked_cnt.setText(str(res_json.get('songLiked')))
        #self.play_music(res_json.get('songUrl'))

    def playMusic2_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 2
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()

        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic3_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 3
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()

        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic4_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 4
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()

        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic5_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 5
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()

        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic6_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 6
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()

        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic7_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 7
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic8_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 8
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic9_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 9
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)
    def playMusic10_chart(self):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        song_id = 10
        song_gift_url = local_url + "api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': song_id}

        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()
        gift_list = res_json.get('gifts')
        self.music_post1.pixmap(self.show_image(gift_list[0]))
        self.music_post2.pixmap(self.show_image(gift_list[1]))
        self.music_post3.pixmap(self.show_image(gift_list[2]))
        self.music_post4.pixmap(self.show_image(gift_list[3]))
        self.music_post5.pixmap(self.show_image(gift_list[4]))
        self.music_post6.pixmap(self.show_image(gift_list[5]))

        self.song_title.setText(res_json.get('song_title'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(res_json.get('gift_cnt'))
        self.song_liked_cnt.setText(res_json.get('song_liked'))

        self.play_music(0)

    def gift_detail(self, giftId):
        self.stackedPages.setCurrentIndex(3)
        self.stackedPages2.setCurrentIndex(3)
        gift_detail_url = local_url + "/api/gift/detail/"
        gift_detail_param = {'giftId': giftId}

        response = requests.get(gift_detail_url, headers=request_header, params=gift_detail_param)
        res_json = response.json()

        emoji_cnt = res_json.get('emoji')

        self.gift_detail_img.setPixmap(self.show_image(res_json.get('giftImg')))
        self.gift_detail_song.setText(res_json.get('song'))
        self.gift_detail_singer.setText(res_json.get('singer'))
        self.count_emoji1.setText(str(emoji_cnt.get('emo1')))
        self.count_emoji2.setText(str(emoji_cnt.get('emo2')))
        self.count_emoji3.setText(str(emoji_cnt.get('emo3')))
        self.count_emoji4.setText(str(emoji_cnt.get('emo4')))

        self.play_music(res_json.get('songUrl'))

    def playMusic1_post(self):
        self.gift_id = 1
        self.gift_detail(1)


    def playMusic2_post(self):
        self.gift_id = 2
        self.gift_detail(2)

    def playMusic3_post(self):
        self.gift_id = 3
        self.gift_detail(3)

    def playMusic4_post(self):
        self.gift_id = 4
        self.gift_detail(4)

    def playMusic5_post(self):
        self.gift_id = 5
        self.gift_detail(5)

    def playMusic6_post(self):
        self.gift_id = 6
        self.gift_detail(6)

    def playMusic7_post(self):
        self.gift_id = 7
        self.gift_detail(7)

    def playMusic8_post(self):
        self.gift_id = 8
        self.gift_detail(8)

    def playMusic9_post(self):
        self.gift_id = 9
        self.gift_detail(9)

    def playMusic10_post(self):
        self.gift_id = 10
        self.gift_detail(10)

    def scroll_post_left(self):
        self.post_scroll_area.scroll(-10,0)

    def scroll_post_right(self):
        self.post_scroll_area.scroll(10,0)

    def backToChart(self):
        self.stackedPages.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(2)
        self.menu_toolBox.setCurrentIndex(0)
        self.player.stop()

    def backToPosts(self):
        self.stackedPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(2)
        self.menu_toolBox.setCurrentIndex(1)
        self.player.stop()

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
            # 검색한 노래 정보 받아오기 - 구현 필요

            #self.play_music()

        elif self.stackedPages.currentIndex() == 3:
            self.stackedPages2.setCurrentIndex(5)
        elif self.stackedPages.currentIndex() == 4:
            self.stackedPages2.setCurrentIndex(9)
        elif self.stackedPages2.currentIndex() == 12:
            self.stackedPages2.setCurrentIndex(2)

        self.stackedPages.setCurrentIndex(currentPage + 1)

    def press_feedback(self, idx):
        emoji_list = [self.count_emoji1, self.count_emoji2, self.count_emoji3, self.count_emoji4]

        gift_detail_url = local_url + "/api/gift/detail"
        gift_detail_param = {'giftId': self.gift_id}
        response = requests.get(gift_detail_url, headers=request_header, params=gift_detail_param)
        res_json = response.json()

        emo = res_json.get('emoji')
        cnt_emo = emo.get('emo'+str(idx))
        emoji_list[idx-1].setText(str(cnt_emo + 1))

        gift_feedback_url = local_url + "/api/gift/feedback"
        gift_feedback_param = {'giftId': self.gift_id, 'idx': idx}
        requests.get(gift_feedback_url, headers=request_header, params=gift_feedback_param)

    def press_emoji1(self):
        self.press_feedback(1)
        """gift_detail_url = local_url + "/api/gift/detail"
        gift_detail_param = {'giftId': self.gift_id}
        response = requests.get(gift_detail_url, headers=request_header, params=gift_detail_param)
        res_json = response.json()
    
        emo = res_json.get('emoji')
        cnt_emo = emo.get('emo1')
        self.count_emoji1.setText(str(cnt_emo+1))

        gift_feedback_url = local_url + "/api/gift/feedback"
        gift_feedback_param = {'giftId': self.gift_id, 'idx': 1}
        requests.get(gift_feedback_url, headers=request_header, params=gift_feedback_param)
"""
    def press_emoji2(self):
        self.press_feedback(2)

    def press_emoji3(self):
        self.press_feedback(3)

    def press_emoji4(self):
        self.press_feedback(4)

    def reply(self):
        self.stackedPages.setCurrentIndex(3)
        self.stackedPages2.setCurrentIndex(0)

    def draw(self):
        self.stackedPages2.setCurrentIndex(0)

    # 로그인 웹 소켓 통신
    def print_frame(frame):
        # print(json.loads(frame.body))
        print(frame.body)
        print(frame.command)
        print(frame.headers)
        global token
        token = frame.body
        print("token : " + token)

    def login(self):
        self.stackedPages2.setCurrentIndex(4)
        spot_id = self.spot_id;
        ws_url = 'ws://localhost:8080/notifications/websocket'
        global token
        token = ''

        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        # logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

        # open transport
        client = Client(ws_url)

        client.connect()

        # subscribe channel
        client.subscribe("/sub/" + str(spot_id), callback=self.print_frame)

        # time.sleep(300)

        while token == '':
            pass

        client.disconnect()

    def logout(self):
        token = ''
        app.exit()

    def postMusic(self):
        self.stackedPages2.setCurrentIndex(1)

    def searchMusic(self):
        self.stackedPages.setCurrentIndex(4)
        self.stackedPages2.setCurrentIndex(6)

    def pause(self):
        playing = self.player.is_playing()
        if playing:
            self.player.pause()
        else:
            self.player.resume()

    def show_volume_chart(self):
        visible = self.volume_frame_chart.isVisible()
        self.volume_frame_chart.setVisible(not visible)
    def show_volume_song(self):
        visible = self.volume_frame_chart.isVisible()
        self.volume_frame_song.setVisible(not visible)
    def show_volume_manito(self):
        visible = self.volume_frame_manito.isVisible()
        self.volume_frame_manito.setVisible(not visible)
    def show_volume_post(self):
        visible = self.volume_frame_post.isVisible()
        self.volume_frame_post.setVisible(not visible)
    def show_volume_received(self):
        visible = self.volume_frame_received.isVisible()
        self.volume_frame_received.setVisible(not visible)
    def show_volume_send(self):
        visible = self.volume_frame_send.isVisible()
        self.volume_frame_send.setVisible(not visible)

    def change_volume(self, vol):
        self.player.set_volume(vol)

    def send_feedback(self):
        self.stackedPages2.setCurrentIndex(5)
        self.painter_widget.save("../resource/saved_images/feedbackImg.png")
        print("feedback saved!")

        # 채팅 서버로 피드백 전송
        url = local_url + "/channel"

        manito_data = manitoDTO = {'userId': 2, 'receiverId': 1, 'userNickname': 'sh', 'contentType': 'IMAGE'}
        now_dir = os.getcwd()
        image_path = f"{now_dir}/../resource/saved_images/feedbackImg.png"  # 이미지 경로
        image_name = r"feedbackImg.png"  # 이미지 이름

        files = {
            "postcardImg": (image_name, open(image_path, "rb"), "image/jpeg")
        }

        payload = {"postcard": json.dumps(manito_data)}

        response = requests.post(url, data=payload, files=files)

        print(response.status_code)

    def post_manito(self):
        self.stackedPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(2)
        self.painter_widget_3.save("../resource/saved_images/manitoImg.png")

        # 서버로 이미지와 마니또 정보 전송
        url = local_url + "/api/manito"

        manito_data = manitoDTO = {'userId': 2, 'songId': 1, 'spotId': 1, 'beforeManitoId': 1}
        image_path = r"../resource/saved_images/manitoImg.png"  # 이미지 경로
        image_name = "manitoImg.png"  # 이미지 이름

        access_token = request_header
        files = {
            "giftImg": (image_name, open(image_path, "rb"), "image/jpeg")
        }
        headers = {
            'Auth': access_token
        }

        payload = {"manito": json.dumps(manito_data)}

        response = requests.post(url, headers=headers, data=payload, files=files)

        print(response.status_code)


    def save_postcard(self):
        self.painter_widget_4.save("../resource/saved_images/postcardImg.png")
        print("postcard saved!")
        self.sent_postcard_image.setPixmap(QPixmap("../resource/saved_images/postcardImg.png"))
        self.stackedPages.setCurrentIndex(12)
        self.stackedPages2.setCurrentIndex(7)

    def input_code(self):
        self.stackedPages.setCurrentIndex(8)
        postcard_detail_url = local_url + '/postcard/'
        postcard_detail_param = {'postcardId': 'postcardId'}
        response = requests.get(postcard_detail_url, headers=request_header, params=postcard_detail_param)
        res_json = response.json()
        self.postcard_detail_img.pixmap(self.show_image(res_json.get('postcadImg')))
        self.postcard_detail_song.setText(res_json.get('song'))
        self.postcard_detail_singer.setText(res_json.get('singer'))
        self.play_music(res_json.get('songUrl'))

    def send_message(self):
        phone_number = self.lineEdit_3.text()
        add_postcard_url = local_url + "/api/postcard"
        add_postcard_data = {
            'sendId': self.sendId,
            'nickname': self.nickname,
            'phoneNumber': self.phone_number,
            'passwd': self.passwd,
            'songId': self.songId,
            'spotId': self.spotId,
            'postcardImg': "../resource/saved_images/postcardImg.png"
        }
        pd = json.dumps(add_postcard_data)
        response = requests.post(add_postcard_url, headers=request_header, data=pd)

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

QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

window = MyWindow()
window.setFixedWidth(1080)
window.setFixedHeight(1920)
window.showFullScreen()

app.exec()

