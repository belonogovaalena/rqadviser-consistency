from rqadviser.model.m_dataframe import ModelDataFrame
from rqadviser.model.m_nlp import ModelNlp
from rqadviser.model.m_result import ModelResult
from rqadviser.model.m_save import ModelSave
from rqadviser.model.m_settings import ModelSettings


class ModelMain:
    def __init__(self):
        self._settings = ModelSettings()
        self._data_frame = ModelDataFrame()
        self._nlp = ModelNlp()
        self._result = ModelResult()
        self._save = ModelSave()

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value

    @property
    def data_frame(self):
        return self._data_frame

    @data_frame.setter
    def data_frame(self, value):
        self._data_frame = value

    @property
    def nlp(self):
        return self._nlp

    @nlp.setter
    def nlp(self, value):
        self._nlp = value

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @property
    def save(self):
        return self._save

    @save.setter
    def save(self, value):
        self._save = value

    def __repr__(self):
        return f"ModelMain: [settings: {repr(self._settings)}, data_frame: {repr(self._data_frame)}, " \
               f"nlp: {repr(self._nlp)}, result: {repr(self._result)}, " \
               f"save: {repr(self._save)}]"
