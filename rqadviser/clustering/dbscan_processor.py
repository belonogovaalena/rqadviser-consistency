"""
Модуль кластеризации методов Density-Based Spatial Clustering of Applications with Noise
"""
import pandas as pd

from sklearn.cluster import DBSCAN

from rqadviser.clustering.clustering_parent import ClusteringParent


class DbscanProcessor(ClusteringParent):
    """
    Модуль кластеризации методов Density-Based Spatial Clustering of Applications with Noise
    """
    def __init__(self, requirement_df: pd.DataFrame, vector_df):
        dbscan = DBSCAN(eps=1.12198, min_samples=1)
        super().__init__(requirement_df, vector_df, dbscan)
