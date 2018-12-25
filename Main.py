import sys
from source.GUI import MainWindow
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow("WordSeacher")
    gui.show()

    app.exec_()

if __name__ == "__main__":
    main()