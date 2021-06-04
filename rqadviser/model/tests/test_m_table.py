"""
Проверка создания модели таблицы
"""
import unittest
from pathlib import Path

import pandas as pd

from rqadviser.model.m_table import TableModel

RESOURCES_PATH = Path.joinpath(Path(__file__).parent, "resources")
TEST_CSV_PATH = Path.joinpath(RESOURCES_PATH, "test.csv")


class TestTableModel(unittest.TestCase):
    """
    Проверка создания модели таблицы
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        df = pd.read_csv(TEST_CSV_PATH)
        model = TableModel(df)
        assert model
