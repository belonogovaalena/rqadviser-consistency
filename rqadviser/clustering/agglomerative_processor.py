from sklearn.cluster import AgglomerativeClustering
from rqadviser.clustering.clustering_parent import ClusteringParent


class AgglomerativeProcessor(ClusteringParent):
    def __init__(self, requirement_df, vector_df, algorithm):
        n_clusters = int(requirement_df.shape[0] / 3.6)
        agglomerate = AgglomerativeClustering(n_clusters=n_clusters,
                                              linkage=algorithm)
        super().__init__(requirement_df, vector_df, agglomerate)
