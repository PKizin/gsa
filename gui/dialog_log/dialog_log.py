import os
import sys
import time
from emitting_stream import EmittingStream
from domain.gslib import GSParams as Params

from PyQt4 import QtCore, QtGui
from ui_dialog_log import Ui_dialogLog


class DialogLog(QtGui.QDialog, Ui_dialogLog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        flags = QtCore.Qt.Tool
        self.setWindowFlags(flags)
        self.stream = EmittingStream()
        self.start()

    def start(self):
        self.setupUi(self)
        self.progressBarStatus.setValue(0)
        self.reset_progress_bar()
        self.stream.textWritten.connect(self.on_write_to_console)
        self.stream.textWritten.connect(self.on_progress_bar_updated)
        sys.stdout = self.stream

        path = Params.path
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(QtCore.QString.fromUtf8(
                       path + '\gui\solitonIcon.png')),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def on_opened(self):
        self.show()
        self.activateWindow()
        self.setFocus()

    def on_closed(self):
        self.close()

    def reset_progress_bar(self):
        self.labelStatus.setText('Status unknown')
        self.progressBarStatus.setValue(0)

    solitonAssembled = QtCore.pyqtSignal()

    def on_write_to_console(self, text):
        self.editLog.moveCursor(QtGui.QTextCursor.End)
        msg_list = str(text).split('\n')
        msg = ''
        if msg_list[0] == '<info>':
            msg = msg_list[1] + '<br><br>'

        elif msg_list[0] == '<success>':
            msg = '<font color=green><b>' + msg_list[1] + '</b></font><br><br>'

        elif msg_list[0] == '<fail>':
            msg = '<font color=red><b>' + msg_list[1] + '</b></font><br><br>'

        elif msg_list[0] == '<strip>':
            msg = msg_list[1]

            l = msg_list[2].split('.')
            r = msg_list[3].split('.')
            n = 0
            while l[1][n] == r[1][n]:
                n += 1
                if n >= min(len(l[1]), len(r[1])):
                    break

            if float('.'.join(l)) * float('.'.join(r)) > 0:
                l = l[0] + '.<b>' + l[1][0:n] + '</b>' + l[1][n:]
                r = r[0] + '.<b>' + r[1][0:n] + '</b>' + r[1][n:]
            else:
                l = l[0] + '.' + l[1]
                r = r[0] + '.' + r[1]

            msg += '<table>' \
                   '<tr>' \
                   '<td>&nbsp;&nbsp;&nbsp;&nbsp;l</td>' \
                   '<td>=</td>' \
                   '<td>' + l + '</td>' \
                   '</tr>' \
                   '<tr>' \
                   '<td>&nbsp;&nbsp;&nbsp;&nbsp;r</td>' \
                   '<td>=</td>' \
                   '<td>' + r + '</td>' \
                   '</tr>' \
                   '</table><br><br>'

        elif msg_list[0] == '<asympt>':
            l = msg_list[1].split('.')
            r = msg_list[2].split('.')
            h = msg_list[3]
            n = 0
            while l[1][n] == r[1][n]:
                n += 1
                if n >= min(len(l[1]), len(r[1])):
                    break

            l = l[0] + '.<b>' + l[1][0:n] + '</b>' + l[1][n:]
            r = r[0] + '.<b>' + r[1][0:n] + '</b>' + r[1][n:]

            msg = '<table>' \
                  '<tr>' \
                  '<td>&nbsp;&nbsp;&nbsp;&nbsp;l</td>' \
                  '<td>=</td>' \
                  '<td>' + l + '</td>' \
                  '</tr>' \
                  '<tr>' \
                  '<td>&nbsp;&nbsp;&nbsp;&nbsp;r</td>' \
                  '<td>=</td>' \
                  '<td>' + r + '</td>' \
                  '</tr>' \
                  '<tr>' \
                  '<td>&nbsp;&nbsp;&nbsp;&nbsp;d</td>' \
                  '<td>=</td>' \
                  '<td>' + h + '</td>' \
                  '</tr>' \
                  '</table><br><br>'

        self.editLog.insertHtml(msg)
        self.editLog.setFocus()
        self.editLog.repaint()

        if msg_list[0] == '<success>':
            time.sleep(1)
            self.solitonAssembled.emit()

    def on_progress_bar_updated(self):
        self.labelStatus.setText(Params.status)
        self.progressBarStatus.setValue(round(Params.progress))
        self.progressBarStatus.setFocus()
        self.progressBarStatus.repaint()
