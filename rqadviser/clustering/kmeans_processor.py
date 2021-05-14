from sklearn.cluster import KMeans
from rqadviser.clustering.clustering_abstract import ClusteringAbstract


class KmeansProcessor(ClusteringAbstract):
    def __init__(self, prepared_df, conv_df):
        number_of_cluster = int(prepared_df.shape[0] / 3.6)
        kmeans = KMeans(number_of_cluster, random_state=100)
        super().__init__(prepared_df, conv_df, kmeans)
