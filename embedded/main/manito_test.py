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

from client import Client
import logging

# http get 요청
# local_url -> 추후 서버 주소로 변경
#local_url = "http://localhost:8080"
local_url = "http://i8a402.p.ssafy.io:80"

request_header = {
    'Auth': 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiUk9MRV9VU0VSIiwidXNlcklkIjoxOSwibmlja05hbWUiOiLsgqzsmqnsnpAxOSIsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE2NzY1MDU3MDksImV4cCI6MTY3NjU2NTcwOX0.xoz54g77UvDeUMZcTSK9vQwO0G9S60eZwXQeyLst4nk'
}

date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
file_name = date_time + '.png'
print("manito saved!")

# 서버로 이미지와 마니또 정보 전송
url = local_url + "/api/manito"
manito_data = manitoDTO = {'userId': 2, 'songId': 1, 'spotId': 1, 'beforeManitoId': 1}
print("manito data")
image_path = r"../resource/saved_images/230216_105602.png"   # 이미지 경로
print(image_path)
image_name = "230216_105602.png"  # 이미지 이름
print(image_name)

access_token = request_header
files = {
    "giftImg": (image_name, open(image_path, "rb"), "image/png")
}
headers = {
    'Auth': access_token
}

payload = {"manito": json.dumps(manito_data)}
print("before")
response = requests.post(url, headers=request_header, data=payload, files=files)
print(response.status_code)