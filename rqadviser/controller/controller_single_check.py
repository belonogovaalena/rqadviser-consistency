from rqadviser.nlp.cosine_processor import CosineProcessor
from rqadviser.nlp.tfidf_processor import TfidfProcessor
from rqadviser.nlp.doc2vecdm_processor import Doc2VecDmProcessor
from rqadviser.nlp.doc2vecdbow_processor import Doc2VecDbowProcessor
from rqadviser.nlp.bert_processor import BertProcessor
from rqadviser.clustering.kmeans_processor import KmeansProcessor
from rqadviser.clustering.em_processor import EMProcessor
from rqadviser.clustering.agglomerative_processor import AgglomerativeProcessor
from rqadviser.clustering.dbscan_processor import DbscanProcessor


class ControllerSingleCheck:
    def __init__(self):
        pass

    def init_nlp_model(self, mode, df):
        nlp_model = None
        if mode == 0:
            nlp_model = CosineProcessor(df)
        if mode == 1:
            nlp_model = TfidfProcessor(df)
        if mode == 2:
            nlp_model = Doc2VecDmProcessor(df)
        if mode == 3:
            nlp_model = Doc2VecDbowProcessor(df)
        if mode == 4:
            nlp_model = BertProcessor(df)
        nlp_model.prepare()
        return nlp_model

    def init_clustering(self, mode, prepared_df, conv_df):
        cluster_model = None
        if mode == 0:
            cluster_model = KmeansProcessor(prepared_df, conv_df)
        elif mode == 1:
            cluster_model = EMProcessor(prepared_df, conv_df)
        elif mode == 2:
            cluster_model = AgglomerativeProcessor(prepared_df, conv_df, 'average')
        elif mode == 3:
            cluster_model = AgglomerativeProcessor(prepared_df, conv_df, 'ward')
        elif mode == 4:
            cluster_model = AgglomerativeProcessor(prepared_df, conv_df, 'complete')
        elif mode == 5:
            cluster_model = AgglomerativeProcessor(prepared_df, conv_df, 'single')
        elif mode == 6:
            cluster_model = DbscanProcessor(prepared_df, conv_df)
        cluster_model.prepare()
        return cluster_model
