import pandas as pd

from rqadviser.nlp.nlp_parent import NlpParent


class CosineProcessor(NlpParent):
    def __init__(self, requirement_df):
        super().__init__(requirement_df)
        self._word_cloud = set()

    def prepare(self):
        self._compute_word_cloud()
        self._compute_word_matrix()

    def _compute_word_cloud(self):
        self._requirement_df.apply(lambda row: self._word_cloud.update(set((row["Requirement"]))), axis=1)
        sorted(self._word_cloud)

    def _compute_word_matrix(self):
        arrays = []
        for _, row in self._requirement_df["Requirement"].items():
            arrays.append(self._get_row(row))
        self._vector_df = pd.DataFrame.from_records(arrays, columns=self._word_cloud)

    def _get_row(self, row: pd.DataFrame):
        word_vector = []
        value = 0
        for word in self._word_cloud:
            if word in row:
                value = 1
            else:
                value = 0
            word_vector.append(value)
        return word_vector
