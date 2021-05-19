class ModelNlp:
    def __init__(self):
        self._cosine = None
        self._tfidf = None
        self._doc2vec_dm = None
        self._doc2vec_dbow = None
        self._bert = None

    @property
    def cosine(self):
        return self._cosine

    @cosine.setter
    def cosine(self, value):
        self._cosine = value

    @property
    def tfidf(self):
        return self._tfidf

    @tfidf.setter
    def tfidf(self, value):
        self._tfidf = value

    @property
    def doc2vec_dm(self):
        return self._doc2vec_dm

    @doc2vec_dm.setter
    def doc2vec_dm(self, value):
        self._doc2vec_dm = value

    @property
    def doc2vec_dbow(self):
        return self._doc2vec_dbow

    @doc2vec_dbow.setter
    def doc2vec_dbow(self, value):
        self._doc2vec_dbow = value

    @property
    def bert(self):
        return self._bert

    @bert.setter
    def bert(self, value):
        self._bert = value

    def __repr__(self):
        return f"ModelNlp: [cosine: {self._cosine}, tfidf: {self._tfidf}, " \
               f"doc2vec_dm: {self._doc2vec_dm}, doc2vec_dbow: {self._doc2vec_dbow}, " \
               f"bert: {self._bert}]"
