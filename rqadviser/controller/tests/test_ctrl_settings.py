"""
Тест настроек проекта
"""
import os
import unittest

from rqadviser.controller.ctrl_settings import ControllerSettings
from rqadviser.controller.tests.common import OUTPUT_PATH, TEST_CSV_PATH


class TestControllerSettings(unittest.TestCase):
    """
    Тест настроек проекта
    """

    def setUp(self) -> None:
        self._ctrl = ControllerSettings()

    def test_1_root_path(self):
        """
        Тест получения пути хранилища проекта
        """
        assert self._ctrl.init_root_path(), "Ошибка получения пути хранилища проекта"

    def test_2_create_project(self):
        """
        Тест создания проекта
        """
        assert not self._ctrl.create_project("test", OUTPUT_PATH)
        assert self._ctrl.create_project(TEST_CSV_PATH, OUTPUT_PATH), "Ошибка создания проекта"

    def tearDown(self) -> None:
        dirs = os.listdir(OUTPUT_PATH)
        for dir_ in dirs:
            path = os.path.join(OUTPUT_PATH, dir_)
            if str(dir_).startswith("test") and os.path.isdir(path):
                files = os.listdir(path)
                for file in files:
                    os.remove(os.path.join(path, file))
            os.rmdir(path)
