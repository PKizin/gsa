# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_log.ui'
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

class Ui_dialogLog(object):
    def setupUi(self, dialogLog):
        dialogLog.setObjectName(_fromUtf8("dialogLog"))
        dialogLog.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../solitonIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogLog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(dialogLog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editLog = QtGui.QTextEdit(dialogLog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.editLog.setPalette(palette)
        self.editLog.setReadOnly(True)
        self.editLog.setObjectName(_fromUtf8("editLog"))
        self.gridLayout.addWidget(self.editLog, 1, 0, 1, 1)
        self.label = QtGui.QLabel(dialogLog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(dialogLog)
        QtCore.QMetaObject.connectSlotsByName(dialogLog)

    def retranslateUi(self, dialogLog):
        dialogLog.setWindowTitle(_translate("dialogLog", "Log", None))
        self.label.setText(_translate("dialogLog", "Console", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogLog = QtGui.QDialog()
    ui = Ui_dialogLog()
    ui.setupUi(dialogLog)
    dialogLog.show()
    sys.exit(app.exec_())

