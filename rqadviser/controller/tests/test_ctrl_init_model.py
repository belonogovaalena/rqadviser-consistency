"""
Тест инициализации объектов
"""
import unittest
from unittest import mock

import pandas as pd

from rqadviser.controller.ctrl_init_model import ControllerInitModel
from rqadviser.controller.tests.common import TEST_CSV_PATH


class TestControllerInit(unittest.TestCase):
    """
    Тест инициализации объектов
    """
    def setUp(self) -> None:
        self._ctrl = ControllerInitModel()

    def test_1_init_clustering(self):
        """
        Тест инициализации модели кластеризации
        """
        requirement_df = pd.read_csv(TEST_CSV_PATH)
        vector_df = pd.DataFrame([[0.9, 0.5, 0.6], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0],
                                  [0.6, 0.4, 0.6], [0.4, 0.6, 1.0], [1.0, 0.7, 1.0]])
        assert not self._ctrl.init_nlp_model(0, pd.DataFrame())
        for i in range(0, 7):
            assert self._ctrl.init_clustering(i, requirement_df, vector_df)

    @mock.patch('rqadviser.controller.ctrl_init_model.ControllerInitModel.prepare')
    def test_2_init_nlp(self, _):
        """
        Тест инициализации модели кластеризации
        """
        requirement_df = pd.read_csv(TEST_CSV_PATH)
        assert not self._ctrl.init_clustering(0, pd.DataFrame(), pd.DataFrame())
        for i in range(0, 5):
            assert self._ctrl.init_nlp_model(i, requirement_df)
