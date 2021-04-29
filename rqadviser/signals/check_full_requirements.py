from PyQt5.QtCore import pyqtSignal, QObject


class CheckFullRequirements(QObject):
    signal = pyqtSignal(int, int, float)
