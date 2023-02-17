from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QColor, QFont
from PyQt5.QtCore import Qt, QObject
from kiosk_main_monitor import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QGuiApplication, QRegion
from PyQt5.QtCore import *

# 사용자 모듈 - painter 추가
import painter

from PyQt5.QtCore import QTime, QDateTime
import datetime

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

import asyncio

from client import Client
import logging

# http get 요청
# local_url -> 추후 서버 주소로 변경
#local_url = "http://localhost:8080"
local_url = "http://i8a402.p.ssafy.io:80"

request_header = {
    'Auth': 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiUk9MRV9VU0VSIiwidXNlcklkIjoxOSwibmlja05hbWUiOiLsgqzsmqnsnpAxOSIsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE2NzY1NDcyOTgsImV4cCI6MTY3NjYwNzI5OH0.9aynjtOKMfAYJ852xJNt4j3JsMe_hLzQHudiKwCg9XQ'
}

# 변수 처리해야함
hy_key = "AIzaSyC6_1JJhtq8uJgPDSLEAjA8OEBwQUa60vo"
sh_key = "AIzaSyDX1YbuvwTj-vb6FAZyxplVxBnjwryQRyA"

hype_boy = "https://www.youtube.com/watch?v=11cta61wi0g"
ditto = "https://www.youtube.com/watch?v=Km71Rr9K-Bw"
omg = "https://www.youtube.com/watch?v=-p1ftgMVWOc"
one_page = "https://www.youtube.com/watch?v=_78CYlWmigI"
love_dive = "https://www.youtube.com/watch?v=Y8JFxS1HlDo"

"""song_id = 1 # 현재 노래 id"""

