import os
import sys

from PyQt4 import QtGui
from gui.dialog_main.dialog_main import DialogMain
from domain.gslib import GSParams as Params


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    path = os.path.dirname(os.path.realpath(__file__))
    Params.path = path

    MainWindow = QtGui.QMainWindow()
    ui = DialogMain()
    ui.start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())