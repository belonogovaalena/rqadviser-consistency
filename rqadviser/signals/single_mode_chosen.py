from PyQt5.QtCore import pyqtSignal, QObject


class SingleModeChosen(QObject):
    signal = pyqtSignal(int, int)
