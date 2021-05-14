import pandas as pd
import itertools
import scipy.spatial


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

    def get_inaccuracies(self, measure):
        self._conv_df["ID"] = self._prepared_df["ID"].to_numpy()
        clusters = self._prepared_df["Cluster"].unique().tolist()
        clusters.sort()
        consistencies = pd.DataFrame(columns=['R1', 'R2', 'Res'])
        for cluster in clusters:
            group = self._prepared_df.loc[self._prepared_df["Cluster"] == cluster, "ID"].tolist()
            pairs = list(itertools.combinations(group, 2))
            if pairs:
                for pair in pairs:
                    v1 = self._conv_df.loc[self._conv_df["ID"] == pair[0]].drop("ID", axis=1).values[0]
                    v2 = self._conv_df.loc[self._conv_df["ID"] == pair[1]].drop("ID", axis=1).values[0]
                    dist = scipy.spatial.distance.cosine(v1, v2)
                    if dist < measure:
                        consistencies = consistencies.append(pd.DataFrame({"R1": pair[0], "R2": pair[1], "Res": dist},
                                                                          index=[0]), ignore_index=True)
        del self._conv_df["ID"]
        return consistencies
