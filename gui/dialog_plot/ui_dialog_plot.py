# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_plot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialogPlot(object):
    def setupUi(self, dialogPlot):
        dialogPlot.setObjectName(_fromUtf8("dialogPlot"))
        dialogPlot.resize(878, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../solitonIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogPlot.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(dialogPlot)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(dialogPlot)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.comboBoxHistory = QtGui.QComboBox(dialogPlot)
        self.comboBoxHistory.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxHistory.setObjectName(_fromUtf8("comboBoxHistory"))
        self.gridLayout_3.addWidget(self.comboBoxHistory, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(dialogPlot)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.imagePlot = QtGui.QLabel(dialogPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePlot.sizePolicy().hasHeightForWidth())
        self.imagePlot.setSizePolicy(sizePolicy)
        self.imagePlot.setMinimumSize(QtCore.QSize(0, 0))
        self.imagePlot.setMaximumSize(QtCore.QSize(50000, 50000))
        self.imagePlot.setText(_fromUtf8(""))
        self.imagePlot.setPixmap(QtGui.QPixmap(_fromUtf8("../../result/0+0.png")))
        self.imagePlot.setScaledContents(True)
        self.imagePlot.setObjectName(_fromUtf8("imagePlot"))
        self.gridLayout_4.addWidget(self.imagePlot, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(dialogPlot)
        QtCore.QMetaObject.connectSlotsByName(dialogPlot)

    def retranslateUi(self, dialogPlot):
        dialogPlot.setWindowTitle(_translate("dialogPlot", "Plot", None))
        self.label.setText(_translate("dialogPlot", "History", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogPlot = QtGui.QDialog()
    ui = Ui_dialogPlot()
    ui.setupUi(dialogPlot)
    dialogPlot.show()
    sys.exit(app.exec_())

