from sklearn.mixture import GaussianMixture
from rqadviser.clustering.clustering_abstract import ClusteringAbstract


class EMProcessor(ClusteringAbstract):
    def __init__(self, prepared_df, conv_df):
        number_of_cluster = int(prepared_df.shape[0] / 3.6)
        gmm = GaussianMixture(number_of_cluster, random_state=100)
        super().__init__(prepared_df, conv_df, gmm)
