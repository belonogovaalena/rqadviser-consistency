from rqadviser.signals.df_parsed import DataFrameParsed


class ModelDataFrame:
    def __init__(self):
        self.__df = None
        self.__prepared_df = None
        self.df_signal = DataFrameParsed()

    @property
    def df(self):
        return self.__df

    @df.setter
    # АШШШШШШШШШШШШШШШФИКС
    def df(self, value):
        self.__df = value
        self.df_signal.signal.emit()

    @property
    def prepared_df(self):
        return self.__prepared_df

    @prepared_df.setter
    def prepared_df(self, value):
        self.__prepared_df = value
