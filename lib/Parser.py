from html.parser import HTMLParser
import urllib.request
import sys

urlString = "http://joyreactor.cc"

def SaveImage(url, path='/data/'):
    u = urllib.request.urlopen(url)
    data = u.read()

    splitPath = url.split('/')
    fName = splitPath.pop()


    f = open(path+fName, 'wb')
    f.write(data)
    f.close()

class parseImages(HTMLParser):
    def setList(self, srcList):
        self.urlList = srcList
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src' and 'http' in value:
                    if '.' in value.split('/').pop():
                   # getImage(urlString + "/" + value)
                        self.urlList.append(value)

def Get_IMG_Urls(urlStr=urlString):
    if len(urlStr)<5:
        urlStr=urlString
    lParser = parseImages()
    u = urllib.request.urlopen(urlStr)
    print(u.info())
    urlList = []
    lParser.setList(urlList)
    lParser.feed(u.read().decode('utf-8'))
    lParser.close()
    return urlList

def Get_IMG_Data_From_Url(url):
    pass