from rqadviser.model.model_settings import ModelSettings
from rqadviser.model.model_dataframe import ModelDataFrame


class ModelMain:
    def __init__(self):
        self.__settings = ModelSettings()
        self.__data_frame = ModelDataFrame()

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, value):
        self.__settings = value

    @property
    def data_frame(self):
        return self.__data_frame

    @data_frame.setter
    def data_frame(self, value):
        self.__data_frame = value
