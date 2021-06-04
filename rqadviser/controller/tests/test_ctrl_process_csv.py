"""
Тест обработки спецификации требований
"""
import unittest

from rqadviser.controller.ctrl_process_csv import ControllerProcessCsv
from rqadviser.controller.tests.common import TEST_CSV_PATH


class TestControllerProcessCsv(unittest.TestCase):
    """
    Тест обработки спецификации требований
    """
    def setUp(self) -> None:
        self._ctrl = ControllerProcessCsv()

    def test_1_parse(self):
        """
        Тест обработки спецификации требований
        """
        assert not self._ctrl.parse_csv(TEST_CSV_PATH).empty, "Ошибка загрузки объекта"

    def test_2_parse_normalized(self):
        """
        Тест обработки спецификации требований и нормализации
        """
        assert not self._ctrl.parse_csv_normalized(TEST_CSV_PATH).empty, "Ошибка загрузки объекта"