#selected_index = 0  # 검색 페이지에서 선택한 노래 인덱스
spot_id = 1    # 기기 번호
gift_id = 1     # gift id


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


        #플레이어 선언
        pafy.set_api_key(sh_key)

        self.music_list = [ditto, hype_boy,love_dive,omg, one_page]
        self.music_chart = []
        self.player = VLC()
        #self.new_music(self.music_list[self.music_index][0])
        #self.new_music(self.music_list[self.music_index])
        #self.player.add_callback(vlc.EventType.MediaPlayerEndReached, self.nextMusic)  ## 종료 됬을대 다음곡

        self.music_index = 0  # 차트에서 현재 노래 인덱스

        # 검색 페이지 세팅
        self.search_result = []
        self.search_buttons_made = []
        self.search_labels_made = []

        self.postcard_img = "" # postcard 이미지 파일명

        self.song_id = 1    # 현재 재생중인 노래 id
        self.new_song_id = 1    # 현재 선택한 노래 id

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
        self.music_index = 0
        self.play_music()

        # 마니또 목록 불러오기
        self.show_manito_list()

    def get_chart(self, url):
        # 차트 정보 불러오기
        song_list_url = url
        song_list_param = {'spotId': spot_id}
        response = requests.get(song_list_url, headers=request_header, params=song_list_param)
        print(response)
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
            self.song_liked.setText(str(self.music_chart[i].get('song_liked')))
            self.chart_button_list[i].setIcon(icon)
            self.chart_button_list[i].setIconSize(pixmap.rect().size())

    def align_chart(self, index):
        if index == 0:
            align_url = local_url + "/api/song/chart/giftcnt/"
        elif index == 1:
            align_url = local_url + "/api/song/chart/updatetime/"
        else:
            align_url = local_url + "/api/song/chart/random/"

        self.get_chart(align_url)
        self.music_index = 0
        self.play_music()

    # 플레이어 함수들
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

    def play_music(self):
        url = self.music_chart[self.music_index].get("song_url")
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
        img_url = self.music_chart[self.music_index].get('song_img')
        pixmap = self.show_image(img_url)
        pixmap = pixmap.scaled(300, 300, Qt.IgnoreAspectRatio)
        icon = QIcon()
        icon.addPixmap(pixmap)

        ## 곡정보(제목,가수,재생시간) 변경 - UI 파일 내놔!!
        self.label_Artist_3.setText(self.music_chart[self.music_index].get('singer'))  # singer
        self.label_Title_5.setText(self.music_chart[self.music_index].get('song_title'))   # song
        self.song_liked.setText(str(self.music_chart[self.music_index].get('song_liked')))     # 좋아요
        self.chart_img_Button1.setIcon(icon)
        self.chart_img_Button1.setIconSize(pixmap.rect().size())
        self.label_185.setText(str(int(self.video.length / 60)) + ":" + str(self.video.length % 60))
        self.player.play()

        """# 슬라이더 위치 설정
        self.chart_music_slider.setSliderPosition(int(self.player.get_position()))
        self.song_music_slider.setSliderPosition(int(self.player.get_position()))
        self.manito_music_slider.setSliderPosition(int(self.player.get_position()))
        self.manito_post_music_slider.setSliderPosition(int(self.player.get_position()))
        self.postcard_music_slider.setSliderPosition(int(self.player.get_position()))
        self.postcard_send_music_slider.setSliderPosition(int(self.player.get_position()))
        #self.move_slider(0)"""

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

    def playMusic_chart(self, id):
        self.stackedPages.setCurrentIndex(1)
        self.stackedPages2.setCurrentIndex(8)
        self.song_id = id
        song_gift_url = local_url + "/api/song/gifts/"
        song_gift_param = {'spotId': spot_id, 'songId': 1}
        response = requests.get(song_gift_url, headers=request_header, params=song_gift_param)
        res_json = response.json()
        gift_list = res_json.get('giftList')

        self.music_post1.setPixmap(self.show_image(gift_list[0]))
        self.music_post2.setPixmap(self.show_image(gift_list[1]))
        self.music_post3.setPixmap(self.show_image(gift_list[2]))
        self.music_post4.setPixmap(self.show_image(gift_list[0]))
        self.music_post5.setPixmap(self.show_image(gift_list[1]))
        self.music_post6.setPixmap(self.show_image(gift_list[2]))
        self.song_title.setText(res_json.get('songTitle'))
        self.song_singer.setText(res_json.get('singer'))
        self.song_gift_cnt.setText(str(res_json.get('giftCnt')))
        self.song_liked_cnt.setText(str(res_json.get('songLiked')))
        self.play_music()

    def playMusic1_chart(self):
        self.music_index = 0
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic2_chart(self):
        self.music_index = 1
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic3_chart(self):
        self.music_index = 2
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic4_chart(self):
        self.music_index = 3
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic5_chart(self):
        self.music_index = 4
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic6_chart(self):
        music_index = 5
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic7_chart(self):
        self.music_index = 6
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic8_chart(self):
        self.music_index = 7
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic9_chart(self):
        self.music_index = 8
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def playMusic10_chart(self):
        self.music_index = 9
        self.playMusic_chart(self.music_chart[self.music_index].get("song_id"))

    def show_manito_list(self):
        # 마니또 목록 불러오기
        manito_post_list = [
            self.post1, self.post2, self.post3, self.post4,
            self.post5, self.post6, self.post7, self.post8,
            self.post9, self.post10
        ]

        manito_list_url = local_url + '/api/manito/' + str(spot_id)
        response = requests.get(manito_list_url, headers=request_header, params=None)
        res_json = response.json()

        for i in range(len(res_json)):
            if i>=10: break
            pixmap = self.show_image(res_json[i].get('giftImg'))
            pixmap = pixmap.scaled(300, 300, Qt.IgnoreAspectRatio)
            icon = QIcon()
            icon.addPixmap(pixmap)
            manito_post_list[i].setIcon(icon)
            manito_post_list[i].setIconSize(pixmap.rect().size())
            manito_post_list[i].setText(str(res_json[i].get('id')))

    def gift_detail(self):
        gift_detail_url = local_url + "/api/gift/detail/"
        gift_detail_param = {'giftId': self.song_id}
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
        self.play_music()

        self.stackedPages.setCurrentIndex(3)
        self.stackedPages2.setCurrentIndex(3)

    def playMusic1_post(self):
        self.song_id = int(self.post1.text())
        self.gift_detail()

    def playMusic2_post(self):
        self.song_id = int(self.post2.text())
        self.gift_detail()

    def playMusic3_post(self):
        self.song_id = int(self.post3.text())
        self.gift_detail()

    def playMusic4_post(self):
        self.song_id = int(self.post4.text())
        self.gift_detail()

    def playMusic5_post(self):
        self.song_id = int(self.post5.text())
        self.gift_detail()

    def playMusic6_post(self):
        self.song_id = int(self.post6.text())
        self.gift_detail()

    def playMusic7_post(self):
        self.song_id = int(self.post7.text())
        self.gift_detail()

    def playMusic8_post(self):
        self.song_id = int(self.post8.text())
        self.gift_detail()

    def playMusic9_post(self):
        self.song_id = int(self.post9.text())
        self.gift_detail()

    def playMusic10_post(self):
        self.song_id = int(self.post10.text())
        self.gift_detail()

    def scroll_chart_left(self):
        # self.post_scroll_area.scroll(10,0)
        value_now = self.scrollArea.horizontalScrollBar().value()
        if value_now >= 100:
            value_next = value_now - 100
        else:
            value_next = 0
        self.scrollArea.horizontalScrollBar().setValue(value_next)

    def scroll_chart_right(self):
        # self.post_scroll_area.scroll(-10,0)
        value_now = self.scrollArea.horizontalScrollBar().value()
        value_max = self.scrollArea.horizontalScrollBar().maximum()
        if value_now <= value_max - 100:
            value_next = value_now + 100
        else:
            value_next = value_max
        self.scrollArea.horizontalScrollBar().setValue(value_next)

    def scroll_post_left(self):
        #self.post_scroll_area.scroll(10,0)
        value_now = self.post_scroll_area.horizontalScrollBar().value()
        if value_now >= 100:
            value_next = value_now -100
        else:
            value_next = 0
        self.post_scroll_area.horizontalScrollBar().setValue(value_next)

    def scroll_post_right(self):
        #self.post_scroll_area.scroll(-10,0)
        value_now = self.post_scroll_area.horizontalScrollBar().value()
        value_max = self.post_scroll_area.horizontalScrollBar().maximum()
        if value_now <= value_max - 100:
            value_next = value_now + 100
        else:
            value_next = value_max
        self.post_scroll_area.horizontalScrollBar().setValue(value_next)

    def backToChart(self):
        self.stackedPages.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(2)
        self.menu_toolBox.setCurrentIndex(0)
        #self.player.stop()
        self.music_index = 0
        self.play_music()

    def backToPosts(self):
        self.stackedPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(2)
        self.menu_toolBox.setCurrentIndex(1)
        self.music_index = 0
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

    def moveto_reply(self):
        self.stackedPages.setCurrentIndex(5)
        self.stackedPages2.setCurrentIndex(9)

        for i in range(len(self.music_chart)):
            if self.music_chart[i].get("song_id") == self.song_id:
                self.music_index = i;
                break;
        self.reply_song_img.setPixmap(self.show_image(self.music_chart[self.music_index].get('song_img')))
        self.gift_reply_song.setText(self.music_chart[self.music_index].get('song_title'))
        self.gift_reply_singer.setText(self.music_chart[self.music_index].get('singer'))
        song = self.search_result[self.music_index].get('song_title')
        singer = self.search_result[self.music_index].get('singer')
        self.manito_painter_data.setText(song + ' - ' + singer)
        self.play_music()

    def moveto_postcard(self):
        self.stackedPages.setCurrentIndex(11)
        self.stackedPages2.setCurrentIndex(10)

        for i in range(len(self.music_chart)):
            if self.music_chart[i].get("song_id") == self.song_id:
                self.music_index = i;
                break;

        self.reply_song_img.setPixmap(self.show_image(self.music_chart[self.music_index].get('song_img')))
        self.gift_detail_song_4.setText(self.music_chart[self.music_index].get('song_title'))
        self.gift_detail_singer_4.setText(self.music_chart[self.music_index].get('singer'))
        song = self.search_result[self.music_index].get('song_title')
        singer = self.search_result[self.music_index].get('singer')
        self.postcard_painter_data.setText(song + ' - ' + singer)

        self.play_music()

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

        elif self.stackedPages2.currentIndex() == 12:
            self.stackedPages2.setCurrentIndex(2)

        self.stackedPages.setCurrentIndex(currentPage + 1)

    def press_feedback(self, idx):
        emoji_list = [self.count_emoji1, self.count_emoji2, self.count_emoji3, self.count_emoji4]

        gift_detail_url = local_url + "/api/gift/detail"
        gift_detail_param = {'giftId': self.song_id}
        response = requests.get(gift_detail_url, headers=request_header, params=gift_detail_param)
        res_json = response.json()
        emo = res_json.get('emoji')
        cnt_emo = emo.get('emo'+str(idx))
        emoji_list[idx-1].setText(str(cnt_emo + 1))

        gift_feedback_url = local_url + "/api/gift/feedback"
        gift_feedback_param = {'giftId': self.song_id, 'idx': idx}
        requests.get(gift_feedback_url, headers=request_header, params=gift_feedback_param)

    def press_emoji1(self):
        self.press_feedback(1)
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
    def login(self):
        print("로그인")
        req_url = 'http://i8a402.p.ssafy.io/api/spot/token?spotId=1'
        token = ''
        idx = 0

        while True:
            if token != '' or idx > 3:
                break

            print('실행')

            try:
                response = requests.get(req_url)
                token = response.json().get('token')
                print(token)

            except:
                print('토큰 받아오기 실패 !!')

            idx += 1
            time.sleep(5)
        if token != '':
            if self.stackedPages.currentIndex() == 9:
                self.stackedPages.setCurrentIndex(10)
            else:
                self.stackedPages2.setCurrentIndex(4)
        else:
            if self.stackedPages.currentIndex() == 9:
                self.stackedPages.setCurrentIndex(6)
            else:
                self.stackedPages.setCurrentIndex(2)
                self.stackedPages2.setCurrentIndex(2)


    def logout(self):
        req_url = 'http://i8a402.p.ssafy.io/api/spot/token/logout?spotId=1'
        response = requests.get(req_url, headers=request_header)
        self.stackedPages.setCurrentIndex(0)
        self.stackedPages2.setCurrentIndex(2)
        print(response)

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

    def select_radio(self, index):
        self.new_song_id = index
        for i in range(len(self.music_chart)):
            if self.music_chart[i].get("song_id") == index:
                self.music_index = i
                break;

    def show_search(self, scroll_area, grid, type):
        # 기존 검색 결과 비우기
        for i in range(len(self.search_buttons_made)):
            grid.removeWidget(self.search_buttons_made[i])
            self.search_buttons_made[i].deleteLater()
            grid.removeWidget(self.search_labels_made[i])
            self.search_labels_made[i].deleteLater()
        self.search_buttons_made.clear()
        self.search_labels_made.clear()

        for i in range(len(self.search_result)):
            # radio_button 추가 -> 노래/가수
            radio_button = QRadioButton(scroll_area)
            radio_button.setObjectName(u"radioButton_gift_song" + str(i))
            #radio_button.setObjectName(str(self.search_result[i].get('song_id')))
            self.search_buttons_made.append(radio_button)
            radio_button.setMinimumSize(QSize(0, 50))
            size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(radio_button.sizePolicy().hasHeightForWidth())
            radio_button.setSizePolicy(size_policy)
            radio_button.setFont(QFont('Gulim', 16))
            radio_button.setStyleSheet(u"border:2px solid #6522f2; border-top-left-radius: 10px;\n"
                                       "border-bottom-left-radius: 10px; \n"
                                       "border-right:none;\n"
                                       "padding:10px;")

            radio_button.clicked.connect(lambda: self.select_radio(self.search_result[i].get('song_id')))

            grid.addWidget(radio_button, i, 0, 1, 1)

            # radio_label 추가 -> 가수/노래
            radio_label = QLabel(scroll_area)
            radio_label.setObjectName(u"radio_label_gift_song" + str(i))
            self.search_labels_made.append(radio_label)
            size_policy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            size_policy2.setHorizontalStretch(0)
            size_policy2.setVerticalStretch(0)
            size_policy2.setHeightForWidth(radio_label.sizePolicy().hasHeightForWidth())
            radio_label.setSizePolicy(size_policy2)
            radio_label.setFont(QFont('Gulim', 16))
            radio_label.setStyleSheet(u"border:2px solid #6522f2; border-top-right-radius: 10px;\n"
                                      "border-bottom-right-radius: 10px; \n"
                                      "border-left: none;"
                                      "margin-right:10px;"
                                      "padding:10px;")
            radio_label.setMinimumWidth(150)
            radio_label.setAlignment(Qt.AlignCenter)
            grid.addWidget(radio_label, i, 1, 1, 1, Qt.AlignRight)

            if type == 0:   # 제목으로 검색
                radio_button.setText(self.search_result[i].get('song_title'))
                radio_label.setText(self.search_result[i].get('singer'))
            else:           # 가수로 검색
                radio_button.setText(self.search_result[i].get('singer'))
                radio_label.setText(self.search_result[i].get('song_title'))


    def search_song(self):
        if self.stackedPages.currentIndex() == 10:
            text = self.lineEdit_postcard_song.text()
            scroll_area = self.scrollAreaWidgetContents_5
            grid =self.gridLayout_5

        elif self.stackedPages.currentIndex() == 4:
            text = self.lineEdit_gift_song.text()
            scroll_area =self.scrollAreaWidgetContents_3
            grid = self.gridLayout

        song_search_url = local_url + "/api/song/search/title/"
        song_search_param = {'keyword': text}
        response = requests.get(song_search_url, headers=request_header, params=song_search_param)
        self.search_result.clear()
        self.search_result = response.json()

        self.show_search(scroll_area, grid, 0)

    def search_singer(self):
        if self.stackedPages.currentIndex() == 10:
            text = self.lineEdit_postcard_singer.text()
            scroll_area = self.scrollAreaWidgetContents_6
            grid = self.gridLayout_6

        elif self.stackedPages.currentIndex() == 4:
            text = self.lineEdit_gift_singer.text()
            scroll_area = self.scrollAreaWidgetContents_4
            grid = self.gridLayout_4

        song_search_url = local_url + "/api/song/search/singer/"
        song_search_param = {'keyword': text}
        response = requests.get(song_search_url, headers=request_header, params=song_search_param)
        self.search_result.clear()
        self.search_result = response.json()

        self.show_search(scroll_area, grid, 1)

    def show_volume_chart(self):
        visible = self.volume_frame_chart.isVisible()
        self.volume_frame_chart.setVisible(not visible)
    def show_volume_song(self):
        visible = self.volume_frame_song.isVisible()
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
        date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file_name = date_time + '.png'
        self.painter_widget.save("../resource/saved_images/" + file_name)

        # 채팅 서버로 피드백 전송
        url = local_url + "/channel"

        manito_data = manitoDTO = {'userId': 2, 'receiverId': 1, 'userNickname': 'sh', 'contentType': 'IMAGE'}
        now_dir = os.getcwd()
        image_path = f"{now_dir}/../resource/saved_images/" + file_name  # 이미지 경로
        image_name = file_name  # 이미지 이름

        files = {
            "postcardImg": (image_name, open(image_path, "rb"), "image/png")
        }

        payload = {"postcard": json.dumps(manito_data)}

        response = requests.post(url, data=payload, files=files)

        print(response.status_code)


    def post_manito(self):
        self.stackedPages.setCurrentIndex(2)
        self.stackedPages2.setCurrentIndex(2)
        date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file_name = date_time + '.png'
        self.painter_widget_3.save("../resource/saved_images/" + file_name)

        # 서버로 이미지와 마니또 정보 전송
        url = local_url + "/api/manito"

        manito_data = manitoDTO = {'userId': 2, 'songId': self.new_song_id, 'spotId': spot_id, 'beforeManitoId': self.song_id}
        image_path = r"../resource/saved_images/" + file_name   # 이미지 경로
        image_name = file_name  # 이미지 이름


        access_token = request_header
        files = {
            "giftImg": (image_name, open(image_path, "rb"), "image/png")
        }
        headers = {
            'Auth': access_token
        }

        payload = {"manito": json.dumps(manito_data)}
        response = requests.post(url, headers=request_header, data=payload, files=files)
        print(response.status_code)
        self.song_id = self.new_song_id
        self.show_manito_list()

    def save_postcard(self):
        date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file_name = date_time + '.png'
        self.painter_widget_4.save("../resource/saved_images/" + file_name)
        self.postcard_img = file_name

        self.sent_postcard_image.setPixmap(QPixmap("../resource/saved_images/"+file_name))
        self.pw_is_valid = 0
        self.stackedPages.setCurrentIndex(12)
        self.stackedPages2.setCurrentIndex(7)


    def input_code(self):
        self.stackedPages.setCurrentIndex(8)
        postcard_detail_url = local_url + '/api/postcard/detail'
        postcard_data = {'passwd': self.lineEdit.text()}
        response = requests.post(postcard_detail_url, headers=request_header, json=postcard_data)

        res_json = response.json()
        self.postcard_detail_img.setPixmap(QPixmap(res_json.get('postcardImg')))
        self.gift_detail_song_3.setText(res_json.get('songTitle'))
        self.gift_detail_singer_3.setText(res_json.get('singer'))
        self.song_id = res_json.get('id')

        self.video = pafy.new(res_json.get('songUrl'))
        audio_url = self.video.getbestaudio(preftype="m4a").url  # direct link에서 음성만 추출
        self.player.set_uri(audio_url)
        self.player.set_volume(70)

        self.player.play()

    def check_pw_validation(self):
        pw_url = local_url + '/api/postcard/pw'
        pw_data = {'passwd': self.input_password.text()}
        response = requests.post(pw_url, headers=request_header, json=pw_data)

        self.passwd = self.input_password.text()
        self.pw_is_valid = 1

    def send_message(self):
        if self.pw_is_valid == 0:
            QMessageBox.information(self, "알림", "중복확인을 해주세요")
        else:
            phone_number = self.input_phone_number.text()
            add_postcard_url = local_url + "/api/postcard"

            postcard_data = postcardDTO = {
                'nickname': '승호신',
                'phoneNumber': phone_number,
                'passwd': self.passwd,
                'songId': self.song_id,
                'spotId': spot_id,
                'spotName': '멀캠12층',
                'postcardImg': f"../resource/saved_images/{self.postcard_img}"
            }
            image_path = r"../resource/saved_images/" + self.postcard_img  # 이미지 경로
            image_name = self.postcard_img  # 이미지 이름

            # access_token['Content-type'] = 'application/json'
            response = requests.post(add_postcard_url, headers=request_header, json=postcard_data)
            print(response.status_code)
            self.stackedPages.setCurrentIndex(13)
            self.stackedPages2.setCurrentIndex(2)

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

