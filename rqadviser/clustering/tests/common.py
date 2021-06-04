"""
Общие данные для тестов кластеризации
"""
from pathlib import Path

RESOURCES_PATH = Path.joinpath(Path(__file__).parent, "resources")
TEST_CSV_PATH = Path.joinpath(RESOURCES_PATH, "test.csv")
