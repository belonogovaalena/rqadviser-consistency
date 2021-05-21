"""
Тест загрузки объекта
"""
import pickle
import unittest
from pathlib import Path

from rqadviser.controller.ctrl_download import ControllerDownload
from rqadviser.controller.tests.common import OUTPUT_PATH


class TestControllerDownload(unittest.TestCase):
    """
    Тест загрузки объекта
    """
    def setUp(self) -> None:
        self._ctrl = ControllerDownload()
        self._ctrl.set_project_path(OUTPUT_PATH)

    def test_1_download_project(self):
        """
        Тест загрузки объекта
        """
        object_ = {'foo': 'bar'}
        Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)
        file_path = Path.joinpath(OUTPUT_PATH, "tests.pkl")
        with open(file_path, 'wb') as output:
            pickle.dump(object_, output, pickle.HIGHEST_PROTOCOL)
        model = self._ctrl.download_model_if_exists("tests")
        assert model == object_, "Ошибка загрузки объекта"

    def test_2_download_error(self):
        """
        Тест загрузки объекта
        """
        model = self._ctrl.download_model_if_exists("test2")
        assert not model, "Ошибка загрузки несуществующего объекта"

    def tearDown(self):
        file_path = Path.joinpath(OUTPUT_PATH, "tests.pkl")
        if Path.exists(file_path):
            Path.unlink(file_path)
