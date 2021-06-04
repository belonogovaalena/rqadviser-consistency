"""
Тест сохранения проекта
"""
import unittest
from pathlib import Path

from rqadviser.controller.ctrl_save import ControllerSave
from rqadviser.controller.tests.common import OUTPUT_PATH


class TestControllerSave(unittest.TestCase):
    """
    Тест сохранения проекта
    """
    def setUp(self) -> None:
        self._ctrl = ControllerSave()
        self._ctrl.set_project_path(str(OUTPUT_PATH))

    def test_1_save(self):
        """
        Тест сохранения проекта
        """
        object_ = {'foo': 'bar'}
        assert self._ctrl.save_to_file(object_, "tests"), "Ошибка сохранения объекта"

    def tearDown(self):
        file_path = Path.joinpath(OUTPUT_PATH, "tests.pkl")
        if Path.exists(file_path):
            Path.unlink(file_path)
