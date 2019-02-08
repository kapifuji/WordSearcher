from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import pyperclip
import time
import source.Const as Const

class MainWindow(QtWidgets.QMainWindow):
    """ウインドウ統括用クラス"""

    def __init__(self, windowName) -> None:
        super().__init__()
        self.__initWindow(windowName)

    def __initWindow(self, windowName) -> None:
        """ウインドウタイトル、画面サイズ、最前面表示"""

        self.setWindowTitle(windowName)
        self.resize(Const.windowSizeX, Const.windowSizeY)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setCentralWidget(MainWidget())

class MainWidget(QtWidgets.QWidget):
    """GUI構成、GUI関連処理用クラス"""

    def __init__(self) -> None:
        """GUIの構成とクリップボード監視スレッド開始"""

        super().__init__()
        self.__setGUI()
        self.__clipThread = ClipBoardObservation()
        # signalにMainWidget.__loadWebPageを登録（ClipBoardObservation.runのsignal.emitで呼び出し）
        self.__clipThread.signal.connect(self.__loadWebPage)
        self.__clipThread.start()
        
    def __setGUI(self) -> None:
        """WebView部分とナビゲーション部分のUIを結合し、GUIとして登録"""

        wrapLayout = QtWidgets.QVBoxLayout()
        wrapLayout.addLayout(self.__getNavigationLayout())
        wrapLayout.addLayout(self.__getWebViewLayout())

        self.setLayout(wrapLayout)
    
    def __getNavigationLayout(self):
        """前後ボタンと検索先変更プルダウンメニューを構成して返却"""

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
        # プルダウンメニューで検索先が変更されたとき、self.__loadWebPageを呼んで画面更新
        self.__refComboBox.activated[str].connect(
            lambda label: self.__loadWebPage(self.__clipThread.getPreviousWord(), label))
        hLayout.addWidget(self.__refComboBox, 4)
        
        return hLayout

    def __getWebViewLayout(self):
        """WebViewを構成して返却"""

        vLayout = QtWidgets.QVBoxLayout()
        self.__webView = QtWebEngineWidgets.QWebEngineView()

        # UserAgentを変更する処理
        webProfile = QtWebEngineWidgets.QWebEngineProfile(self.__webView)
        webProfile.setHttpUserAgent(Const.webViewUA)
        webPage = QtWebEngineWidgets.QWebEnginePage(webProfile, self)
        self.__webView.setPage(webPage)

        self.__webView.setHtml(Const.welcomePage)
        vLayout.addWidget(self.__webView)

        return vLayout

    def __loadWebPage(self, clipText: str, refer: str = None) -> None:
        """
        指定した検索先で語句を検索して結果を表示します。
        
        Arguments:
            clipText {str} -- 検索したい語句
        
        Keyword Arguments:
            refer {str} -- 検索先　指定しない場合はプルダウンメニューの値を取得 (default: {None})
        
        Returns:
            None
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
        """1つ前に保存されていた語句を取得
        
        Returns:
            str -- 1つ前に保存されていた語句
        """

        return self.__previousWord

    def __init__(self) -> None:
        QtCore.QThread.__init__(self)

    def run(self) -> None:
        """
        0.5秒毎にクリップボードを検査　
        変化があれば検索を実行
        """
        
        while True:
            clipText = str(pyperclip.paste())
            if not self.__previousWord == clipText:
                # MainWidget.__loadWebPageを実行
                self.signal.emit(clipText)
                self.__previousWord = clipText
                    
            time.sleep(0.5)