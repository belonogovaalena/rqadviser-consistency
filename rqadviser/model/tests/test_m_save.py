"""
Проверка модели хранения состояния сохранения
"""
import unittest

from rqadviser.model.m_save import ModelSave


class TestModelResult(unittest.TestCase):
    """
    Проверка модели хранения состояния сохранения
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        model = ModelSave()
        model.save_state = True
        repr(model)
        assert model.save_state
