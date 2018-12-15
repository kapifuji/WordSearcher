import sys
from GUI import MainWindow
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow("語句検索ツール")
    gui.show()

    app.exec_()

if __name__ == "__main__":
    main()