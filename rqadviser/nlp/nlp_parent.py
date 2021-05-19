from abc import abstractmethod


class NlpParent:
    def __init__(self, requirement_df):
        self._requirement_df = requirement_df
        self._vector_df = None

    @abstractmethod
    def prepare(self):
        pass

    @property
    def vector_df(self):
        return self._vector_df
