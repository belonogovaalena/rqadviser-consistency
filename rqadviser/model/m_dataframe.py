"""
Модель хранения таблицы спецификации
"""
import pandas as pd

from rqadviser.signals.signals import DataFrameParsed


class ModelDataFrame:
    """
    Модель хранения таблицы спецификации
    """
    def __init__(self):
        self._req_df = None
        self._norm_req_df = None
        self.df_signal = DataFrameParsed()

    @property
    def req_df(self) -> pd.DataFrame:
        """
        :return: Спецификация требований
        """
        return self._req_df

    @req_df.setter
    def req_df(self, value: pd.DataFrame):
        """
        :param value: Спецификация требований
        """
        self._req_df = value
        self.df_signal.signal.emit()

    @property
    def norm_req_df(self) -> pd.DataFrame:
        """
        :return: Спецификация требований после препроцессинга
        """
        return self._norm_req_df

    @norm_req_df.setter
    def norm_req_df(self, value: pd.DataFrame):
        """
        :param value: Спецификация требований после препроцессинга
        """
        self._norm_req_df = value

    def __repr__(self):
        return f"ModelDataFrame: [req_df: {self._req_df}, norm_req_df: {self._norm_req_df}]"
