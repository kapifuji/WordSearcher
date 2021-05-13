##
##    Copyright (C) 2021 kapifuji
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import os
import sys
from cx_Freeze import setup, Executable

_VERSION = "1.0.1"

_SOURCE_FOLDER = "WordSearcher"
_MAIN = "__main__.py"

exe = Executable(
    script = _SOURCE_FOLDER + "/" + _MAIN,
    base = "Win32GUI",
    target_name="WordSearcher",
    icon="icon.ico")

packages = []

includes = [
    "PyQt5",
    "pyperclip",
]

excludes = []

build_exe_options = {
    "includes": includes, "excludes": excludes, "path": sys.path + [_SOURCE_FOLDER]
}

setup(name = "WordSearcher",
      options = {"build_exe": build_exe_options},
      version = _VERSION,
      executables = [exe])