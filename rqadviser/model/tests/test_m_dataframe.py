"""
Проверка модели хранения спецификации
"""
import unittest

from rqadviser.model.m_dataframe import ModelDataFrame


class TestModelDataFrame(unittest.TestCase):
    """
    Проверка модели хранения спецификации
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        model = ModelDataFrame()
        model.req_df = {'foo1': 'bar1'}
        model.norm_req_df = {'foo2': 'bar2'}
        repr(model)
        assert model.req_df == {'foo1': 'bar1'}
        assert model.norm_req_df == {'foo2': 'bar2'}
