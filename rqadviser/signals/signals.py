from PyQt5.QtCore import QObject, pyqtSignal


class CheckFullRequirements(QObject):
    signal = pyqtSignal(int, int, float)


class CheckSingleRequirement(QObject):
    signal = pyqtSignal(int, int, str)


class ClusterFound(QObject):
    signal = pyqtSignal()


class DataFrameParsed(QObject):
    signal = pyqtSignal()


class DownloadProject(QObject):
    signal = pyqtSignal(str)


class FileChosen(QObject):
    signal = pyqtSignal(str)


class FullModeChosen(QObject):
    signal = pyqtSignal(int, int, float)


class InaccuraciesFound(QObject):
    signal = pyqtSignal()


class SaveProject(QObject):
    signal = pyqtSignal()


class SavedProject(QObject):
    signal = pyqtSignal()


class SingleModeChosen(QObject):
    signal = pyqtSignal(int, int)
