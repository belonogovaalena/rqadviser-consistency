from rqadviser.signals.df_parsed import DataFrameParsed


class ModelDataFrame:
    def __init__(self):
        self._req_df = None
        self._norm_req_df = None
        self.df_signal = DataFrameParsed()

    @property
    def req_df(self):
        return self._req_df

    @req_df.setter
    def req_df(self, value):
        self._req_df = value
        self.df_signal.signal.emit()

    @property
    def norm_req_df(self):
        return self._norm_req_df

    @norm_req_df.setter
    def norm_req_df(self, value):
        self._norm_req_df = value
