from sklearn.cluster import DBSCAN
from rqadviser.clustering.clustering_parent import ClusteringParent


class DbscanProcessor(ClusteringParent):
    def __init__(self, requirement_df, vector_df):
        dbscan = DBSCAN(eps=1.12198, min_samples=1)
        super().__init__(requirement_df, vector_df, dbscan)
