from PyQt4 import QtGui
from gui.dialog_main.dialog_main import DialogMain


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = DialogMain()
    ui.start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())