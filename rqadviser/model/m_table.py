from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class TableModel(QtGui.QStandardItemModel):
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        for col in data.columns:
            data_col = [QtGui.QStandardItem("{}".format(x)) for x in data[col].values]
            self.appendColumn(data_col)
        return

    def rowCount(self, parent=None):  # noqa: N802
        return len(self._data.values)

    def columnCount(self, parent=None):  # noqa: N802
        return self._data.columns.size

    def headerData(self, x, orientation, role):  # noqa: N802
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[x]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[x]
        return None
