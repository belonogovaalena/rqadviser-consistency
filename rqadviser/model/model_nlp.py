class ModelNlp:
    def __init__(self):
        self.__cosine = None
        self.__tfidf = None
        self.__doc2vec_dm = None
        self.__doc2vec_dbow = None
        self.__bert = None

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

    @property
    def doc2vec_dm(self):
        return self.__doc2vec_dm

    @doc2vec_dm.setter
    def doc2vec_dm(self, value):
        self.__doc2vec_dm = value

    @property
    def doc2vec_dbow(self):
        return self.__doc2vec_dbow

    @doc2vec_dbow.setter
    def doc2vec_dbow(self, value):
        self.__doc2vec_dbow = value

    @property
    def bert(self):
        return self.__bert

    @bert.setter
    def bert(self, value):
        self.__bert = value
