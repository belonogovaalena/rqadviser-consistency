import pandas as pd


class ControllerCsv:
    def __init__(self):
        pass

    def parse_csv(self, file_name):
        return pd.read_csv(file_name)
