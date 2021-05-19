from rqadviser.clustering.clustering_parent import ClusteringParent

from sklearn.cluster import KMeans


class KmeansProcessor(ClusteringParent):
    def __init__(self, requirement_df, vector_df):
        n_clusters = int(requirement_df.shape[0] / 3.6)
        kmeans = KMeans(n_clusters, random_state=100)
        super().__init__(requirement_df, vector_df, kmeans)
