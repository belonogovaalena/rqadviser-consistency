import pandas as pd
from rqadviser.nlp.data_processor import DataProcessor


class ControllerProcessCsv:
    @staticmethod
    def parse_csv_normalized(file_path):
        data_processor = DataProcessor()
        data_processor.prepare_unsupervised(file_path)
        return data_processor.df

    @staticmethod
    def parse_csv(file_path):
        return pd.read_csv(file_path)
