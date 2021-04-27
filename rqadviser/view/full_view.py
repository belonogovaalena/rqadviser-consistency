from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QLabel, QButtonGroup, QRadioButton, \
    QPushButton, QLineEdit
from rqadviser.signals.full_mode_chosen import FullModeChosen


class FullCheckView(QMainWindow):

    def __init__(self, main, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.__main = main

        self.__full_mode_chosen = FullModeChosen()
        self.__full_mode_chosen.signal.connect(self.__main.full_mode_chosen_slot)

        self.__buttons_clustering = QButtonGroup()
        self.__buttons_nlp = QButtonGroup()
        self.__line_dimension = QLineEdit()
        self.__line_dimension.setPlaceholderText("Максимально допустимое расстояние между требованиями")
        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self.__line_dimension)
        self.__line_dimension.setValidator(input_validator)
        self.__line_dimension.setAccessibleDescription("asa")

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("Выбор метода проверки")
        self.__setup_geometry()
        self.__create_grid()

    def __setup_geometry(self):
        frame = self.frameGeometry()
        desktop = QApplication.desktop()
        screen = desktop.screenNumber(desktop.cursor().pos())
        frame.moveCenter(desktop.screenGeometry(screen).center())
        self.move(frame.topLeft())

    def __create_grid(self):
        grid_layout = QGridLayout()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_layout)
        label_clus = QLabel("Выбор алгоритма кластеризации")
        label_clus.setStyleSheet("font-weight: bold")
        grid_layout.addWidget(label_clus, 0, 0)
        label_nlp = QLabel("Выбор алгоритма NLP")
        label_nlp.setStyleSheet("font-weight: bold")
        grid_layout.addWidget(label_nlp, 0, 1)

        simple_nlp_but = QRadioButton("Simple cosine method")
        self.__buttons_nlp.addButton(simple_nlp_but, 0)
        grid_layout.addWidget(simple_nlp_but, 1, 0)

        tfidf_nlp_but = QRadioButton("TF-IDF")
        self.__buttons_nlp.addButton(tfidf_nlp_but, 1)
        grid_layout.addWidget(tfidf_nlp_but, 2, 0)

        word2vec_nlp_but = QRadioButton("Word2Vec")
        self.__buttons_nlp.addButton(word2vec_nlp_but, 2)
        grid_layout.addWidget(word2vec_nlp_but, 3, 0)

        bert_nlp_but = QRadioButton("BERT")
        self.__buttons_nlp.addButton(bert_nlp_but, 3)
        grid_layout.addWidget(bert_nlp_but, 4, 0)

        kmeans_cluster_but = QRadioButton("K-Means++")
        self.__buttons_clustering.addButton(kmeans_cluster_but, 0)
        grid_layout.addWidget(kmeans_cluster_but, 1, 1)

        em_cluster_but = QRadioButton("EM-algorithm")
        self.__buttons_clustering.addButton(em_cluster_but, 1)
        grid_layout.addWidget(em_cluster_but, 2, 1)

        aglo_av_cluster_but = QRadioButton("Aglomerative Average")
        self.__buttons_clustering.addButton(aglo_av_cluster_but, 2)
        grid_layout.addWidget(aglo_av_cluster_but, 3, 1)

        aglo_max_cluster_but = QRadioButton("Aglomerative Max")
        self.__buttons_clustering.addButton(aglo_max_cluster_but, 3)
        grid_layout.addWidget(aglo_max_cluster_but, 4, 1)

        aglo_min_cluster_but = QRadioButton("Aglomerative Min")
        self.__buttons_clustering.addButton(aglo_min_cluster_but, 4)
        grid_layout.addWidget(aglo_min_cluster_but, 5, 1)

        dbscan_cluster_but = QRadioButton("DBSCAN")
        self.__buttons_clustering.addButton(dbscan_cluster_but, 5)
        grid_layout.addWidget(dbscan_cluster_but, 6, 1)

        grid_layout.addWidget(self.__line_dimension, 7, 0, 1, 0)

        ok_but = QPushButton("OK")
        ok_but.clicked.connect(self.on_button_ok_clicked)
        grid_layout.addWidget(ok_but, 8, 0, 1, 0)

    def on_button_ok_clicked(self):
        self.__full_mode_chosen.signal.emit(self.__buttons_clustering.checkedId(), self.__buttons_nlp.checkedId(),
                                            float(self.__line_dimension.text()))
        self.hide()
