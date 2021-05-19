from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QAbstractScrollArea, QGridLayout, QPushButton, QTableView, QWidget

from rqadviser.model.m_table import TableModel


class ViewTable:
    def __init__(self, main, df):
        self._main = main
        self._df = df

        self._grid_layout = QGridLayout()
        central_widget = QWidget(self._main)
        self._main.setCentralWidget(central_widget)
        central_widget.setLayout(self._grid_layout)

        self._table = QTableView()

    def create_table(self):
        model = TableModel(self._df)
        self._table.setModel(model)
        header = self._table.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self._table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self._table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self._table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self._table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._table.setSelectionMode(QAbstractItemView.SingleSelection)
        self._grid_layout.addWidget(self._table, 2, 0)

    def create_buttons(self):
        single_check_button = QPushButton("Поиск ближайшего требования")
        full_check_button = QPushButton("Полная проверка требований")
        single_check_button.setEnabled(False)
        self._table.selectionModel().selectionChanged.connect(lambda: single_check_button.setEnabled(True))
        full_check_button.clicked.connect(lambda: single_check_button.setEnabled(True))
        self._grid_layout.addWidget(single_check_button, 0, 0)
        self._grid_layout.addWidget(full_check_button, 1, 0)
        single_check_button.clicked.connect(self._main.single_check_chosen_slot)
        full_check_button.clicked.connect(self._main.full_check_chosen_slot)

    def get_current(self):
        return self._table.model().index(self._table.currentIndex().row(), 0).data()
