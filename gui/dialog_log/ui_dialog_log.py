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
        dialogLog.setWindowModality(QtCore.Qt.NonModal)
        dialogLog.resize(720, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../solitonIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogLog.setWindowIcon(icon)
        dialogLog.setSizeGripEnabled(True)
        dialogLog.setModal(False)
        self.gridLayout_2 = QtGui.QGridLayout(dialogLog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(dialogLog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
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
        self.gridLayout.addWidget(self.editLog, 2, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.progressBarStatus = QtGui.QProgressBar(dialogLog)
        self.progressBarStatus.setProperty("value", 24)
        self.progressBarStatus.setObjectName(_fromUtf8("progressBarStatus"))
        self.gridLayout_3.addWidget(self.progressBarStatus, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.labelStatus = QtGui.QLabel(dialogLog)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout_3.addWidget(self.labelStatus, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(dialogLog)
        QtCore.QMetaObject.connectSlotsByName(dialogLog)

    def retranslateUi(self, dialogLog):
        dialogLog.setWindowTitle(_translate("dialogLog", "Log", None))
        self.label.setText(_translate("dialogLog", "Console", None))
        self.labelStatus.setText(_translate("dialogLog", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogLog = QtGui.QDialog()
    ui = Ui_dialogLog()
    ui.setupUi(dialogLog)
    dialogLog.show()
    sys.exit(app.exec_())

