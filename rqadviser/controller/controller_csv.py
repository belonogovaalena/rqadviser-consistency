import pandas as pd
from rqadviser.nlp.data_processor import DataProcessor


class ControllerCsv:
    def __init__(self):
        pass

    def parse_csv(self, file_name):
        data_processor = DataProcessor()
        data_processor.prepare_unsupervised(file_name)
        return data_processor.df, pd.read_csv(file_name)
