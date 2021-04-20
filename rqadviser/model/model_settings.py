class ModelSettings:
    def __init__(self):
        # TODO: инициализировать настройки из файла
        self.__saves_path = "/home/belonogova/rqadviser/"

    @property
    def saves_path(self):
        return self.__saves_path

    @saves_path.setter
    def saves_path(self, value):
        self.__saves_path = value
