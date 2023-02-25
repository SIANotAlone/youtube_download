
import yt_dlp

from PyQt6.QtWidgets import QFileDialog
import requests
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import uic


class App:
    def __init__(self) -> None:
        pass
    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()

        



    def download_video(self, URL):
        with yt_dlp.YoutubeDL() as ydl:
            ydl.download(URL)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main.ui", self)


        self.download_btn.clicked.connect(self.download_btn_click)

        self.youtube_url.textChanged[str].connect(self.youtube_url_edit)


    def youtube_url_edit(self):
        #print(self.youtube_url.text())
        url = self.youtube_url.text()
        split = url.split('=')
        try:
            id = split[1]
        except IndexError:
            id = 1
        try:
            image = QImage()
            image.loadFromData(requests.get(f'https://i.ytimg.com/vi/{id}/hq720.jpg').content)
            #image = image.scaled(288, 192)
            image = image.scaled(432, 288)

            
            self.preview.setPixmap(QPixmap(image))
        except:
            pass

    def download_btn_click(self):
        with yt_dlp.YoutubeDL() as ydl:
                ydl.download(self.youtube_url.text())
        
        


