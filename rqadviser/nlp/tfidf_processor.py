import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from rqadviser.nlp.nlp_abstract import NlpAbstract


class TfidfProcessor(NlpAbstract):
    def __init__(self, df):
        super().__init__(df)

    def prepare(self):
        self._df["Requirement"] = self._df.apply(lambda row: " ".join(row["Requirement"]), axis=1)
        vec = TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.50)
        self._conv_df = pd.DataFrame(vec.fit_transform(self._df.Requirement).todense(), columns=vec.get_feature_names())
