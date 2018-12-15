from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import pyperclip
import time
import concurrent.futures

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, windowName):
        super().__init__()
        self.__initWindow(windowName)

    def __initWindow(self, windowName):
        self.setWindowTitle(windowName)
        self.resize(500, 500)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setCentralWidget(MainWidget())

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__setGUI()
        self.__clipThread = ClipBoardObservation()
        self.__clipThread.signal.connect(self.__loadWebPage)
        self.__clipThread.start()
        
    def __setGUI(self):

        # 検索先切り替えボタンなど
        #hLayout = QtWidgets.QHBoxLayout()
        #self.setLayout(hLayout)

        self.__webView = QtWebEngineWidgets.QWebEngineView()
        self.__webView.load(QtCore.QUrl("https://ja.m.wikipedia.org/wiki/大阪"))
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addWidget(self.__webView)
        self.setLayout(vLayout)

    def __loadWebPage(self, clipText):
        self.__webView.load(QtCore.QUrl("https://ja.m.wikipedia.org/wiki/" + clipText))
        #self.__webView.load(QtCore.QUrl("https://ejje.weblio.jp/content/" + clipText))

        """
        self.__webView.setHtml('''
        <!doctype html>
        <a href="https://ja.wikipedia.org/wiki/世界">ぐーぐる</a>
        ''')
        """

class ClipBoardObservation(QtCore.QThread):
    __previousWord = str(pyperclip.paste())
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        while True:
            clipText = str(pyperclip.paste())
            if not self.__previousWord == clipText:
                if not clipText == "":
                    self.signal.emit(clipText)

                self.__previousWord = clipText
                    
            print(clipText)
            time.sleep(0.5)
