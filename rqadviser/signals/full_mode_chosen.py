from PyQt5.QtCore import pyqtSignal, QObject


class FullModeChosen(QObject):
    signal = pyqtSignal(int, int, float)
