from abc import abstractmethod


class ClusteringAbstract:
    def __init__(self, prepared_df, conv_df, algorithm):
        self._prepared_df = prepared_df
        self._conv_df = conv_df
        self._algorithm = algorithm

    def prepare(self):
        self._prepared_df["Cluster"] = self._algorithm.fit_predict(self._conv_df)

    def get_nearest(self, requirement_id):
        # находим, к какому кластеру принадлежит требование с заданным ID
        cluster_id = self._prepared_df.loc[self._prepared_df["ID"] == requirement_id, "Cluster"].values[0]
        return self._prepared_df.loc[self._prepared_df["Cluster"] == cluster_id][["ID", "Requirement"]]
