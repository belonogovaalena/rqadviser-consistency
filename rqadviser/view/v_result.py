from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QAbstractScrollArea, QMainWindow, QTableView

from rqadviser.model.m_table import TableModel


class ViewResult(QMainWindow):
    def __init__(self, df, parent=None):
        super(QMainWindow, self).__init__(parent)
        self._df = df
        self._create_table()

    def _create_table(self):
        model = TableModel(self._df)
        table = QTableView()
        table.setModel(model)
        header = table.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        table.resizeColumnsToContents()
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setCentralWidget(table)
