"""
Контроллер загрузки проекта
"""
import logging
import os
import pickle  # noqa: S403
from typing import Any

from rqadviser.nlp.nlp_parent import NlpParent


class ControllerDownload:
    """
    Контроллер загрузки проекта
    """
    def __init__(self):
        self.__project_path = ""

    def set_project_path(self, path: str):
        """
        Установка директории проекта
        :param path: Директория проекта
        """
        self.__project_path = path

    def __check_model_exists(self, model: str) -> bool:
        """
        :param model: Наименование модели, существование которой надо проверить
        :return: Признак существования модели
        """
        path = self.__get_pickle_path(model)
        return os.path.exists(path)

    def __get_pickle_path(self, name: str) -> str:
        """
        :param name: Наименование модели
        :return: Путь к файлу модели .pkl
        """
        return os.path.join(self.__project_path, "{0}.pkl".format(name))

    def download_model_if_exists(self, model: str) -> Any[NlpParent, None]:
        """
        Загрузка модели из файла .pkl
        :param model: Наименование модели
        :return: Загруженная модель
        """
        if not self.__check_model_exists(model):
            return None
        path = self.__get_pickle_path(model)
        try:
            with open(path, 'rb') as file:
                result = pickle.load(file)  # noqa: S301
        except pickle.PickleError as ex:
            logger.error(ex)
            return None
        return result


logger = logging.getLogger("rqadviser")
