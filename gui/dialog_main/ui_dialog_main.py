# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_main.ui'
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

class Ui_dialogMain(object):
    def setupUi(self, dialogMain):
        dialogMain.setObjectName(_fromUtf8("dialogMain"))
        dialogMain.setWindowModality(QtCore.Qt.NonModal)
        dialogMain.resize(910, 400)
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
        dialogMain.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../.designer/solitonIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogMain.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(dialogMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget7 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget7.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget7.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget7.setObjectName(_fromUtf8("stackedWidget7"))
        self.page_17 = QtGui.QWidget()
        self.page_17.setObjectName(_fromUtf8("page_17"))
        self.imageSymbol7 = QtGui.QLabel(self.page_17)
        self.imageSymbol7.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol7.setText(_fromUtf8(""))
        self.imageSymbol7.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_l.png")))
        self.imageSymbol7.setScaledContents(True)
        self.imageSymbol7.setObjectName(_fromUtf8("imageSymbol7"))
        self.labelSymbol7 = QtGui.QLabel(self.page_17)
        self.labelSymbol7.setGeometry(QtCore.QRect(80, 60, 46, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        self.labelSymbol7.setFont(font)
        self.labelSymbol7.setObjectName(_fromUtf8("labelSymbol7"))
        self.stackedWidget7.addWidget(self.page_17)
        self.page_18 = QtGui.QWidget()
        self.page_18.setObjectName(_fromUtf8("page_18"))
        self.stackedWidget7.addWidget(self.page_18)
        self.gridLayout.addWidget(self.stackedWidget7, 0, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 1)
        self.stackedWidget1 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget1.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget1.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget1.setObjectName(_fromUtf8("stackedWidget1"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.imageSymbol1 = QtGui.QLabel(self.page_3)
        self.imageSymbol1.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol1.setText(_fromUtf8(""))
        self.imageSymbol1.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_-.png")))
        self.imageSymbol1.setScaledContents(True)
        self.imageSymbol1.setObjectName(_fromUtf8("imageSymbol1"))
        self.labelSymbol1 = QtGui.QLabel(self.page_3)
        self.labelSymbol1.setGeometry(QtCore.QRect(80, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelSymbol1.setFont(font)
        self.labelSymbol1.setObjectName(_fromUtf8("labelSymbol1"))
        self.stackedWidget1.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.stackedWidget1.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget1, 0, 1, 1, 1)
        self.stackedWidget2 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget2.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget2.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget2.setObjectName(_fromUtf8("stackedWidget2"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.imageSymbol2 = QtGui.QLabel(self.page_5)
        self.imageSymbol2.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol2.setText(_fromUtf8(""))
        self.imageSymbol2.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_0.png")))
        self.imageSymbol2.setScaledContents(True)
        self.imageSymbol2.setObjectName(_fromUtf8("imageSymbol2"))
        self.labelSymbol2 = QtGui.QLabel(self.page_5)
        self.labelSymbol2.setGeometry(QtCore.QRect(80, 60, 61, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        self.labelSymbol2.setFont(font)
        self.labelSymbol2.setObjectName(_fromUtf8("labelSymbol2"))
        self.stackedWidget2.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.stackedWidget2.addWidget(self.page_6)
        self.gridLayout.addWidget(self.stackedWidget2, 0, 4, 1, 1)
        self.stackedWidget6 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget6.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget6.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget6.setObjectName(_fromUtf8("stackedWidget6"))
        self.page_15 = QtGui.QWidget()
        self.page_15.setObjectName(_fromUtf8("page_15"))
        self.imageSymbol6 = QtGui.QLabel(self.page_15)
        self.imageSymbol6.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol6.setText(_fromUtf8(""))
        self.imageSymbol6.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_r.png")))
        self.imageSymbol6.setScaledContents(True)
        self.imageSymbol6.setObjectName(_fromUtf8("imageSymbol6"))
        self.labelSymbol6 = QtGui.QLabel(self.page_15)
        self.labelSymbol6.setGeometry(QtCore.QRect(80, 60, 46, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        self.labelSymbol6.setFont(font)
        self.labelSymbol6.setObjectName(_fromUtf8("labelSymbol6"))
        self.stackedWidget6.addWidget(self.page_15)
        self.page_16 = QtGui.QWidget()
        self.page_16.setObjectName(_fromUtf8("page_16"))
        self.stackedWidget6.addWidget(self.page_16)
        self.gridLayout.addWidget(self.stackedWidget6, 0, 3, 1, 1)
        self.stackedWidget3 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget3.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget3.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget3.setObjectName(_fromUtf8("stackedWidget3"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.imageSymbol3 = QtGui.QLabel(self.page)
        self.imageSymbol3.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol3.setText(_fromUtf8(""))
        self.imageSymbol3.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_+.png")))
        self.imageSymbol3.setScaledContents(True)
        self.imageSymbol3.setObjectName(_fromUtf8("imageSymbol3"))
        self.labelSymbol3 = QtGui.QLabel(self.page)
        self.labelSymbol3.setGeometry(QtCore.QRect(80, 60, 61, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        self.labelSymbol3.setFont(font)
        self.labelSymbol3.setObjectName(_fromUtf8("labelSymbol3"))
        self.stackedWidget3.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget3.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget3, 0, 7, 1, 1)
        self.stackedWidget4 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget4.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget4.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget4.setObjectName(_fromUtf8("stackedWidget4"))
        self.page_11 = QtGui.QWidget()
        self.page_11.setObjectName(_fromUtf8("page_11"))
        self.imageSymbol4 = QtGui.QLabel(self.page_11)
        self.imageSymbol4.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol4.setText(_fromUtf8(""))
        self.imageSymbol4.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_^.png")))
        self.imageSymbol4.setScaledContents(True)
        self.imageSymbol4.setObjectName(_fromUtf8("imageSymbol4"))
        self.labelSymbol4 = QtGui.QLabel(self.page_11)
        self.labelSymbol4.setGeometry(QtCore.QRect(80, 50, 41, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        self.labelSymbol4.setFont(font)
        self.labelSymbol4.setObjectName(_fromUtf8("labelSymbol4"))
        self.stackedWidget4.addWidget(self.page_11)
        self.page_12 = QtGui.QWidget()
        self.page_12.setObjectName(_fromUtf8("page_12"))
        self.stackedWidget4.addWidget(self.page_12)
        self.gridLayout.addWidget(self.stackedWidget4, 0, 2, 1, 1)
        self.stackedWidget5 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget5.setMinimumSize(QtCore.QSize(120, 115))
        self.stackedWidget5.setMaximumSize(QtCore.QSize(120, 115))
        self.stackedWidget5.setObjectName(_fromUtf8("stackedWidget5"))
        self.page_13 = QtGui.QWidget()
        self.page_13.setObjectName(_fromUtf8("page_13"))
        self.imageSymbol5 = QtGui.QLabel(self.page_13)
        self.imageSymbol5.setGeometry(QtCore.QRect(9, 9, 102, 97))
        self.imageSymbol5.setText(_fromUtf8(""))
        self.imageSymbol5.setPixmap(QtGui.QPixmap(_fromUtf8("../solitons_v.png")))
        self.imageSymbol5.setScaledContents(True)
        self.imageSymbol5.setObjectName(_fromUtf8("imageSymbol5"))
        self.labelSymbol5 = QtGui.QLabel(self.page_13)
        self.labelSymbol5.setGeometry(QtCore.QRect(80, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(20)
        self.labelSymbol5.setFont(font)
        self.labelSymbol5.setObjectName(_fromUtf8("labelSymbol5"))
        self.stackedWidget5.addWidget(self.page_13)
        self.page_14 = QtGui.QWidget()
        self.page_14.setObjectName(_fromUtf8("page_14"))
        self.stackedWidget5.addWidget(self.page_14)
        self.gridLayout.addWidget(self.stackedWidget5, 0, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.editLeft = QtGui.QLineEdit(self.centralwidget)
        self.editLeft.setEnabled(False)
        self.editLeft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editLeft.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.editLeft.setObjectName(_fromUtf8("editLeft"))
        self.gridLayout_6.addWidget(self.editLeft, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.button5 = QtGui.QPushButton(self.centralwidget)
        self.button5.setMinimumSize(QtCore.QSize(0, 23))
        self.button5.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button5.setObjectName(_fromUtf8("button5"))
        self.gridLayout_4.addWidget(self.button5, 0, 5, 1, 1)
        self.button6 = QtGui.QPushButton(self.centralwidget)
        self.button6.setMinimumSize(QtCore.QSize(0, 23))
        self.button6.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button6.setObjectName(_fromUtf8("button6"))
        self.gridLayout_4.addWidget(self.button6, 0, 6, 1, 1)
        self.button7 = QtGui.QPushButton(self.centralwidget)
        self.button7.setMinimumSize(QtCore.QSize(0, 23))
        self.button7.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button7.setObjectName(_fromUtf8("button7"))
        self.gridLayout_4.addWidget(self.button7, 0, 7, 1, 1)
        self.button2 = QtGui.QPushButton(self.centralwidget)
        self.button2.setMinimumSize(QtCore.QSize(0, 23))
        self.button2.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button2.setObjectName(_fromUtf8("button2"))
        self.gridLayout_4.addWidget(self.button2, 0, 2, 1, 1)
        self.button3 = QtGui.QPushButton(self.centralwidget)
        self.button3.setMinimumSize(QtCore.QSize(0, 23))
        self.button3.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button3.setObjectName(_fromUtf8("button3"))
        self.gridLayout_4.addWidget(self.button3, 0, 3, 1, 1)
        self.button4 = QtGui.QPushButton(self.centralwidget)
        self.button4.setMinimumSize(QtCore.QSize(0, 23))
        self.button4.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button4.setObjectName(_fromUtf8("button4"))
        self.gridLayout_4.addWidget(self.button4, 0, 4, 1, 1)
        self.button1 = QtGui.QPushButton(self.centralwidget)
        self.button1.setMinimumSize(QtCore.QSize(0, 23))
        self.button1.setMaximumSize(QtCore.QSize(23, 16777215))
        self.button1.setObjectName(_fromUtf8("button1"))
        self.gridLayout_4.addWidget(self.button1, 0, 1, 1, 1)
        self.buttonDelete = QtGui.QPushButton(self.centralwidget)
        self.buttonDelete.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonDelete.setMaximumSize(QtCore.QSize(69, 16777215))
        self.buttonDelete.setObjectName(_fromUtf8("buttonDelete"))
        self.gridLayout_4.addWidget(self.buttonDelete, 0, 8, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 9, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 0, 1, 1, 1)
        self.editCode = QtGui.QLineEdit(self.centralwidget)
        self.editCode.setAlignment(QtCore.Qt.AlignCenter)
        self.editCode.setObjectName(_fromUtf8("editCode"))
        self.gridLayout_6.addWidget(self.editCode, 1, 1, 1, 1)
        self.editRight = QtGui.QLineEdit(self.centralwidget)
        self.editRight.setEnabled(False)
        self.editRight.setObjectName(_fromUtf8("editRight"))
        self.gridLayout_6.addWidget(self.editRight, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 1, 1, 1)
        self.buttonCompute = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonCompute.setFont(font)
        self.buttonCompute.setObjectName(_fromUtf8("buttonCompute"))
        self.gridLayout_5.addWidget(self.buttonCompute, 0, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 4, 1, 1)
        self.buttonBreak = QtGui.QPushButton(self.centralwidget)
        self.buttonBreak.setObjectName(_fromUtf8("buttonBreak"))
        self.gridLayout_5.addWidget(self.buttonBreak, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        dialogMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(dialogMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGap = QtGui.QMenu(self.menubar)
        self.menuGap.setObjectName(_fromUtf8("menuGap"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuResults = QtGui.QMenu(self.menubar)
        self.menuResults.setObjectName(_fromUtf8("menuResults"))
        dialogMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(dialogMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        dialogMain.setStatusBar(self.statusbar)
        self.actionGap = QtGui.QAction(dialogMain)
        self.actionGap.setObjectName(_fromUtf8("actionGap"))
        self.actionParams = QtGui.QAction(dialogMain)
        self.actionParams.setObjectName(_fromUtf8("actionParams"))
        self.actionAbout = QtGui.QAction(dialogMain)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_parameters = QtGui.QAction(dialogMain)
        self.actionAbout_parameters.setObjectName(_fromUtf8("actionAbout_parameters"))
        self.actionCoding = QtGui.QAction(dialogMain)
        self.actionCoding.setObjectName(_fromUtf8("actionCoding"))
        self.actionLog = QtGui.QAction(dialogMain)
        self.actionLog.setObjectName(_fromUtf8("actionLog"))
        self.actionPlot = QtGui.QAction(dialogMain)
        self.actionPlot.setObjectName(_fromUtf8("actionPlot"))
        self.menuGap.addAction(self.actionCoding)
        self.menuGap.addAction(self.actionParams)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_parameters)
        self.menuResults.addAction(self.actionLog)
        self.menuResults.addAction(self.actionPlot)
        self.menubar.addAction(self.menuGap.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(dialogMain)
        QtCore.QMetaObject.connectSlotsByName(dialogMain)

    def retranslateUi(self, dialogMain):
        dialogMain.setWindowTitle(_translate("dialogMain", "Gap Soliton Assembler", None))
        self.labelSymbol7.setText(_translate("dialogMain", "7", None))
        self.labelSymbol1.setText(_translate("dialogMain", "1", None))
        self.labelSymbol2.setText(_translate("dialogMain", "2", None))
        self.labelSymbol6.setText(_translate("dialogMain", "6", None))
        self.labelSymbol3.setText(_translate("dialogMain", "3", None))
        self.labelSymbol4.setText(_translate("dialogMain", "4", None))
        self.labelSymbol5.setText(_translate("dialogMain", "5", None))
        self.editLeft.setText(_translate("dialogMain", "0", None))
        self.button5.setText(_translate("dialogMain", "5", None))
        self.button6.setText(_translate("dialogMain", "6", None))
        self.button7.setText(_translate("dialogMain", "7", None))
        self.button2.setText(_translate("dialogMain", "2", None))
        self.button3.setText(_translate("dialogMain", "3", None))
        self.button4.setText(_translate("dialogMain", "4", None))
        self.button1.setText(_translate("dialogMain", "1", None))
        self.buttonDelete.setText(_translate("dialogMain", "Delete", None))
        self.label.setText(_translate("dialogMain", "Left tail", None))
        self.label_2.setText(_translate("dialogMain", "Main part", None))
        self.editRight.setText(_translate("dialogMain", "0", None))
        self.label_3.setText(_translate("dialogMain", "Right tail", None))
        self.buttonCompute.setText(_translate("dialogMain", "Compute", None))
        self.buttonBreak.setText(_translate("dialogMain", "Break", None))
        self.menuGap.setTitle(_translate("dialogMain", "Parameters", None))
        self.menuHelp.setTitle(_translate("dialogMain", "About", None))
        self.menuResults.setTitle(_translate("dialogMain", "Results", None))
        self.actionGap.setText(_translate("dialogMain", "Gaps", None))
        self.actionParams.setText(_translate("dialogMain", "Numerical computation", None))
        self.actionAbout.setText(_translate("dialogMain", "About program", None))
        self.actionAbout_parameters.setText(_translate("dialogMain", "About parameters", None))
        self.actionCoding.setText(_translate("dialogMain", "Symbolic dynamics", None))
        self.actionLog.setText(_translate("dialogMain", "Log", None))
        self.actionPlot.setText(_translate("dialogMain", "Plot", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialogMain = QtGui.QMainWindow()
    ui = Ui_dialogMain()
    ui.setupUi(dialogMain)
    dialogMain.show()
    sys.exit(app.exec_())
