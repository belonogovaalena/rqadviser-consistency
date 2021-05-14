from PyQt5.QtCore import pyqtSignal, QObject


class DownloadProject(QObject):
    signal = pyqtSignal(str)
