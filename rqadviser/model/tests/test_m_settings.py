"""
Проверка модели хранения настроек
"""
import unittest

from rqadviser.model.m_settings import ModelSettings


class TestModelSettings(unittest.TestCase):
    """
    Проверка модели хранения настроек
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        model = ModelSettings()
        model.project_name = 1
        model.root_path = 2
        repr(model)
        assert model.project_name == 1
        assert model.root_path == 2
