from PyQt5.QtCore import pyqtSignal, QObject


class InaccuraciesFound(QObject):
    signal = pyqtSignal()
