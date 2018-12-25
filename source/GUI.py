from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import pyperclip
import time
import Const

class MainWindow(QtWidgets.QMainWindow):
    """ウインドウ統括用クラス"""

    def __init__(self, windowName):
        super().__init__()
        self.__initWindow(windowName)

    def __initWindow(self, windowName):
        self.setWindowTitle(windowName)
        self.resize(Const.windowSizeX, Const.windowSizeY)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setCentralWidget(MainWidget())

class MainWidget(QtWidgets.QWidget):
    """GUI構成、GUI関連処理用クラス"""

    def __init__(self):
        super().__init__()
        self.__setGUI()
        self.__clipThread = ClipBoardObservation()
        self.__clipThread.signal.connect(self.__loadWebPage)
        self.__clipThread.start()
        
    def __setGUI(self):
        wrapLayout = QtWidgets.QVBoxLayout()
        wrapLayout.addLayout(self.__getNavigationLayout())
        wrapLayout.addLayout(self.__getWebViewLayout())

        self.setLayout(wrapLayout)
    
    def __getNavigationLayout(self):
        hLayout = QtWidgets.QHBoxLayout()

        backButton = QtWidgets.QPushButton("←")
        backButton.clicked.connect(lambda: self.__webView.back())
        hLayout.addWidget(backButton, 1)

        forwardButton = QtWidgets.QPushButton("→")
        forwardButton.clicked.connect(lambda: self.__webView.forward())
        hLayout.addWidget(forwardButton, 1)

        hLayout.addStretch(1)

        self.__refComboBox = QtWidgets.QComboBox()
        self.__refComboBox.addItems(Const.searchRef.keys())
        self.__refComboBox.activated[str].connect(
            lambda label: self.__loadWebPage(self.__clipThread.getPreviousWord(), label))
        hLayout.addWidget(self.__refComboBox, 4)
        
        return hLayout

    def __getWebViewLayout(self):
        vLayout = QtWidgets.QVBoxLayout()
        self.__webView = QtWebEngineWidgets.QWebEngineView()
        self.__webView.load(QtCore.QUrl("https://github.com/rpianna/WordSeacher/blob/master/README.md"))
        vLayout.addWidget(self.__webView)

        return vLayout

    def __loadWebPage(self, clipText: str, refer: str = None):
        if clipText == "":
            return
        if (refer is None) or (refer not in Const.searchRef.keys()):
            refer = self.__refComboBox.currentText()

        self.__webView.load(QtCore.QUrl(Const.searchRef[refer] + clipText))

class ClipBoardObservation(QtCore.QThread):
    """クリップボード監視スレッド用クラス"""

    __previousWord = str(pyperclip.paste())
    signal = QtCore.pyqtSignal(str)

    def getPreviousWord(self) -> str:
        return self.__previousWord

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        while True:
            clipText = str(pyperclip.paste())
            if not self.__previousWord == clipText:
                self.signal.emit(clipText)
                self.__previousWord = clipText
                    
            print(clipText)
            time.sleep(0.5)