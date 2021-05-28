"""
Интерфейс таблицы с результатами анализа
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QAbstractScrollArea, QGridLayout, QLabel, QMainWindow, QTableView, \
    QWidget

from rqadviser.model.m_table import TableModel


class ViewResult(QMainWindow):
    """
    Интерфейс таблицы с результатами анализа
    """
    def __init__(self, df, message="", parent=None):
        # pylint: disable=bad-super-call
        super(QMainWindow, self).__init__(parent)
        self._df = df
        self._message = message
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
        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel(self._message), 0, 0)
        grid_layout.addWidget(table, 1, 0)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_layout)
