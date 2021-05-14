from PyQt5.QtCore import pyqtSignal, QObject


class CheckSingleRequirement(QObject):
    signal = pyqtSignal(int, int, str)
