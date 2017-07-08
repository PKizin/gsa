from domain.gslib import GSParams as Params
from PyQt4 import QtCore, QtGui


class CodeValidator(QtGui.QValidator):
    def __init__(self, parent=None):
        QtGui.QValidator.__init__(self, parent)

    def validate(self, text, pos):
        for ch in text:
            if ch not in Params.alphabet:
                return QtGui.QValidator.Invalid, pos
        return QtGui.QValidator.Acceptable, pos
