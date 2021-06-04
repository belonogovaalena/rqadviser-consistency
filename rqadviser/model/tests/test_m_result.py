"""
Проверка модели хранения результата
"""
import unittest

from rqadviser.model.m_result import ModelResult


class TestModelResult(unittest.TestCase):
    """
    Проверка модели хранения результата
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        model = ModelResult()
        model.inaccuracies = 1
        model.requirements_cluster = 2
        repr(model)
        assert model.inaccuracies == 1
        assert model.requirements_cluster == 2
