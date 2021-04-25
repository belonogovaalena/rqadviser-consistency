from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidget, QTableView
from rqadviser.view.menu_view import MenuViewHelper
from rqadviser.model.model_main import ModelMain
from rqadviser.signals.file_chosen import FileChosen
from rqadviser.view.table_view import TableView


class MainView(QMainWindow):
    __model: ModelMain

    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.__controller = controller
        self.__model = model
        self.__init_ui()

        self.__signal_file_chosen = FileChosen()
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
        self.__signal_file_chosen.signal.connect(self.__controller.file_chosen_slot)

    def new_project_slot(self):
        self.hide()
        # TODO проверку, что файл выбран
        dialog = QFileDialog()
        file_name, _ = dialog.getOpenFileNames(self, 'Выберите файл .csv:', filter="CSV Files (*.csv)")
        self.show()
        self.__signal_file_chosen.signal.emit(file_name[0])

    def df_changed_slot(self):
        df = self.__model.data_frame.df
        table_view = TableView(self, df)
        table_view.create_table()

    def download_project_slot(self):
        print("TBD: Загрузка проекта")

    def save_project_slot(self):
        print("TBD: Сохранение проекта")
