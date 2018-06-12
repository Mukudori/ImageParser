from PyQt5.QtWidgets import QMainWindow, QLabel, QHeaderView, QListWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread

import threading


from lib.Downloader import DownloadThread
from lib import Parser
from lib.ImageWidgetModule import ImageWidget





class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/mainForm.ui',self)
        self.initUI()
        self.connectSlots()

    def RefreshTable(self):
        self.th1 = threading.Thread(target=self.startDownload)
        self.th1.start()

    def ViewImages(self):
        self.RefreshTable()

    def initUI(self):
        self.widget = 0
        self.visibleBlock = True
        self.setVisibleBlock()

    def setVisibleBlock(self):
        vis = not self.visibleBlock
        self.label_2.setVisible(vis)
        self.lwBlock.setVisible(vis)
        self.visibleBlock = vis

    def connectSlots(self):
        self.act_download.triggered.connect(self.ViewImages)
        self.actBlockView.triggered.connect(self.setVisibleBlock)

    def startDownload(self):
        urlList = Parser.Get_IMG_Urls(self.leURL.text())
        self.lwMain.clear()
        #self.lwMain.setRowCount(len(urlList) // self.ColumnCount)
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
            image.loadFromData(data['data'])
            #image = image.scaled(200,200)

            widget = ImageWidget(data)
            #widget.setPixmap(QPixmap(image))
            #widget.setMinimumWidth(200)
            #widget.setMinimumHeight(200)

            '''self.lwMain.setCellWidget(self.i, self.j, widget)
            self.lwMain.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
            self.lwMain.verticalHeader().resizeSections(QHeaderView.ResizeToContents)
            if (self.j < self.twMain.columnCount()):
                self.j += 1
            else:
                self.j = 0
                self.i += 1
            self.lwMain.addItem(widget)'''

            myQListWidgetItem = QListWidgetItem(self.lwMain)
            # Set size hint
            myQListWidgetItem.setSizeHint(widget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.lwMain.addItem(myQListWidgetItem)
            self.lwMain.setItemWidget(myQListWidgetItem, widget)




