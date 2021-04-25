from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QLabel, QButtonGroup, QRadioButton


class SingleView(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.__init_ui()
        self.buttons_clustering = None
        self.buttons_nlp = None

    def __init_ui(self):
        self.setWindowTitle("Выбор метода проверки")
        self.__setup_geometry()
        self.__create_grid()

    def __setup_geometry(self):
        self.setFixedSize(347, 169)
        frame = self.frameGeometry()
        desktop = QApplication.desktop()
        screen = desktop.screenNumber(desktop.cursor().pos())
        frame.moveCenter(desktop.screenGeometry(screen).center())
        self.move(frame.topLeft())

    def __create_grid(self):
        self.buttons_nlp = QButtonGroup(self)
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
        self.buttons_nlp.addButton(simple_nlp_but)
        grid_layout.addWidget(simple_nlp_but, 1, 0)

        tfidf_nlp_but = QRadioButton("TF-IDF")
        self.buttons_nlp.addButton(tfidf_nlp_but)
        grid_layout.addWidget(tfidf_nlp_but, 2, 0)

        word2vec_nlp_but = QRadioButton("Word2Vec")
        self.buttons_nlp.addButton(word2vec_nlp_but)
        grid_layout.addWidget(word2vec_nlp_but, 3, 0)

        bert_nlp_but = QRadioButton("BERT")
        self.buttons_nlp.addButton(bert_nlp_but)
        grid_layout.addWidget(bert_nlp_but, 4, 0)

        self.buttons_clustering = QButtonGroup(self)
        kmeans_cluster_but = QRadioButton("K-Means++")
        self.buttons_clustering.addButton(kmeans_cluster_but)
        grid_layout.addWidget(kmeans_cluster_but, 1, 1)

        em_cluster_but = QRadioButton("EM-algorithm")
        self.buttons_clustering.addButton(em_cluster_but)
        grid_layout.addWidget(em_cluster_but, 2, 1)

        aglo_av_cluster_but = QRadioButton("Aglomerative Average")
        self.buttons_clustering.addButton(aglo_av_cluster_but)
        grid_layout.addWidget(aglo_av_cluster_but, 3, 1)

        aglo_max_cluster_but = QRadioButton("Aglomerative Max")
        self.buttons_clustering.addButton(aglo_max_cluster_but)
        grid_layout.addWidget(aglo_max_cluster_but, 4, 1)

        aglo_min_cluster_but = QRadioButton("Aglomerative Min")
        self.buttons_clustering.addButton(aglo_min_cluster_but)
        grid_layout.addWidget(aglo_min_cluster_but, 5, 1)

        dbscan_cluster_but = QRadioButton("DBSCAN")
        self.buttons_clustering.addButton(dbscan_cluster_but)
        grid_layout.addWidget(dbscan_cluster_but, 6, 1)
