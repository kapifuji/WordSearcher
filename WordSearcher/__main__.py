##
##    Copyright (C) 2021 kapifuji
##
##    This file is part of WordSearcher.
##
##    WordSearcher is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License.
##
##
##    WordSearcher is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with WordSearcher.  If not, see <https://www.gnu.org/licenses/>.
##

import os
import sys
from PyQt5 import QtWidgets, QtGui
from GUI import MainWindow
import Const


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