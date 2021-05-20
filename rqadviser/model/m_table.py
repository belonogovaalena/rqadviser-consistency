"""
Модель таблицы для интерфейса
"""
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class TableModel(QtGui.QStandardItemModel):
    """
    Модель таблицы для интерфейса
    """
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        for col in data.columns:
            data_col = [QtGui.QStandardItem("{}".format(x)) for x in data[col].values]
            self.appendColumn(data_col)

    # pylint: disable=invalid-name, unused-argument
    def rowCount(self, parent=None):  # noqa: N802
        """
        Имплементация метода количества строк
        """
        return len(self._data.values)

    # pylint: disable=invalid-name, unused-argument
    def columnCount(self, parent=None):  # noqa: N802
        """
        Имплементация метода количества ста
        """
        return self._data.columns.size

    # pylint: disable=invalid-name
    def headerData(self, x, orientation, role):  # noqa: N802
        """
        Имплементация создания заголовка таблицы
        """
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[x]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[x]
        return None
