from PyQt5.QtCore import pyqtSignal, QObject


class SavedProject(QObject):
    signal = pyqtSignal()
