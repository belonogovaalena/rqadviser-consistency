from PyQt5.QtCore import pyqtSignal, QObject


class ClusterFound(QObject):
    signal = pyqtSignal()
