class ModelSettings:
    def __init__(self):
        self.__saves_path = ""
        self.__project_name = ""

    @property
    def saves_path(self):
        return self.__saves_path

    @saves_path.setter
    #FIIIIIIIIIIIIIIIIIIIIIIIIX
    def saves_path(self, value):
        self.__saves_path = value

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, value):
        self.__project_name = value
