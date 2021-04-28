from rqadviser.nlp.cosine_processor import CosineProcessor
from rqadviser.clustering.kmeans_processor import KmeansProcessor


class ControllerSingleCheck:
    def __init__(self):
        pass

    def init_nlp_model(self, mode, df):
        nlp_model = None
        if mode == 0:
            nlp_model = CosineProcessor(df)
            nlp_model.prepare()
        return nlp_model

    def init_clustering(self, mode, prepared_df, conv_df):
        cluster_model = None
        if mode == 0:
            cluster_model = KmeansProcessor(prepared_df, conv_df)
        cluster_model.prepare()
        return cluster_model
