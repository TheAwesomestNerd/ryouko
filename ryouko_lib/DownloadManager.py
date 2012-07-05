#! /usr/bin/env/ python

import os.path, sys
from PyQt4 import QtCore, QtGui
try:
    __file__
except:
    __file__ = sys.executable
app_lib = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(app_lib)
from Python23Compat import *

class DownloadProgressBar(QtGui.QProgressBar):
    def __init__(self, reply=None, parent=None):
        super(DownloadProgressBar, self).__init__()
        self.reply = reply
        if self.reply:
            self.reply.downloadProgress.connect(self.updateProgress)
    def updateProgress(self, received, total):
        self.setMaximum(total)
        self.setValue(received)
        self.show()

class DownloadProgressDialog(QtGui.QProgressBar):
    def __init__(self, reply=None, destination=os.path.expanduser("~"), parent=None):
        super(DownloadProgressDialog, self).__init__()
        self.reply = reply
        self.destination = destination
        if self.reply:
            self.reply.downloadProgress.connect(self.updateProgress)
            self.reply.finished.connect(self.finishDownload)
        self.setWindowTitle(os.path.split(unicode(destination))[1])
    def finishDownload(self):
        if self.reply.isFinished():
            data = self.reply.readAll()
            f = QtCore.QFile(self.destination)
            f.open(QtCore.QIODevice.WriteOnly)
            f.writeData(data)
            f.flush()
            f.close()
            self.hide()
    def updateProgress(self, received, total):
        self.setMaximum(total)
        self.setValue(received)
        self.show()

class DownloadManagerGUI(QtGui.QMainWindow):
    downloadFinished = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(DownloadManagerGUI, self).__init__()
        self.downloads = []
    def newReply(self, reply, destination = os.path.expanduser("~")):
        i = DownloadProgressDialog(reply, destination)
        self.downloads.append(i)
        reply.finished.connect(self.checkForFinishedDownloads)
    def checkForFinishedDownloads(self):
        for i in range(len(self.downloads)):
            if self.downloads[i].reply.isFinished():
                self.downloads[i].deleteLater()
                del self.downloads[i]
                self.downloadFinished.emit()
                break
