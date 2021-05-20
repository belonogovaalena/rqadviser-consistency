"""
Модуль кластеризации методом K-средних
"""
import pandas as pd

from sklearn.cluster import KMeans

from rqadviser.clustering.clustering_parent import ClusteringParent


class KmeansProcessor(ClusteringParent):
    """
    Модуль кластеризации методом K-средних
    """
    def __init__(self, requirement_df: pd.DataFrame, vector_df: pd.DataFrame):
        n_clusters = int(requirement_df.shape[0] / 3.6)
        kmeans = KMeans(n_clusters, random_state=100)
        super().__init__(requirement_df, vector_df, kmeans)
