from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread


class ImageWidget(QWidget):
    def __init__(self, imageData):
        super().__init__()
        self.image = QImage()
        self.image.loadFromData(imageData['data'])
        self.getProperties(self.image, imageData)
        self.initUI(self.image)

    def getProperties(self, image, imageData):
        self.properties = {'null' : 0}
        self.properties['name'] = imageData['name']
        self.properties['url'] = imageData['url']
        self.properties['recolurion'] = "%sx%s" % (image.height(), image.width())
        size = len(imageData['data'])/1024
        if (size // 1024) == 0 :
            self.properties['size'] = "%.2f Кб" % size
        else:
            self.properties['size'] = "%.2f Мб" % (size/1024)

    def _TR(self, text):
        return 'tr(%s)' % text

    def initUI(self, image):
        self.image = QLabel()
        self.image.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.image.setPixmap(QPixmap.fromImage(image))

        vLay = QVBoxLayout()
        self.lab1 = QLabel('<b>Название :</b> %s' % self.properties['name'])
        self.lab2 = QLabel('<b>URL :</b> %s' % self.properties['url'])
        self.lab3 = QLabel('<b>Разрешение :</b> %s' % self.properties['recolurion'])
        self.lab4 = QLabel('<b>Вес :</b> %s' % self.properties['size'])
        self.lab1.setWordWrap(True)
        self.lab2.setWordWrap(True)
        self.lab3.setWordWrap(True)
        self.lab4.setWordWrap(True)
        #self.lab1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #self.lab2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #self.lab3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #self.lab4.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        vLay.addWidget(self.lab1)
        vLay.addWidget(self.lab2)
        vLay.addWidget(self.lab3)
        vLay.addWidget(self.lab4)


        hLay = QHBoxLayout()
        hLay.addWidget(self.image)
        hLay.addLayout(vLay)
        self.setLayout(hLay)


