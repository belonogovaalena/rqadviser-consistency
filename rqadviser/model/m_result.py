"""
Модель результата анализа
"""
import pandas as pd

from rqadviser.signals.signals import ClusterFound
from rqadviser.signals.signals import InaccuraciesFound


class ModelResult:
    """
    Модель результата анализа
    """
    def __init__(self):
        self.cluster_signal = ClusterFound()
        self.inaccuracies_signal = InaccuraciesFound()
        self._requirements_cluster = None
        self._inaccuracies = None

    @property
    def requirements_cluster(self) -> pd.DataFrame:
        """
        :return: Датафрейм с требованиями заданного кластера
        """
        return self._requirements_cluster

    @requirements_cluster.setter
    def requirements_cluster(self, value: pd.DataFrame):
        """
        :param value: Датафрейм с требованиями заданного кластера
        """
        self._requirements_cluster = value
        self.cluster_signal.signal.emit()

    @property
    def inaccuracies(self) -> pd.DataFrame:
        """
        :return: Датафрейм с противоречащими требованиями
        """
        return self._inaccuracies

    @inaccuracies.setter
    def inaccuracies(self, value: pd.DataFrame):
        """
        :param value: Датафрейм с противоречащими требованиями
        """
        self._inaccuracies = value
        self.inaccuracies_signal.signal.emit()

    def __repr__(self):
        return f"ModelResult: [requirements_cluster: {self._requirements_cluster}, " \
               f"inaccuracies: {self._inaccuracies}]"
