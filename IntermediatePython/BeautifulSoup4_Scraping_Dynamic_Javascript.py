import bs4 as bs
import urllib.request
import sys
from PyQt4.QtGui import QApplication # easy for making the applications
from PyQt4.QtCore import QUrl # for reading URLS
from PyQt4.QtWebKit import QWebPage # this will help in loading the page and acts like browser and runs the java script

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
    def on_page_load(self):
        self.app.quit()
url='https://pythonprogramming.net/parsememcparseface/'
client_response=Client(url)
source=client_response.mainFrame().toHtml()

#source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(source,'lxml')

js_test = soup.find('p', class_='jstest')
print(js_test)