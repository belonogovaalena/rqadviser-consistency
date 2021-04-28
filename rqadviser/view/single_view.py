from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QLabel, QButtonGroup, QRadioButton, \
    QPushButton
from rqadviser.signals.single_mode_chosen import SingleModeChosen


class SingleCheckView(QMainWindow):

    def __init__(self, main, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.__main = main

        self.__single_mode_chosen = SingleModeChosen()
        self.__single_mode_chosen.signal.connect(self.__main.single_mode_chosen_slot)

        self.__buttons_clustering = QButtonGroup()
        self.__buttons_nlp = QButtonGroup()

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("Выбор метода проверки")
        self.__setup_geometry()
        self.__create_grid()

    def __setup_geometry(self):
        self.setFixedSize(461, 269)
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

        aglo_max_cluster_but = QRadioButton("Aglomerative Ward")
        self.__buttons_clustering.addButton(aglo_max_cluster_but, 3)
        grid_layout.addWidget(aglo_max_cluster_but, 4, 1)

        aglo_min_cluster_but = QRadioButton("Aglomerative Сomplete")
        self.__buttons_clustering.addButton(aglo_min_cluster_but, 4)
        grid_layout.addWidget(aglo_min_cluster_but, 5, 1)

        aglo_single_cluster_but = QRadioButton("Aglomerative Single")
        self.__buttons_clustering.addButton(aglo_single_cluster_but, 5)
        grid_layout.addWidget(aglo_single_cluster_but, 6, 1)

        dbscan_cluster_but = QRadioButton("DBSCAN")
        self.__buttons_clustering.addButton(dbscan_cluster_but, 6)
        grid_layout.addWidget(dbscan_cluster_but, 7, 1)

        ok_but = QPushButton("OK")
        ok_but.clicked.connect(self.on_button_ok_clicked)
        grid_layout.addWidget(ok_but, 8, 0, 1, 0)

    def on_button_ok_clicked(self):
        self.__single_mode_chosen.signal.emit(self.__buttons_clustering.checkedId(), self.__buttons_nlp.checkedId())
        self.hide()
