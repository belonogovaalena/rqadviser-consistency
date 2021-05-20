"""
Интерфейс для полной проверки
"""
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, \
    QRadioButton, QWidget

from rqadviser.signals.signals import FullModeChosen, SingleModeChosen


class CheckView(QMainWindow):
    """
    Интерфейс для полной проверки
    """
    def __init__(self, main):
        # pylint: disable=bad-super-call
        super(QMainWindow, self).__init__()
        self._main = main

        self._full_mode_chosen = FullModeChosen()
        self._full_mode_chosen.signal.connect(self._main.full_mode_chosen_slot)

        self._single_mode_chosen = SingleModeChosen()
        self._single_mode_chosen.signal.connect(self._main.single_mode_chosen_slot)

        self._buttons_clustering = QButtonGroup()
        self._buttons_nlp = QButtonGroup()
        self._line_dimension = QLineEdit()
        self._line_dimension.setPlaceholderText("Допустимое расстояние между требованиями")
        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self._line_dimension)
        self._line_dimension.setValidator(input_validator)

        self._init_ui()

    def _init_ui(self):
        """
        Инициализация интерфейса
        """
        self.setWindowTitle("Выбор метода проверки")
        self.setFixedSize(451, 271)
        frame = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        frame.moveCenter(QApplication.desktop().screenGeometry(screen).center())
        self.move(frame.topLeft())
        self._create_grid()

    def _create_grid(self):
        """
        Создание переключателей на интерфейсе
        """
        # pylint: disable=too-many-locals
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
        self._buttons_nlp.addButton(simple_nlp_but, 0)
        grid_layout.addWidget(simple_nlp_but, 1, 0)

        tfidf_nlp_but = QRadioButton("TF-IDF")
        self._buttons_nlp.addButton(tfidf_nlp_but, 1)
        grid_layout.addWidget(tfidf_nlp_but, 2, 0)

        doc2vecdm_nlp_but = QRadioButton("Doc2Vec DM")
        self._buttons_nlp.addButton(doc2vecdm_nlp_but, 2)
        grid_layout.addWidget(doc2vecdm_nlp_but, 3, 0)

        doc2vecdbow_nlp_but = QRadioButton("Doc2Vec DBOW")
        self._buttons_nlp.addButton(doc2vecdbow_nlp_but, 3)
        grid_layout.addWidget(doc2vecdbow_nlp_but, 4, 0)

        bert_nlp_but = QRadioButton("BERT")
        self._buttons_nlp.addButton(bert_nlp_but, 4)
        grid_layout.addWidget(bert_nlp_but, 5, 0)

        kmeans_cluster_but = QRadioButton("K-Means++")
        self._buttons_clustering.addButton(kmeans_cluster_but, 0)
        grid_layout.addWidget(kmeans_cluster_but, 1, 1)

        em_cluster_but = QRadioButton("EM-algorithm")
        self._buttons_clustering.addButton(em_cluster_but, 1)
        grid_layout.addWidget(em_cluster_but, 2, 1)

        aglo_av_cluster_but = QRadioButton("Aglomerative Average")
        self._buttons_clustering.addButton(aglo_av_cluster_but, 2)
        grid_layout.addWidget(aglo_av_cluster_but, 3, 1)

        aglo_max_cluster_but = QRadioButton("Aglomerative Ward")
        self._buttons_clustering.addButton(aglo_max_cluster_but, 3)
        grid_layout.addWidget(aglo_max_cluster_but, 4, 1)

        aglo_min_cluster_but = QRadioButton("Aglomerative Сomplete")
        self._buttons_clustering.addButton(aglo_min_cluster_but, 4)
        grid_layout.addWidget(aglo_min_cluster_but, 5, 1)

        aglo_single_cluster_but = QRadioButton("Aglomerative Single")
        self._buttons_clustering.addButton(aglo_single_cluster_but, 5)
        grid_layout.addWidget(aglo_single_cluster_but, 6, 1)

        dbscan_cluster_but = QRadioButton("DBSCAN")
        self._buttons_clustering.addButton(dbscan_cluster_but, 6)
        grid_layout.addWidget(dbscan_cluster_but, 7, 1)

        grid_layout.addWidget(self._line_dimension, 7, 0, 1, 0)

        ok_but = QPushButton("OK")
        ok_but.clicked.connect(self.on_button_ok_clicked)
        grid_layout.addWidget(ok_but, 8, 0, 1, 0)

    def on_button_ok_clicked(self):
        """
        Слот при выборе конкретного режима проверки
        """
        if self._line_dimension.isEnabled():
            self._full_mode_chosen.signal.emit(self._buttons_clustering.checkedId(), self._buttons_nlp.checkedId(),
                                               float(self._line_dimension.text()))
        else:
            self._single_mode_chosen.signal.emit(self._buttons_clustering.checkedId(), self._buttons_nlp.checkedId())
        self.hide()

    def enable_single(self):
        """
        Установка режима частичной проверки
        """
        self._line_dimension.setEnabled(False)

    def enable_full(self):
        """
        Установка режима полной проверки
        """
        self._line_dimension.setEnabled(True)
