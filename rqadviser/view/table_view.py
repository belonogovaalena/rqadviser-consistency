from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QWidget, QGridLayout, QAbstractScrollArea, QAbstractItemView, QPushButton


class TableModel(QtGui.QStandardItemModel):
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        for col in data.columns:
            data_col = [QtGui.QStandardItem("{}".format(x)) for x in data[col].values]
            self.appendColumn(data_col)
        return

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def headerData(self, x, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[x]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[x]
        return None


class TableView:
    def __init__(self, main, df):
        self.__main = main
        self.__df = df

        self.__grid_layout = QGridLayout()
        central_widget = QWidget(self.__main)
        self.__main.setCentralWidget(central_widget)
        central_widget.setLayout(self.__grid_layout)

        self.__table = QTableView()

    def create_table(self):
        model = TableModel(self.__df)
        self.__table.setModel(model)
        header = self.__table.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.__table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.__table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.__table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.__table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.__table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__grid_layout.addWidget(self.__table, 2, 0)

    def create_buttons(self):
        single_check_button = QPushButton("Поиск ближайшего требования")
        full_check_button = QPushButton("Полная проверка требований")
        single_check_button.setEnabled(False)
        self.__table.selectionModel().selectionChanged.connect(lambda: single_check_button.setEnabled(True))
        self.__grid_layout.addWidget(single_check_button, 0, 0)
        self.__grid_layout.addWidget(full_check_button, 1, 0)
        single_check_button.clicked.connect(self.__main.single_check_chosen_slot)
        full_check_button.clicked.connect(self.__main.full_check_chosen_slot)

    def get_current(self):
        return self.__table.model().index(self.__table.currentIndex().row(), 0).data()
