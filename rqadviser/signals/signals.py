"""
Модуль с сигналами
"""
from PyQt5.QtCore import QObject, pyqtSignal


class CheckFullRequirements(QObject):
    """
    Интерфейс->контроллер, сигнал при выборе полной проверки
    """
    signal = pyqtSignal(int, int, float)


class CheckSingleRequirement(QObject):
    """
    Интерфейс->контроллер, сигнал при выборе частичной проверки
    """
    signal = pyqtSignal(int, int, str)


class ClusterFound(QObject):
    """
    Модель->интерфейс, сигнал при получении результатов частичной проверки для отображения
    """
    signal = pyqtSignal()


class DataFrameParsed(QObject):
    """
    Модель->интерфейс, сигнал при обработке спецификации для отображения
    """
    signal = pyqtSignal()


class DownloadProject(QObject):
    """
    Интерфейс->контроллер, сигнал при выборе проекта для загрузки
    """
    signal = pyqtSignal(str)


class FileChosen(QObject):
    """
    Интерфейс->контроллер, сигнал при выборе спецификации для создания проекта
    """
    signal = pyqtSignal(str)


class FullModeChosen(QObject):
    """
    Интерфейс->интерфейс, сигнал из меню выбора режима полной проверки с результатами выбора
    """
    signal = pyqtSignal(int, int, float)


class InaccuraciesFound(QObject):
    """
    Модель->интерфейс, сигнал при получении результатов полной проверки для отображения
    """
    signal = pyqtSignal()


class SaveProject(QObject):
    """
    Интерфейс->контроллер, сигнал при запуска сохранения проекта
    """
    signal = pyqtSignal()


class SavedProject(QObject):
    """
    Модель->интерфейс, сигнал при получении результатов о попытке сохранения
    """
    signal = pyqtSignal()


class SingleModeChosen(QObject):
    """
    Интерфейс->интерфейс, сигнал из меню выбора режима частичной проверки с результатами выбора
    """
    signal = pyqtSignal(int, int)
