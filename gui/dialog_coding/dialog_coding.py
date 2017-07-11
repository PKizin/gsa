import os
import sys
from PyQt4 import QtCore, QtGui
from ui_dialog_coding import Ui_dialogCoding
from domain.gslib import GSParams as Params


class DialogCoding(QtGui.QDialog, Ui_dialogCoding):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        flags = QtCore.Qt.Tool
        self.setWindowFlags(flags)
        self.code_type = 2
        self.start()

    def start(self):
        self.setupUi(self)
        self.radioGap1.clicked.connect(self.on_gap1_clicked)
        self.radioGap2.clicked.connect(self.on_gap2_clicked)
        self.radioGap3.clicked.connect(self.on_gap3_clicked)
        self.radioCoding1.clicked.connect(self.on_convenient_clicked)
        self.radioCoding2.clicked.connect(self.on_default_clicked)
        self.radioCoding3.clicked.connect(self.on_custom_clicked)
        self.buttonCodingOK.clicked.connect(self.on_closed)
        self.editCode.installEventFilter(self)

        path = Params.path
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(
                       path + '\gui\solitonIcon.png')),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.update_image()

    def update_image(self):
        if Params.gap == 1:
            self.label1Gap1.setVisible(True)
            self.label2Gap1.setVisible(True)
            self.label3Gap1.setVisible(True)

            self.label1Gap2.setVisible(False)
            self.label2Gap2.setVisible(False)
            self.label3Gap2.setVisible(False)
            self.label4Gap2.setVisible(False)
            self.label5Gap2.setVisible(False)

            self.label1Gap3.setVisible(False)
            self.label2Gap3.setVisible(False)
            self.label3Gap3.setVisible(False)
            self.label4Gap3.setVisible(False)
            self.label5Gap3.setVisible(False)
            self.label6Gap3.setVisible(False)
            self.label7Gap3.setVisible(False)

            self.label1Gap1.setText(str(Params.alphabet[0]))
            self.label2Gap1.setText(str(Params.alphabet[1]))
            self.label3Gap1.setText(str(Params.alphabet[2]))
            self.imageComponents.setPixmap(QtGui.QPixmap(
                QtCore.QString.fromUtf8(
                    Params.path + '\gui\components1.png')))

        if Params.gap == 2:
            self.label1Gap1.setVisible(False)
            self.label2Gap1.setVisible(False)
            self.label3Gap1.setVisible(False)

            self.label1Gap2.setVisible(True)
            self.label2Gap2.setVisible(True)
            self.label3Gap2.setVisible(True)
            self.label4Gap2.setVisible(True)
            self.label5Gap2.setVisible(True)

            self.label1Gap3.setVisible(False)
            self.label2Gap3.setVisible(False)
            self.label3Gap3.setVisible(False)
            self.label4Gap3.setVisible(False)
            self.label5Gap3.setVisible(False)
            self.label6Gap3.setVisible(False)
            self.label7Gap3.setVisible(False)

            self.label1Gap2.setText(str(Params.alphabet[0]))
            self.label2Gap2.setText(str(Params.alphabet[1]))
            self.label3Gap2.setText(str(Params.alphabet[2]))
            self.label4Gap2.setText(str(Params.alphabet[3]))
            self.label5Gap2.setText(str(Params.alphabet[4]))
            self.imageComponents.setPixmap(QtGui.QPixmap(
                QtCore.QString.fromUtf8(
                    Params.path + '\gui\components2.png')))

        if Params.gap == 3:
            self.label1Gap1.setVisible(False)
            self.label2Gap1.setVisible(False)
            self.label3Gap1.setVisible(False)

            self.label1Gap2.setVisible(False)
            self.label2Gap2.setVisible(False)
            self.label3Gap2.setVisible(False)
            self.label4Gap2.setVisible(False)
            self.label5Gap2.setVisible(False)

            self.label1Gap3.setVisible(True)
            self.label2Gap3.setVisible(True)
            self.label3Gap3.setVisible(True)
            self.label4Gap3.setVisible(True)
            self.label5Gap3.setVisible(True)
            self.label6Gap3.setVisible(True)
            self.label7Gap3.setVisible(True)

            self.label1Gap3.setText(str(Params.alphabet[0]))
            self.label2Gap3.setText(str(Params.alphabet[1]))
            self.label3Gap3.setText(str(Params.alphabet[2]))
            self.label4Gap3.setText(str(Params.alphabet[3]))
            self.label5Gap3.setText(str(Params.alphabet[4]))
            self.label6Gap3.setText(str(Params.alphabet[5]))
            self.label7Gap3.setText(str(Params.alphabet[6]))
            self.imageComponents.setPixmap(QtGui.QPixmap(
                QtCore.QString.fromUtf8(
                    Params.path + '\gui\components3.png')))

    def update_alphabet(self):
        Params.alphabet = str(self.editCode.text()).split(', ')

    def on_opened(self):
        self.show()
        self.activateWindow()
        self.setFocus()
        self.editCode.setText(', '.join(Params.alphabet))
        self.update_image()

    def on_closed(self):
        self.update_alphabet()
        self.close()

    def on_gap1_clicked(self):
        if Params.gap == 1:
            return
        if self.code_type == 1:
            Params.alphabet = ['-', '0', '+']
        else:
            Params.alphabet = ['-1', '0', '+1']
        Params.gap = 1
        Params.mu = 1.0
        Params.v0 = 3.0
        Params.periods = 10
        self.editCode.setText(', '.join(Params.alphabet))
        self.update_alphabet()
        self.update_image()

    def on_gap2_clicked(self):
        if Params.gap == 2:
            return
        if self.code_type == 1:
            Params.alphabet = ['-', '^', '0', 'v', '+']
        else:
            Params.alphabet = ['-2', '-1', '0', '+1', '+2']
        Params.gap = 2
        Params.mu = 4.0
        Params.v0 = 10.0
        Params.periods = 20
        self.editCode.setText(', '.join(Params.alphabet))
        self.update_alphabet()
        self.update_image()

    def on_gap3_clicked(self):
        if Params.gap == 3:
            return
        if self.code_type == 1:
            Params.alphabet = ['-', '^', '>', '0', '<', 'v', '+']
        else:
            Params.alphabet = ['-3', '-2', '-1', '0', '+1', '+2', '+3']
        Params.gap = 3
        Params.mu = 10.0
        Params.v0 = 20.0
        Params.periods = 20
        self.editCode.setText(', '.join(Params.alphabet))
        self.update_alphabet()
        self.update_image()

    def on_convenient_clicked(self):
        if Params.gap == 1:
            Params.alphabet = ['-', '0', '+']
        elif Params.gap == 2:
            Params.alphabet = ['-', '^', '0', 'v', '+']
        elif Params.gap == 3:
            Params.alphabet = ['-', '^', '>', '0', '<', 'v', '+']
        self.code_type = 1
        self.editCode.setEnabled(False)
        self.editCode.setText(', '.join(Params.alphabet))
        self.update_alphabet()
        self.update_image()

    def on_default_clicked(self):
        if Params.gap == 1:
            Params.alphabet = ['-1', '0', '+1']
        elif Params.gap == 2:
            Params.alphabet = ['-2', '-1', '0', '+1', '+2']
        elif Params.gap == 3:
            Params.alphabet = ['-3', '-2', '-1', '0', '+1', '+2', '+3']
        self.code_type = 2
        self.editCode.setEnabled(False)
        self.editCode.setText(', '.join(Params.alphabet))
        self.update_alphabet()
        self.update_image()

    def on_custom_clicked(self):
        self.code_type = 3
        self.editCode.setEnabled(True)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyRelease:
            self.update_alphabet()
            self.update_image()
        return QtGui.QWidget.eventFilter(self, obj, event)