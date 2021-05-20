"""
Модуль преобразования предложений в числовые вектора методом TF-IDF
"""
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from rqadviser.nlp.nlp_parent import NlpParent


class TfidfProcessor(NlpParent):
    """
    Модуль преобразования предложений в числовые вектора методом TF-IDF
    """
    def prepare(self):
        """
        Вычисление векторов
        """
        self._requirement_df["Requirement"] = self._requirement_df.apply(lambda row: " ".join(row["Requirement"]),
                                                                         axis=1)
        vec = TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.50)
        self._vector_df = pd.DataFrame(vec.fit_transform(self._requirement_df.Requirement).todense(), columns=vec.
                                       get_feature_names())
