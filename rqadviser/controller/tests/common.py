"""
Общие данные для тестов контроллера
"""
from pathlib import Path

OUTPUT_PATH = Path.joinpath(Path(__file__).parent, "output")
RESOURCES_PATH = Path.joinpath(Path(__file__).parent, "resources")
TEST_CSV_PATH = Path.joinpath(RESOURCES_PATH, "test.csv")
