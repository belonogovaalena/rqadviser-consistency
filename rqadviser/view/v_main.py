from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from rqadviser.model.m_main import ModelMain
from rqadviser.signals.signals import CheckFullRequirements, CheckSingleRequirement, DownloadProject, FileChosen, \
    SaveProject
from rqadviser.view.v_full_check import FullCheckView
from rqadviser.view.v_menu import ViewMenu
from rqadviser.view.v_result import ViewResult
from rqadviser.view.v_single_check import ViewSingleCheck
from rqadviser.view.v_table import ViewTable


class MainView(QMainWindow):
    _model: ModelMain

    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)
        self._controller = controller
        self._model = model

        self.s_file_chosen = FileChosen()
        self._s_check_single_requirement = CheckSingleRequirement()
        self._s_check_full_requirements = CheckFullRequirements()
        self._s_save_project = SaveProject()
        self._s_download_project = DownloadProject()

        self._init_ui()

        self._single_check_view = ViewSingleCheck(self)
        self._full_check_view = FullCheckView(self)
        self._table_view = None

        self._connect()

    def _init_ui(self):
        self.setWindowTitle("Проверка требований на противоречивость")
        self._setup_geometry()
        self._create_menu()

    def _setup_geometry(self):
        self.resize(500, 400)
        frame = self.frameGeometry()
        desktop = QApplication.desktop()
        screen = desktop.screenNumber(desktop.cursor().pos())
        frame.moveCenter(desktop.screenGeometry(screen).center())
        self.move(frame.topLeft())

    def _create_menu(self):
        menu_helper = ViewMenu(self)
        menu_helper.create_menu()
        self.menuBar().addMenu(menu_helper.project_menu)

    def _connect(self):
        self.s_file_chosen.signal.connect(self._controller.req_file_chosen_slot)
        self._s_check_single_requirement.signal.connect(self._controller.check_single_requirement_slot)
        self._s_check_full_requirements.signal.connect(self._controller.check_full_requirements_slot)
        self._s_save_project.signal.connect(self._controller.save_project_slot)
        self._s_download_project.signal.connect(self._controller.download_project_slot)

    def new_project_slot(self):
        self.hide()
        dialog = QFileDialog()
        file_path, _ = dialog.getOpenFileNames(self, 'Выберите файл .csv:', filter="CSV Files (*.csv)",
                                               options=QFileDialog.DontUseNativeDialog)
        self.show()
        if file_path:
            self.s_file_chosen.signal.emit(file_path[0])

    def df_changed_slot(self):
        df = self._model.data_frame.req_df
        self._table_view = ViewTable(self, df)
        self._table_view.create_table()
        self._table_view.create_buttons()

    def single_check_chosen_slot(self):
        self._single_check_view.show()

    def single_mode_chosen_slot(self, cluster_mode, nlp_mode):
        self._s_check_single_requirement.signal.emit(cluster_mode, nlp_mode, str(self._table_view.get_current()))

    def single_check_complete(self):
        result_view = ViewResult(self._model.result.requirements_cluster, self)
        result_view.show()
        result_view.setWindowTitle("Частичная проверка")
        result_view.setFixedSize(result_view.size())

    def full_check_chosen_slot(self):
        self._full_check_view.show()

    def full_mode_chosen_slot(self, cluster_mode, nlp_mode, measure):
        self._s_check_full_requirements.signal.emit(cluster_mode, nlp_mode, measure)

    def full_check_complete(self):
        result_view = ViewResult(self._model.result.inaccuracies, self)
        result_view.show()
        result_view.setWindowTitle("Полная проверка")
        result_view.setFixedSize(result_view.size())

    def download_project_slot(self):
        self.hide()
        dialog = QFileDialog()
        dir_name = dialog.getExistingDirectory(None, 'Выберите директорию проверки',
                                               options=QFileDialog.DontUseNativeDialog)
        self.show()
        if dir_name:
            self._s_download_project.signal.emit(dir_name)

    def save_project_slot(self):
        self._s_save_project.signal.emit()

    def project_saved(self):
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
