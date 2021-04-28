from sklearn.cluster import AgglomerativeClustering
from rqadviser.clustering.clustering_abstract import ClusteringAbstract


class AgglomerativeProcessor(ClusteringAbstract):
    def __init__(self, prepared_df, conv_df, mode):
        number_of_cluster = int(prepared_df.shape[0] / 3.6)
        agglomerate = AgglomerativeClustering(n_clusters=number_of_cluster,
                                              linkage=mode)
        super().__init__(prepared_df, conv_df, agglomerate)
