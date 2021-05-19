from gensim.models import Doc2Vec
import gensim
from gensim.models import Doc2Vec
from sklearn.utils import shuffle
import pandas as pd

from rqadviser.nlp.nlp_parent import NlpParent


class Doc2VecDbowProcessor(NlpParent):
    def __init__(self, df):
        super().__init__(df)
        self._model = None

    def prepare(self):
        tagged_doc = gensim.models.doc2vec.TaggedDocument
        self._requirement_df["TaggedDoc"] = self._requirement_df.apply(lambda row: tagged_doc(row["Requirement"], [row.ID]), axis=1)
        self._init_model()

    def _init_model(self):
        lst = self._requirement_df["TaggedDoc"].tolist()

        # вариант 2: Метод распределенной сумки слов, датасет небольшой, обучаемся всего 10 эпох,
        # предсказываем слово из контекста
        self._model = Doc2Vec(vector_size=150, window=12, min_count=0, workers=11, alpha=0.0555, min_alpha=-0.3, dm=0)
        self._model.build_vocab(lst)
        for epoch in range(10):
            self._model.train(shuffle([x for x in lst]), total_examples=len(lst), epochs=1)
            self._model.alpha -= 0.002
            self._model.min_alpha = self._model.alpha
        self._vector_df = pd.DataFrame(self._model.docvecs.doctag_syn0)
