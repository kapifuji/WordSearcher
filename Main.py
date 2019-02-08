import sys
from PyQt5 import QtWidgets
from source.GUI import MainWindow
import source.Const as Const

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow(Const.windowName)
    gui.show()

    app.exec_()

if __name__ == "__main__":
    main()