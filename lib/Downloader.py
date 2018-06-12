from PyQt5.QtCore import QThread, pyqtSignal

import urllib

class DownloadThread(QThread):

    data_downloaded = pyqtSignal(object)

    def __init__(self, url):
        QThread.__init__(self)
        self.url = url

    def run(self):
        data = urllib.request.urlopen(self.url['url']).read()

        self.data_downloaded.emit({'data' : data, 'name' : self.url['name'], 'url' : self.url['url']})
