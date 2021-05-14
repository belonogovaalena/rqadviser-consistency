from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from rqadviser.view.menu_view import MenuViewHelper
from rqadviser.model.model_main import ModelMain
from rqadviser.signals.file_chosen import FileChosen
from rqadviser.signals.check_single_requirement import CheckSingleRequirement
from rqadviser.signals.check_full_requirements import CheckFullRequirements
from rqadviser.signals.save_project import SaveProject
from rqadviser.view.table_view import TableView
from rqadviser.view.single_view import SingleCheckView
from rqadviser.view.full_view import FullCheckView
from rqadviser.view.result_view import ResultView


class MainView(QMainWindow):
    __model: ModelMain

    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.__controller = controller
        self.__model = model

        self.signal_file_chosen = FileChosen()
        self.__check_single_requirement = CheckSingleRequirement()
        self.__check_full_requirements = CheckFullRequirements()
        self.__save_project = SaveProject()

        self.__init_ui()

        self.__single_check_view = SingleCheckView(self)
        self.__full_check_view = FullCheckView(self)
        self.__table_view = None

        self.__connect()

    def __init_ui(self):
        self.setWindowTitle("Проверка требований на противоречивость")
        self.__setup_geometry()
        self.__create_menu()

    def __setup_geometry(self):
        self.resize(500, 400)
        frame = self.frameGeometry()
        desktop = QApplication.desktop()
        screen = desktop.screenNumber(desktop.cursor().pos())
        frame.moveCenter(desktop.screenGeometry(screen).center())
        self.move(frame.topLeft())

    def __create_menu(self):
        menu_helper = MenuViewHelper(self)
        menu_helper.create_menu()
        self.menuBar().addMenu(menu_helper.project_menu)

    def __connect(self):
        self.signal_file_chosen.signal.connect(self.__controller.file_chosen_slot)
        self.__check_single_requirement.signal.connect(self.__controller.check_single_requirement_slot)
        self.__check_full_requirements.signal.connect(self.__controller.check_full_requirements_slot)
        self.__save_project.signal.connect(self.__controller.save_project_slot)

    def new_project_slot(self):
        self.hide()
        # TODO проверку, что файл выбран
        dialog = QFileDialog()
        file_name, _ = dialog.getOpenFileNames(self, 'Выберите файл .csv:', filter="CSV Files (*.csv)")
        self.show()
        self.signal_file_chosen.signal.emit(file_name[0])

    def df_changed_slot(self):
        df = self.__model.data_frame.df
        self.__table_view = TableView(self, df)
        self.__table_view.create_table()
        self.__table_view.create_buttons()

    def single_check_chosen_slot(self):
        self.__single_check_view.show()

    def single_mode_chosen_slot(self, cluster_mode, nlp_mode):
        self.__check_single_requirement.signal.emit(cluster_mode, nlp_mode, str(self.__table_view.get_current()))

    def single_check_complete(self):
        result_view = ResultView(self.__model.result.requirements_cluster, self)
        result_view.show()

    def full_check_chosen_slot(self):
        self.__full_check_view.show()

    def full_mode_chosen_slot(self, cluster_mode, nlp_mode, measure):
        self.__check_full_requirements.signal.emit(cluster_mode, nlp_mode, measure)

    def full_check_complete(self):
        result_view = ResultView(self.__model.result.inaccuracies, self)
        result_view.show()

    def download_project_slot(self):
        print("TBD: Загрузка проекта")

    def save_project_slot(self):
        self.__save_project.signal.emit()

    def project_saved(self):
        msg = QMessageBox(self)
        if self.__model.save.save_state:
            msg.setText("Проект сохранен")
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setText("Ошибка сохранения проекта")
            msg.setIcon(QMessageBox.Critical)

        msg.setWindowTitle("Сохранениt")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
