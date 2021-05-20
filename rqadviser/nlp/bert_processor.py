"""
Модуль преобразования предложений в числовые вектора методом bert
"""
import pandas as pd

# pylint: disable=import-error
from sentence_transformers import SentenceTransformer

from rqadviser.nlp.nlp_parent import NlpParent


class BertProcessor(NlpParent):
    """
    Модуль преобразования предложений в числовые вектора методом bert
    """
    def __init__(self, requirement_df: pd.DataFrame):
        super().__init__(requirement_df)
        self._model = None

    def prepare(self):
        """
        Получение векторов
        """
        sentences = self._requirement_df["Requirement"].to_list()
        self._model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')
        self._vector_df = pd.DataFrame(self._model.encode(sentences, show_progress_bar=True))
