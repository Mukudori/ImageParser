from PyQt5.QtWidgets import QMainWindow, QLabel, QHeaderView
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
import threading


import urllib

from lib import Parser


class DownloadThread(QThread):

    data_downloaded = pyqtSignal(object)

    def __init__(self, url):
        QThread.__init__(self)
        self.url = url

    def run(self):
        data = urllib.request.urlopen(self.url).read()
        self.data_downloaded.emit(data)



class MainForm(QMainWindow, QThread):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/mainForm.ui',self)
        self.act_download.triggered.connect(self.ViewImages)
        self.widget=0


    def RefreshTable(self):
        self.th1 = threading.Thread(target=self.startDownload)
        self.th1.start()


    def ViewImages(self):
        self.RefreshTable()



    def startDownload(self):
        urlList = Parser.Get_IMG_Urls(self.leURL.text())
        self.twMain.clear()
        n = 3
        #w.horizontalHeader()->resizeSections(QHeaderView::ResizeToContents);
        self.twMain.setRowCount(len(urlList) // n)
        self.twMain.setColumnCount(n)
        self.twMain.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
        self.twMain.verticalHeader().resizeSections(QHeaderView.ResizeToContents)
        self.i = 0
        self.j = 0
        self.threads = []
        for url in urlList:

            #data = urllib.request.urlopen(url).read()
            downloader = DownloadThread(url)
            downloader.data_downloaded.connect(self.on_data_ready)
            self.threads.append(downloader)
            downloader.start()

    def on_data_ready(self, data):

            image = QImage()
            image.loadFromData(data)

            widget = QLabel()
            widget.setPixmap(QPixmap(image))
            widget.setMinimumWidth(200)
            widget.setMinimumHeight(200)

            self.twMain.setCellWidget(self.i, self.j, widget)
            if (self.j < self.twMain.columnCount()):
                self.j += 1
            else:
                self.j = 0
                self.i += 1




