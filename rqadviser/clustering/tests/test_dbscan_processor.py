"""
Тест кластеризации DBSCAN
"""
import unittest

import pandas as pd

from rqadviser.clustering.dbscan_processor import DbscanProcessor
from rqadviser.clustering.tests.common import TEST_CSV_PATH


class TestDbscan(unittest.TestCase):
    """
    Тест кластеризации DBSCAN
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        requirement_df = pd.read_csv(TEST_CSV_PATH)
        vector_df = pd.DataFrame([[0.9, 0.6, 0.6], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0],
                                  [0.6, 0.4, 0.6], [0.0, 0.6, 1.0], [1.0, 4.0, 1.0]])
        self._processor = DbscanProcessor(requirement_df, vector_df)
        self._processor.prepare()

    def test_1_get_nearest(self):
        """
        Проверка поиска ближайших требований
        """
        assert not self._processor.get_nearest("R-0002").empty, "Ошибка получения ближайшего требования"

    def test_2_get_inaccuracies(self):
        """
        Проверка поиска противоречий
        """
        assert not self._processor.get_inaccuracies(0.15).empty, "Ошибка получения противоречий"
