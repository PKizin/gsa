from gmpy2 import const_pi as pi
from domain.gslib import GSParams as Params

from PyQt4 import QtCore, QtGui
from ui_dialog_params import Ui_dialogParams


class DialogParams(QtGui.QDialog, Ui_dialogParams):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        flags = QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
        self.setWindowFlags(flags)
        self.start()

    def start(self):
        self.setupUi(self)
        self.buttonParamsOK.clicked.connect(self.on_closed)
        self.spinBox_n.valueChanged.connect(self.on_n_value_changed)
        self.spinBox_m.valueChanged.connect(self.on_m_value_changed)

    def on_opened(self):
        self.spinBoxMu.setValue(Params.mu)
        self.spinBoxV0.setValue(Params.v0)
        self.spinBox_n.setValue(Params.periods)
        self.spinBoxL.setValue(pi() * Params.periods)
        self.spinBox_m.setValue(Params.frequency)
        self.spinBox_h.setValue(pi() / Params.frequency)
        self.spinBoxO.setValue((pi() / Params.frequency) ** 4)
        self.spinBoxPrecision.setValue(Params.bits)
        self.spinBoxM.setValue(Params.left_tail)
        self.spinBoxK.setValue(Params.right_tail)
        self.spinBox_fi.setValue(Params.find_inf_step)
        self.spinBox_fg.setValue(Params.find_gap_step)
        self.spinBox_strip.setValue(Params.initial_strip)

        self.show()
        self.activateWindow()
        self.setFocus()

    def on_closed(self):
        Params.mu = self.spinBoxMu.value()
        Params.v0 = self.spinBoxV0.value()
        Params.periods = self.spinBox_n.value()
        Params.frequency = self.spinBox_m.value()
        Params.bits = self.spinBoxPrecision.value()
        Params.left_tail = self.spinBoxM.value()
        Params.right_tail = self.spinBoxK.value()
        Params.find_inf_step = self.spinBox_fi.value()
        Params.find_inf_step = self.spinBox_fg.value()
        Params.initial_strip = self.spinBox_strip.value()

        self.close()

    def on_n_value_changed(self):
        self.spinBoxL.setValue(pi() * self.spinBox_n.value())

    def on_m_value_changed(self):
        self.spinBox_h.setValue(pi() / self.spinBox_m.value())
        self.spinBoxO.setValue(self.spinBox_h.value() ** 4)