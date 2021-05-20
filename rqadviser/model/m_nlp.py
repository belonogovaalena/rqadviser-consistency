"""
Модель преобразования предложений в вектора
"""
from rqadviser.nlp.nlp_parent import NlpParent


class ModelNlp:
    """
    Модель преобразования предложений в вектора
    """
    def __init__(self):
        self._cosine = None
        self._tfidf = None
        self._doc2vec_dm = None
        self._doc2vec_dbow = None
        self._bert = None

    @property
    def cosine(self) -> NlpParent:
        """
        :return: Модель простых косинусных растояний
        """
        return self._cosine

    @cosine.setter
    def cosine(self, value: NlpParent):
        """
        :param value: Модель простых косинусных растояний
        """
        self._cosine = value

    @property
    def tfidf(self) -> NlpParent:
        """
        :return: Модель TF-IDF
        """
        return self._tfidf

    @tfidf.setter
    def tfidf(self, value: NlpParent):
        """
        :param value: Модель TF-IDF
        """
        self._tfidf = value

    @property
    def doc2vec_dm(self) -> NlpParent:
        """
        :return: Модель Doc2Vec Distributed Memory
        """
        return self._doc2vec_dm

    @doc2vec_dm.setter
    def doc2vec_dm(self, value: NlpParent):
        """
        :param value: Модель Doc2Vec Distributed Memory
        """
        self._doc2vec_dm = value

    @property
    def doc2vec_dbow(self) -> NlpParent:
        """
        :return: Модель Doc2Vec Distributed Bag Of Words
        """
        return self._doc2vec_dbow

    @doc2vec_dbow.setter
    def doc2vec_dbow(self, value: NlpParent):
        """
        :param value: Модель Doc2Vec Distributed Bag Of Words
        """
        self._doc2vec_dbow = value

    @property
    def bert(self) -> NlpParent:
        """
        :return: Модель BERT
        """
        return self._bert

    @bert.setter
    def bert(self, value: NlpParent):
        """
        :param value: Модель BERT
        """
        self._bert = value

    def __repr__(self):
        return f"ModelNlp: [cosine: {self._cosine}, tfidf: {self._tfidf}, " \
               f"doc2vec_dm: {self._doc2vec_dm}, doc2vec_dbow: {self._doc2vec_dbow}, " \
               f"bert: {self._bert}]"
