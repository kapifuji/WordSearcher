import os
import sys
from PyQt5 import QtWidgets, QtGui
from source.GUI import MainWindow
import source.Const as Const


def resource_path(relative) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path("icon.ico")))
    gui = MainWindow(Const.windowName)
    gui.show()

    app.exec_()

if __name__ == "__main__":
    main()