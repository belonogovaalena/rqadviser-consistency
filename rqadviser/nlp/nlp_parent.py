"""
Родительский класс для модулей преобразования предложений в числовые вектора
"""
from abc import abstractmethod

import pandas as pd


class NlpParent:
    """
    Родительский класс для модулей преобразования предложений в числовые вектора
    """
    def __init__(self, requirement_df: pd.DataFrame):
        self._requirement_df = requirement_df
        self._vector_df = None

    @abstractmethod
    def prepare(self):
        """
        Преобразование предложений в вектора
        """

    @property
    def vector_df(self):
        """
        :return: Датафрейм из векторов
        """
        return self._vector_df
