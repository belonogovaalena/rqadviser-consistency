from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication

from rqadviser.view.menu_view import MenuViewHelper


class MainView(QMainWindow):
    def __init__(self, controller, model, parent=None):
        super(QWidget, self).__init__(parent)
        self.__controller = controller
        self.__model = model
        self.__init_ui()

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

    def new_project_slot(self):
        print("TBD: Создание нового проекта")

    def download_project_slot(self):
        print("TBD: Загрузка проекта")

    def save_project_slot(self):
        print("TBD: Сохранение проекта")
