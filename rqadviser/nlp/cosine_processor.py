import pandas as pd
from rqadviser.nlp.nlp_abstract import NlpAbstract


class CosineProcessor(NlpAbstract):
    def __init__(self, df):
        super().__init__(df)
        self.__word_cloud = set()

    def prepare(self):
        self.__compute_word_cloud()
        self.__compute_word_matrix()

    def __compute_word_cloud(self):
        self._df.apply(lambda row: self.__word_cloud.update(set((row["Requirement"]))), axis=1)
        sorted(self.__word_cloud)

    def __compute_word_matrix(self):
        arrays = []
        for _, row in self._df["Requirement"].items():
            arrays.append(self.__get_row(row))
        self._conv_df = pd.DataFrame.from_records(arrays, columns=self.__word_cloud)

    def __get_row(self, row: pd.DataFrame):
        word_vector = list()
        value = 0
        for word in self.__word_cloud:
            if word in row:
                value = 1
            else:
                value = 0
            word_vector.append(value)
        return word_vector
