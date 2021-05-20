"""
Интерфейс таблицы с результатами анализа
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QAbstractScrollArea, QMainWindow, QTableView

from rqadviser.model.m_table import TableModel


class ViewResult(QMainWindow):
    """
    Интерфейс таблицы с результатами анализа
    """
    def __init__(self, df, parent=None):
        # pylint: disable=bad-super-call
        super(QMainWindow, self).__init__(parent)
        self._df = df
        self._create_table()

    def _create_table(self):
        """
        Создание таблицы
        """
        model = TableModel(self._df)
        table = QTableView()
        table.setModel(model)
        header = table.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        table.resizeColumnsToContents()
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # pylint: disable=no-member
        table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setCentralWidget(table)
