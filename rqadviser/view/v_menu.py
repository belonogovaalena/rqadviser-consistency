"""
Интерфейс меню
"""
from PyQt5.QtWidgets import QAction, QMainWindow, QMenu


class ViewMenu:
    """
    Интерфейс меню
    """
    def __init__(self, main: QMainWindow):
        self._project_menu = QMenu()
        self._main = main

    def create_menu(self):
        """
        Создание меню
        """
        new_action = QAction(self._main)
        new_action.setText("Новый проект")
        new_action.triggered.connect(self._main.new_project_slot)

        download_action = QAction(self._main)
        download_action.setText("Загрузить проект")
        download_action.triggered.connect(self._main.download_project_slot)

        save_action = QAction(self._main)
        save_action.setText("Сохранить проект")
        save_action.setEnabled(False)
        save_action.triggered.connect(self._main.save_project_slot)

        project_menu = QMenu("Проект", self._main)

        self._main.signals["file_chosen"].signal.connect(lambda: save_action.setEnabled(True))
        project_menu.addAction(new_action)
        project_menu.addAction(download_action)
        project_menu.addAction(save_action)

        self._project_menu = project_menu

    @property
    def project_menu(self) -> QMenu:
        """
        :return: Меню
        """
        return self._project_menu
