import os

from PyQt4 import QtCore, QtGui
from ui_dialog_plot import Ui_dialogPlot


class DialogPlot(QtGui.QDialog, Ui_dialogPlot):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        flags = QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
        self.setWindowFlags(flags)
        self.start()

    def start(self):
        self.setupUi(self)
        self.comboBoxHistory.currentIndexChanged.connect(self.on_index_changed)

    def on_opened(self):
        self.show()
        self.activateWindow()
        self.setFocus()

        self.on_updated()

    def on_closed(self):
        self.close()

    def on_updated(self):
        cur_dir = os.getcwd()
        res_dir = cur_dir + '/result'
        all_list = os.listdir(res_dir)
        png_list = [os.path.join(res_dir, i) for i in all_list if i.endswith('.png')]
        sorted_list = sorted(png_list, key=os.path.getatime)
        sorted_codes = [os.path.basename(i) for i in sorted_list]
        sorted_codes = [i.split('.')[0] for i in sorted_codes]

        self.comboBoxHistory.clear()
        self.comboBoxHistory.addItems(sorted_codes[::-1])

        png = res_dir + '/' + self.comboBoxHistory.currentText() + '.png'
        self.imagePlot.setPixmap(QtGui.QPixmap(png))

    def on_index_changed(self):
        cur_dir = os.getcwd()
        res_dir = cur_dir + '/result'
        png = res_dir + '/' + self.comboBoxHistory.currentText() + '.png'
        self.imagePlot.setPixmap(QtGui.QPixmap(png))