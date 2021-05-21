"""
Тест кластеризации
"""
import unittest

import pandas as pd

from sklearn.cluster import KMeans

from rqadviser.clustering.clustering_parent import ClusteringParent
from rqadviser.clustering.tests.common import TEST_CSV_PATH


class TestClusteringParent(unittest.TestCase):
    """
    Тест кластеризации
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        requirement_df = pd.read_csv(TEST_CSV_PATH)
        vector_df = pd.DataFrame([[0.9, 0.5, 0.6], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0],
                                  [0.6, 0.4, 0.6], [0.4, 0.6, 1.0], [1.0, 0.7, 1.0]])
        kmeans = KMeans(3, random_state=100)
        self._processor = ClusteringParent(requirement_df, vector_df, kmeans)
        self._processor.prepare()

    def test_1_get_nearest(self):
        """
        Проверка поиска ближайших требований
        """
        assert not self._processor.get_nearest("R-0004").empty, "Ошибка получения ближайшего требования"

    def test_2_get_inaccuracies(self):
        """
        Проверка поиска противоречий
        """
        assert not self._processor.get_inaccuracies(0.19).empty, "Ошибка получения противоречий"
