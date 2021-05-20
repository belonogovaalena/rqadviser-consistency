"""
Контроллер обработки файла спецификаии
"""
import pandas as pd

from rqadviser.nlp.data_processor import DataProcessor


class ControllerProcessCsv:
    """
    Контроллер обработки файла спецификаии
    """
    @staticmethod
    def parse_csv_normalized(file_path: str) -> pd.DataFrame:
        """
        Проводит препроцессинг данных спецификации
        :param file_path: Путь к файлу спецификации
        :return: Датафрейм с спецификацией
        """
        data_processor = DataProcessor()
        data_processor.prepare_unsupervised(file_path)
        return data_processor.norm_df

    @staticmethod
    def parse_csv(file_path: str) -> pd.DataFrame:
        """
        Читает файл спецификации в датафрейм без препроцессинга
        :param file_path: Путь к файлу спецификации
        :return: Датафрейм с спецификацией
        """
        return pd.read_csv(file_path)
