from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import pyperclip
import time
import source.Const as Const

class MainWindow(QtWidgets.QMainWindow):
    """ウインドウ統括用クラス"""

    def __init__(self, windowName):
        super().__init__()
        self.__initWindow(windowName)

    def __initWindow(self, windowName):
        """ウインドウタイトル、画面サイズ、最前面表示"""
        self.setWindowTitle(windowName)
        self.resize(Const.windowSizeX, Const.windowSizeY)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setCentralWidget(MainWidget())

class MainWidget(QtWidgets.QWidget):
    """GUI構成、GUI関連処理用クラス"""

    def __init__(self):
        """GUIの構成とクリップボード監視スレッド開始"""
        super().__init__()
        self.__setGUI()
        self.__clipThread = ClipBoardObservation()
        self.__clipThread.signal.connect(self.__loadWebPage)
        self.__clipThread.start()
        
    def __setGUI(self):
        """WebView部分とナビゲーション部分のUIを結合"""
        wrapLayout = QtWidgets.QVBoxLayout()
        wrapLayout.addLayout(self.__getNavigationLayout())
        wrapLayout.addLayout(self.__getWebViewLayout())

        self.setLayout(wrapLayout)
    
    def __getNavigationLayout(self):
        """前後ボタンと検索先変更プルダウンメニューを構成"""
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
        """WebViewを構成"""
        vLayout = QtWidgets.QVBoxLayout()
        self.__webView = QtWebEngineWidgets.QWebEngineView()
        webProfile = QtWebEngineWidgets.QWebEngineProfile(self.__webView)
        webProfile.setHttpUserAgent(Const.webViewUA)
        webPage = QtWebEngineWidgets.QWebEnginePage(webProfile, self)
        self.__webView.setPage(webPage)
        self.__webView.setHtml(Const.welcomePage)
        vLayout.addWidget(self.__webView)

        return vLayout

    def __loadWebPage(self, clipText: str, refer: str = None):
        """
        クリップボード変化時と検索変更時に呼ばれる。
        クリップボードの語句で指定検索先を検索。
        """
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
        """
        0.5秒おきにクリップボードを検査。
        変化があれば検索を実行。
        """
        while True:
            clipText = str(pyperclip.paste())
            if not self.__previousWord == clipText:
                self.signal.emit(clipText)
                self.__previousWord = clipText
                    
            time.sleep(0.5)