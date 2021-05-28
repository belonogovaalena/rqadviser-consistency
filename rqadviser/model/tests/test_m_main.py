"""
Проверка мастер-модели
"""
import unittest

from rqadviser.model.m_main import ModelMain


class TestModelMain(unittest.TestCase):
    """
    Проверка мастер-модели
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        model = ModelMain()
        model.nlp = 1
        model.settings = 2
        model.save = 3
        model.result = 4
        model.data_frame = 5
        repr(model)
        assert model.nlp == 1
        assert model.settings == 2
        assert model.save == 3
        assert model.result == 4
        assert model.data_frame == 5
