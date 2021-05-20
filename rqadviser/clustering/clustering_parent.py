"""
Родительский модуль для кластеризации
"""
import itertools

import pandas as pd

import scipy.spatial

from sklearn.base import ClusterMixin


class ClusteringParent:
    """
    Родительский модуль для кластеризации
    """
    def __init__(self, requirement_df: pd.DataFrame, vector_df: pd.DataFrame, algorithm: ClusterMixin):
        self._requirement_df = requirement_df
        self._vector_df = vector_df
        self._algorithm = algorithm

    def prepare(self):
        """
        Кластеризация
        """
        self._requirement_df["Cluster"] = self._algorithm.fit_predict(self._vector_df)

    def get_nearest(self, requirement_id: str) -> pd.DataFrame:
        """
        :param requirement_id: ID заданного требоваия
        :return: Кластер требований, в который входит заданное
        """
        # находим, к какому кластеру принадлежит требование с заданным ID
        cluster_id = self._requirement_df.loc[self._requirement_df["ID"] == requirement_id, "Cluster"].values[0]
        return self._requirement_df.loc[self._requirement_df["Cluster"] == cluster_id][["ID", "Requirement"]]

    def get_inaccuracies(self, measure: float) -> pd.DataFrame:
        """
        :param measure: Минимально допустимое расстояние между требованиями
        :return: Список противоречий
        """
        self._vector_df["ID"] = self._requirement_df["ID"].to_numpy()
        # получаем перечень кластеров
        clusters = self._requirement_df["Cluster"].unique().tolist()
        clusters.sort()
        consistencies = pd.DataFrame(columns=['R1', 'R2', 'Res'])
        for cluster in clusters:
            # определяем группу требований для конкретного кластера
            group = self._requirement_df.loc[self._requirement_df["Cluster"] == cluster, "ID"].tolist()
            pairs = list(itertools.combinations(group, 2))
            if pairs:
                # для всех требований в кластере определяем расстояние
                for pair in pairs:
                    # pylint: disable=invalid-name
                    v1 = self._vector_df.loc[self._vector_df["ID"] == pair[0]].drop("ID", axis=1).values[0]
                    v2 = self._vector_df.loc[self._vector_df["ID"] == pair[1]].drop("ID", axis=1).values[0]
                    dist = scipy.spatial.distance.cosine(v1, v2)
                    # если оно оказывается меньше допустимого - добавляем пару требований как противоречие
                    if dist < measure:
                        consistencies = consistencies.append(pd.DataFrame({"R1": pair[0], "R2": pair[1], "Res": dist},
                                                                          index=[0]), ignore_index=True)
        del self._vector_df["ID"]
        return consistencies
