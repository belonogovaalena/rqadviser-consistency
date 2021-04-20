from PyQt5.QtWidgets import QAction, QMenu


class MenuViewHelper:
    def __init__(self, main):
        self.__project_menu = QMenu()
        self.__main = main

    def create_menu(self):
        new_action = QAction(self.__main)
        new_action.setText("Новый проект")
        new_action.triggered.connect(self.__main.new_project_slot)

        download_action = QAction(self.__main)
        download_action.setText("Загрузить проект")
        download_action.triggered.connect(self.__main.download_project_slot)

        save_action = QAction(self.__main)
        save_action.setText("Сохранить проект")
        save_action.setEnabled(False)
        save_action.triggered.connect(self.__main.save_project_slot)

        project_menu = QMenu("Проект", self.__main)

        project_menu.addAction(new_action)
        project_menu.addAction(download_action)
        project_menu.addAction(save_action)

        self.__project_menu = project_menu

    @property
    def project_menu(self):
        return self.__project_menu
