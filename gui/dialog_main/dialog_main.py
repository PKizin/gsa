import os
import ctypes
from threading import Thread
from validator import CodeValidator
from domain.gslib import GSParams as Params
from domain.gslib import GSCoding as Coder

from PyQt4 import QtCore, QtGui
from ui_dialog_main import Ui_dialogMain
from gui.dialog_params.dialog_params import DialogParams
from gui.dialog_coding.dialog_coding import DialogCoding
from gui.dialog_log.dialog_log import DialogLog
from gui.dialog_plot.dialog_plot import DialogPlot


class DialogMain(QtGui.QDialog, Ui_dialogMain):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.dialog_params = DialogParams()
        self.dialog_coding = DialogCoding()
        self.dialog_log = DialogLog()
        self.dialog_plot = DialogPlot()
        self.code_validator = CodeValidator()
        self.code_length = 1
        self.code_thread = Thread(target=Coder.make_state, args=('', '', ))
        pid = '0.0.0.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(pid)

    def start(self, dialog_main):
        self.setupUi(dialog_main)

        path = os.path.dirname(os.path.realpath(__file__)) + '\..\\'
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(
                       path + "solitonIcon.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog_main.setWindowIcon(icon)
        self.dialog_params.setWindowIcon(icon)
        self.dialog_coding.setWindowIcon(icon)
        self.dialog_coding.update_image()
        self.dialog_log.setWindowIcon(icon)
        self.dialog_plot.setWindowIcon(icon)

        self.imageSymbol1.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_-.png")))
        self.imageSymbol2.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_0.png")))
        self.imageSymbol3.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_+.png")))
        self.imageSymbol4.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_^.png")))
        self.imageSymbol5.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_v.png")))
        self.imageSymbol6.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_r.png")))
        self.imageSymbol7.setPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(path + "solitons_l.png")))

        self.actionParams.triggered.connect(self.dialog_params.on_opened)
        self.actionCoding.triggered.connect(self.dialog_coding.on_opened)
        self.actionLog.triggered.connect(self.dialog_log.on_opened)
        self.actionPlot.triggered.connect(self.dialog_plot.on_opened)

        self.dialog_log.solitonAssembled.connect(self.dialog_plot.on_opened)

        self.dialog_coding.buttonCodingOK.clicked.connect(self.update_data)
        self.dialog_params.buttonParamsOK.clicked.connect(self.update_data)

        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)
        self.button4.clicked.connect(self.on_button4_clicked)
        self.button5.clicked.connect(self.on_button5_clicked)
        self.button6.clicked.connect(self.on_button6_clicked)
        self.button7.clicked.connect(self.on_button7_clicked)
        self.buttonDelete.clicked.connect(self.on_button_delete_clicked)
        self.buttonCompute.clicked.connect(self.on_button_compute_clicked)
        self.buttonBreak.clicked.connect(self.on_button_break_clicked)

        self.editCode.setValidator(self.code_validator)
        self.editCode.setReadOnly(True)

        self.update_data()

    def update_data(self):
        self.editLeft.setText('0' * Params.left_tail)
        self.editCode.setText('')
        self.editRight.setText('0' * Params.right_tail)
        self.button1.setText(Params.alphabet[0])
        self.button2.setText(Params.alphabet[1])
        self.button3.setText(Params.alphabet[2])
        if Params.gap == 1:
            self.button4.setVisible(False)
            self.button5.setVisible(False)
            self.button6.setVisible(False)
            self.button7.setVisible(False)
            self.stackedWidget4.setVisible(False)
            self.stackedWidget5.setVisible(False)
            self.stackedWidget6.setVisible(False)
            self.stackedWidget7.setVisible(False)
            self.labelSymbol1.setText(Params.alphabet[0])
            self.labelSymbol2.setText(Params.alphabet[1])
            self.labelSymbol3.setText(Params.alphabet[2])
        elif Params.gap == 2:
            self.button4.setVisible(True)
            self.button5.setVisible(True)
            self.button6.setVisible(False)
            self.button7.setVisible(False)
            self.button4.setText(Params.alphabet[3])
            self.button5.setText(Params.alphabet[4])
            self.stackedWidget4.setVisible(True)
            self.stackedWidget5.setVisible(True)
            self.stackedWidget6.setVisible(False)
            self.stackedWidget7.setVisible(False)
            self.labelSymbol1.setText(Params.alphabet[0])
            self.labelSymbol2.setText(Params.alphabet[2])
            self.labelSymbol3.setText(Params.alphabet[4])
            self.labelSymbol4.setText(Params.alphabet[1])
            self.labelSymbol5.setText(Params.alphabet[3])
        elif Params.gap == 3:
            self.button4.setVisible(True)
            self.button5.setVisible(True)
            self.button6.setVisible(True)
            self.button7.setVisible(True)
            self.button4.setText(Params.alphabet[3])
            self.button5.setText(Params.alphabet[4])
            self.button6.setText(Params.alphabet[5])
            self.button7.setText(Params.alphabet[6])
            self.stackedWidget4.setVisible(True)
            self.stackedWidget5.setVisible(True)
            self.stackedWidget6.setVisible(True)
            self.stackedWidget7.setVisible(True)
            self.labelSymbol1.setText(Params.alphabet[0])
            self.labelSymbol2.setText(Params.alphabet[3])
            self.labelSymbol3.setText(Params.alphabet[6])
            self.labelSymbol4.setText(Params.alphabet[1])
            self.labelSymbol5.setText(Params.alphabet[5])
            self.labelSymbol6.setText(Params.alphabet[2])
            self.labelSymbol7.setText(Params.alphabet[4])

    def on_button1_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button1.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button2_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button2.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button3_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button3.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button4_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button4.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button5_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button5.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button6_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button6.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button7_clicked(self):
        s1 = self.editCode.text()
        s2 = self.button7.text()
        if self.code_length >= 20:
            return
        if s2.size() == 1:
            self.editCode.setText(s1 + s2)
        else:
            self.editCode.setText(s1 + '(' + s2 + ')')
        self.code_length += 1

    def on_button_delete_clicked(self):
        s = str(self.editCode.text())
        n = s.__len__()
        if n == 0:
            return
        if s[n-1] == ')':
            while s[n-1] != '(':
                s = s[:-1]
                n = s.__len__()
        s = s[:-1]
        self.editCode.setText(s)
        self.code_length -= 1

    def on_button_compute_clicked(self):
        self.dialog_log.on_opened()
        s = str(self.editCode.text())
        for i in range(Params.left_tail):
            s = '0' + s
        for i in range(Params.right_tail):
            s += '0'
        s = s.replace('(', '')
        s = s.replace(')', '')
        if Params.gap == 1:
            s = s.replace(Params.alphabet[0], '|' + Params.alphabet[0])
            s = s.replace(Params.alphabet[1], '|' + Params.alphabet[1])
            s = s.replace(Params.alphabet[2], '|' + Params.alphabet[2])
            if not Params.thread_state:
                self.code_thread = Thread(target=Coder.make_state, args=(s[1:].split('|'), ))
                Params.thread_state = True
                self.code_thread.start()
        elif Params.gap == 2:
            s = s.replace(Params.alphabet[0], '|' + Params.alphabet[0])
            s = s.replace(Params.alphabet[1], '|' + Params.alphabet[1])
            s = s.replace(Params.alphabet[2], '|' + Params.alphabet[2])
            s = s.replace(Params.alphabet[3], '|' + Params.alphabet[3])
            s = s.replace(Params.alphabet[4], '|' + Params.alphabet[4])
            if not Params.thread_state:
                self.code_thread = Thread(target=Coder.make_state, args=(s[1:].split('|'), ))
                Params.thread_state = True
                self.code_thread.start()
        elif Params.gap == 3:
            s = s.replace(Params.alphabet[0], '|' + Params.alphabet[0])
            s = s.replace(Params.alphabet[1], '|' + Params.alphabet[1])
            s = s.replace(Params.alphabet[2], '|' + Params.alphabet[2])
            s = s.replace(Params.alphabet[3], '|' + Params.alphabet[3])
            s = s.replace(Params.alphabet[4], '|' + Params.alphabet[4])
            s = s.replace(Params.alphabet[5], '|' + Params.alphabet[5])
            s = s.replace(Params.alphabet[6], '|' + Params.alphabet[6])
            if not Params.thread_state:
                self.code_thread = Thread(target=Coder.make_state, args=(s[1:].split('|'), ))
                Params.thread_state = True
                self.code_thread.start()

    def on_button_break_clicked(self):
        if Params.thread_state:
            Params.thread_state = False
            self.code_thread.join()