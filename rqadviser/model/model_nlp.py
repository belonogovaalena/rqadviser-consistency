class ModelNlp:
    def __init__(self):
        self.__cosine = None

    @property
    def cosine(self):
        return self.__cosine

    @cosine.setter
    def cosine(self, value):
        self.__cosine = None