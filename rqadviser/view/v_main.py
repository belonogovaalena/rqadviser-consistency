"""
Мастер-интерфейс
"""
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from rqadviser.signals.signals import CheckFullRequirements, CheckSingleRequirement, DownloadProject, FileChosen, \
    SaveProject
from rqadviser.view.v_check import CheckView
from rqadviser.view.v_menu import ViewMenu
from rqadviser.view.v_result import ViewResult
from rqadviser.view.v_table import ViewTable


class MainView(QMainWindow):
    """
    Мастер-интерфейс
    """
    def __init__(self, controller, model):
        # pylint: disable=bad-super-call
        super(QMainWindow, self).__init__()
        self._controller = controller
        self._model = model

        self.signals = {"file_chosen": FileChosen(), "check_single_requirement": CheckSingleRequirement(),
                        "check_full_requirements": CheckFullRequirements(), "save_project": SaveProject(),
                        "download_project": DownloadProject()}

        self._init_ui()

        self._full_check_view = CheckView(self)
        self._table_view = None

        self._connect()

    def _init_ui(self):
        """
        Инициализация интерфейса
        """
        self.setWindowTitle("Проверка требований на противоречивость")
        self._setup_geometry()
        self._create_menu()

    def _setup_geometry(self):
        """
        Настраивает размеры и положение окна интерфейса
        """
        self.resize(500, 400)
        frame = self.frameGeometry()
        desktop = QApplication.desktop()
        screen = desktop.screenNumber(desktop.cursor().pos())
        frame.moveCenter(desktop.screenGeometry(screen).center())
        self.move(frame.topLeft())

    def _create_menu(self):
        """
        Создание меню
        """
        menu_helper = ViewMenu(self)
        menu_helper.create_menu()
        self.menuBar().addMenu(menu_helper.project_menu)

    def _connect(self):
        """
        Соединение сигналов со слотами
        """
        self.signals["file_chosen"].signal.connect(self._controller.req_file_chosen_slot)
        self.signals["check_single_requirement"].signal.connect(self._controller.check_single_requirement_slot)
        self.signals["check_full_requirements"].signal.connect(self._controller.check_full_requirements_slot)
        self.signals["save_project"].signal.connect(self._controller.save_project_slot)
        self.signals["download_project"].signal.connect(self._controller.download_project_slot)

    def new_project_slot(self):
        """
        Слот для отображения интерфейса для создания нового проекта
        """
        self.hide()
        dialog = QFileDialog()
        file_path, _ = dialog.getOpenFileNames(self, 'Выберите файл .csv:', filter="CSV Files (*.csv)",
                                               options=QFileDialog.DontUseNativeDialog)
        self.show()
        if file_path:
            self.signals["file_chosen"].signal.emit(file_path[0])

    def df_changed_slot(self):
        """
        Слот для отображения обработанной спецификации
        """
        req_df = self._model.data_frame.req_df
        self._table_view = ViewTable(self, req_df)
        self._table_view.create_table()
        self._table_view.create_buttons()

    def single_check_chosen_slot(self):
        """
        Слот для отображения меню выбора режима частичной проверки
        """
        self._full_check_view.enable_single()
        self._full_check_view.show()

    def single_mode_chosen_slot(self, cluster_mode: int, nlp_mode: int):
        """
        Слот при запуске частичной проверки
        :param cluster_mode: Выбранная модель кластеризации
        :param nlp_mode: Выбранная модель преобразования предложений в вектора
        """
        self.signals["check_single_requirement"].signal.emit(cluster_mode, nlp_mode,
                                                             str(self._table_view.get_current()))

    def single_check_complete(self):
        """
        Слот для отображения результатов частичной проверки
        """
        message = "Ниже приведен список ближайших по смыслу требований к заданному:"
        result_view = ViewResult(self._model.result.requirements_cluster, message, self)
        result_view.show()
        result_view.setWindowTitle("Частичная проверка")
        result_view.setFixedSize(result_view.size())

    def full_check_chosen_slot(self):
        """
        Слот для отображения меню выбора режима полной проверки
        """
        self._full_check_view.enable_full()
        self._full_check_view.show()

    def full_mode_chosen_slot(self, cluster_mode, nlp_mode, measure):
        """
        Слот при запуске частичной проверки
        :param measure: Минимально допустимое расстояние между векторами
        :param cluster_mode: Выбранная модель кластеризации
        :param nlp_mode: Выбранная модель преобразования предложений в вектора
        """
        self.signals["check_full_requirements"].signal.emit(cluster_mode, nlp_mode, measure)

    def full_check_complete(self):
        """
        Слот для отображения результатов полной проверки
        """
        message = "Ниже приведен список пар требований, являющихся противоречиями, и расстояние между ними:"
        result_view = ViewResult(self._model.result.inaccuracies, message, self)
        result_view.show()
        result_view.setWindowTitle("Полная проверка")
        result_view.setFixedSize(result_view.size())

    def download_project_slot(self):
        """
        Слот для отображения интерфейса выбора проекта для загрузки
        """
        self.hide()
        dialog = QFileDialog()
        dir_name = dialog.getExistingDirectory(None, 'Выберите директорию проверки',
                                               options=QFileDialog.DontUseNativeDialog)
        self.show()
        if dir_name:
            self.signals["download_project"].signal.emit(dir_name)

    def save_project_slot(self):
        """
        Слот для передачи сигнала о том, что запущено сохранение проекта
        """
        self.signals["save_project"].signal.emit()

    def project_saved(self):
        """
        Слот для отображения окна с результатами сохранения
        """
        msg = QMessageBox(self)
        if self._model.save.save_state:
            msg.setText("Проект сохранен")
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setText("Ошибка сохранения проекта")
            msg.setIcon(QMessageBox.Critical)

        msg.setWindowTitle("Сохранение")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
