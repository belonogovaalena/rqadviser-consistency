"""
Модуль преобразования предложений в числовые вектора методом doc2vec
"""
import gensim
from gensim.models import Doc2Vec

import pandas as pd

from sklearn.utils import shuffle

from rqadviser.nlp.nlp_parent import NlpParent


class Doc2VecProcessor(NlpParent):
    """
    Модуль преобразования предложений в числовые вектора методом doc2vec
    """
    def __init__(self, df, mode="dbow"):
        super().__init__(df)
        self._model = None
        self._mode = mode

    def prepare(self):
        """
        Вычисление векторов
        """
        tagged_doc = gensim.models.doc2vec.TaggedDocument
        self._requirement_df["TaggedDoc"] = self._requirement_df.apply(lambda row: tagged_doc(row["Requirement"], [row.
                                                                                              ID]), axis=1)
        self._init_model()

    def _init_model(self):
        """
        Инициализация модели
        """
        lst = self._requirement_df["TaggedDoc"].tolist()
        if self._mode == "dbow":
            self._model = Doc2Vec(vector_size=150, window=12, min_count=0, workers=11, alpha=0.0555, min_alpha=-0.3,
                                  dm=0)
        elif self._mode == "dm":
            self._model = Doc2Vec(vector_size=150, window=12, min_count=0, workers=11, alpha=0.0555, min_alpha=0.0555,
                                  dm=1)
        else:
            return
        self._model.build_vocab(lst)
        for _ in range(10):
            self._model.train(shuffle(list(lst)), total_examples=len(lst), epochs=1)
            self._model.alpha -= 0.002
            self._model.min_alpha = self._model.alpha
        self._vector_df = pd.DataFrame(self._model.docvecs.doctag_syn0)
