from sentence_transformers import SentenceTransformer
from rqadviser.nlp.nlp_abstract import NlpAbstract


class BertProcessor(NlpAbstract):
    def __init__(self, df):
        super().__init__(df)
        self.__model = None

    def prepare(self):
        sentences = self._df["Requirement"].to_list()
        self.__model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')
        self._conv_df = self.__model.encode(sentences, show_progress_bar=True)
