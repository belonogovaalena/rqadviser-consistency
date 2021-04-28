class ModelNlp:
    def __init__(self):
        self.__cosine = None
        self.__tfidf = None

    @property
    def cosine(self):
        return self.__cosine

    @cosine.setter
    def cosine(self, value):
        self.__cosine = value

    @property
    def tfidf(self):
        return self.__tfidf

    @tfidf.setter
    def tfidf(self, value):
        self.__tfidf = value
