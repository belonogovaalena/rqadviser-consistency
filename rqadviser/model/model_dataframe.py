from rqadviser.signals.df_parsed import DataFrameParsed


class ModelDataFrame:
    def __init__(self):
        self.__df = None
        self.df_signal = DataFrameParsed()

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, value):
        self.__df = value
        self.df_signal.signal.emit()
