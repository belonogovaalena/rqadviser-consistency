import pandas as pd

from rqadviser.nlp.nlp_parent import NlpParent

from sentence_transformers import SentenceTransformer


class BertProcessor(NlpParent):
    def __init__(self, requirement_df):
        super().__init__(requirement_df)
        self._model = None

    def prepare(self):
        sentences = self._requirement_df["Requirement"].to_list()
        self._model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')
        self._vector_df = pd.DataFrame(self._model.encode(sentences, show_progress_bar=True))
