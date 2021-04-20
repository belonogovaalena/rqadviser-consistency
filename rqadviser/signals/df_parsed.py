from PyQt5.QtCore import pyqtSignal, QObject


class DataFrameParsed(QObject):
    signal = pyqtSignal()
