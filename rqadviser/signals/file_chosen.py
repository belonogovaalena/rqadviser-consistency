from PyQt5.QtCore import pyqtSignal, QObject


class FileChosen(QObject):
    signal = pyqtSignal(str)
