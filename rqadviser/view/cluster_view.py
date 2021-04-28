from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QWidget, QGridLayout, QAbstractScrollArea, QAbstractItemView, QPushButton, \
    QMainWindow

from rqadviser.model.model_table import TableModel


class ClusterView(QMainWindow):
    def __init__(self, df, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.__df = df

        self.__grid_layout = QGridLayout()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.__grid_layout)
        self.__create_table()

    def __create_table(self):
        model = TableModel(self.__df)
        table = QTableView()
        table.setModel(model)
        header = table.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__grid_layout.addWidget(table, 0, 0)
