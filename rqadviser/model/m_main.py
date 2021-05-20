"""
Мастер-модель
"""
from rqadviser.model.m_dataframe import ModelDataFrame
from rqadviser.model.m_nlp import ModelNlp
from rqadviser.model.m_result import ModelResult
from rqadviser.model.m_save import ModelSave
from rqadviser.model.m_settings import ModelSettings


class ModelMain:
    """
    Мастер-модель
    """
    def __init__(self):
        self._settings = ModelSettings()
        self._data_frame = ModelDataFrame()
        self._nlp = ModelNlp()
        self._result = ModelResult()
        self._save = ModelSave()

    @property
    def settings(self) -> ModelSettings:
        """
        :return: Модель настроек
        """
        return self._settings

    @settings.setter
    def settings(self, value: ModelSettings):
        """
        :param value: Модель настроек
        """
        self._settings = value

    @property
    def data_frame(self) -> ModelDataFrame:
        """
        :return: Модель хранения таблицы спецификации
        """
        return self._data_frame

    @data_frame.setter
    def data_frame(self, value: ModelDataFrame):
        """
        :param value: Модель хранения таблицы спецификации
        """
        self._data_frame = value

    @property
    def nlp(self) -> ModelNlp:
        """
        :return: Модель преобразования предложений в вектора
        """
        return self._nlp

    @nlp.setter
    def nlp(self, value: ModelNlp):
        """
        :param value: Модель преобразования предложений в вектора
        """
        self._nlp = value

    @property
    def result(self) -> ModelResult:
        """
        :return: Модель результата анализа
        """
        return self._result

    @result.setter
    def result(self, value: ModelResult):
        """
        :param value: Модель результата анализа
        """
        self._result = value

    @property
    def save(self) -> ModelSave:
        """
        :return: Модель состояния сохранения
        """
        return self._save

    @save.setter
    def save(self, value) -> ModelSave:
        """
        :param value: Модель состояния сохранения
        """
        self._save = value

    def __repr__(self):
        return f"ModelMain: [settings: {repr(self._settings)}, data_frame: {repr(self._data_frame)}, " \
               f"nlp: {repr(self._nlp)}, result: {repr(self._result)}, " \
               f"save: {repr(self._save)}]"
