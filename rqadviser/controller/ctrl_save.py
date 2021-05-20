"""
Контроллер сохранеия проекта
"""
import logging
import os
import pickle  # noqa: S403

from rqadviser.nlp.nlp_parent import NlpParent


class ControllerSave:
    """
    Контроллер сохранеия проекта
    """
    def __init__(self):
        self.__project_path = ""

    def set_project_path(self, path: str):
        """
        Установка директории проекта
        :param path: Директория проекта
        """
        self.__project_path = path

    def __get_pickle_path(self, name: str) -> str:
        """
        :param name: Наименование модели
        :return: Путь к файлу модели .pkl
        """
        return os.path.join(self.__project_path, "{0}.pkl".format(name))

    def save_to_file(self, model: NlpParent, name: str) -> bool:
        """
        Сохранение обученной модели преобразования предложений в вектора в файл .pkl
        :param model: Модель для сохранения
        :param name: Наименование модели
        :return: Признак успешного сохранения
        """
        file_path = self.__get_pickle_path(name)
        try:
            with open(file_path, 'wb') as output:
                pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)
            return True
        except pickle.PickleError as ex:
            logger.error(ex)
            return False


logger = logging.getLogger("rqadviser")
