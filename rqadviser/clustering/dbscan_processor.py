from sklearn.cluster import DBSCAN
from rqadviser.clustering.clustering_abstract import ClusteringAbstract


class DbscanProcessor(ClusteringAbstract):
    def __init__(self, prepared_df, conv_df):
        dbscan = DBSCAN(eps=1.12198, min_samples=1)
        super().__init__(prepared_df, conv_df, dbscan)
