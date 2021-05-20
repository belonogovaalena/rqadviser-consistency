"""
Модель настроек
"""


class ModelSettings:
    """
    Модель настроек
    """
    def __init__(self):
        self._root_path = ""
        self._project_name = ""

    @property
    def root_path(self) -> str:
        """
        :return: Путь к хранилищу проектов
        """
        return self._root_path

    @root_path.setter
    def root_path(self, value: str):
        """
        :param value: Путь к хранилищу проектов
        """
        self._root_path = value

    @property
    def project_name(self) -> str:
        """
        :return: Наименование проекта
        """
        return self._project_name

    @project_name.setter
    def project_name(self, value: str):
        """
        :param value: Наименование проекта
        """
        self._project_name = value

    def __repr__(self):
        return f"ModelSettings: [root_path: {self._root_path}, project_name: {self._project_name}]"
