from gensim.models import Doc2Vec
import gensim
from gensim.models import Doc2Vec
from sklearn.utils import shuffle

from rqadviser.nlp.nlp_abstract import NlpAbstract


class Doc2VecDmProcessor(NlpAbstract):
    def __init__(self, df):
        super().__init__(df)
        self.__model = None

    def prepare(self):
        tagged_doc = gensim.models.doc2vec.TaggedDocument
        self._df["TaggedDoc"] = self._df.apply(lambda row: tagged_doc(row["Requirement"], [row.ID]), axis=1)
        self.__init_model()

    def __init_model(self):
        lst = self._df["TaggedDoc"].tolist()

        # вариант 1: Метод распределенной памяти, датасет небольшой, обучаемся всего 10 эпох,

        self.__model = Doc2Vec(vector_size=150, window=12, min_count=0, workers=11, alpha=0.0555, min_alpha=0.0555, dm=1)
        self.__model.build_vocab(lst)
        for epoch in range(10):
            self.__model.train(shuffle([x for x in lst]), total_examples=len(lst), epochs=1)
            self.__model.alpha -= 0.002
            self.__model.min_alpha = self.__model.alpha
        self._conv_df = self.__model.docvecs.doctag_syn0
