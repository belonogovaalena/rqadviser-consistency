"""
Контроллер работы с настройками
"""
import getpass
import logging
import os
import platform
from configparser import ConfigParser
from datetime import datetime
from pathlib import Path
from shutil import copyfile


class ControllerSettings:
    """
    Контроллер работы с настройками
    """
    @staticmethod
    def create_project(csv_file_path: str, root_path: str) -> str:
        """
        Создание директории проекта и копирование в нее файла спецификации
        :param csv_file_path: Путь к выбранному пользователю файлу .csv спецификации
        :param root_path: Путь к хранилищу проектов
        :return: Название проекта
        """
        # определяем название CSV с требованиями
        csv_file_name = Path(csv_file_path).name
        # название проекта складывается из названия CSV и даты формирования проекта
        project_name = "{0}_{1}".format(csv_file_name.split('.')[0], datetime.strftime(datetime.now(), "%Y%m%dT%H%M%S"))
        try:
            # создание папки проекта
            Path(os.path.join(root_path, project_name)).mkdir(parents=True, exist_ok=True)
            # копирование CSV в необходимый проект
            copyfile(csv_file_path, os.path.join(root_path, project_name, 'data.csv'))
        except FileNotFoundError as ex:
            logger.error(ex)
            return ""
        return project_name

    @staticmethod
    def init_root_path() -> str:
        """
        Инициализация директории хранилища проекта
        :return: Директория хранилища проекта
        """
        root_path = ""
        project_path = Path(__file__).parent.parent.parent
        # сначала пытаемся определить путь в конфигурационном файла
        cfg_path = os.path.join(project_path, "cfg", "rqadviser-consistency.ini")
        if os.path.exists(cfg_path):
            config = ConfigParser()
            config.read(cfg_path)
            root_path = config.get("settings", "root")
        # если конфига нет, то пытаемся определить дефолтные пути для разных ОС
        else:
            if platform.system() == "Linux":
                return "/home/{0}/output/rqadviser".format(getpass.getuser())
            if platform.system() == "Windows":
                return "C:\\Users\\{0}\\rqadviser".format(getpass.getuser())
        return root_path


logger = logging.getLogger("rqadviser")
