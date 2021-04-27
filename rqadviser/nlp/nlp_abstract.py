from abc import ABCMeta, abstractmethod


class NlpAbstract:
    def __init__(self, df):
        self._df = df
        self._conv_df = None

    @abstractmethod
    def prepare(self):
        pass

    @property
    def conv_df(self):
        return self._conv_df
