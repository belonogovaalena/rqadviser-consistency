from rqadviser.nlp.cosine_processor import CosineProcessor
from rqadviser.nlp.tfidf_processor import TfidfProcessor
from rqadviser.nlp.doc2vecdm_processor import Doc2VecDmProcessor
from rqadviser.nlp.doc2vecdbow_processor import Doc2VecDbowProcessor
from rqadviser.nlp.bert_processor import BertProcessor
from rqadviser.clustering.kmeans_processor import KmeansProcessor
from rqadviser.clustering.em_processor import EMProcessor
from rqadviser.clustering.agglomerative_processor import AgglomerativeProcessor
from rqadviser.clustering.dbscan_processor import DbscanProcessor


class ControllerInitModel:
    @staticmethod
    def init_nlp_model(mode, requirement_df):
        nlp_model = None
        if requirement_df.empty:
            return nlp_model
        if mode == 0:
            nlp_model = CosineProcessor(requirement_df)
        if mode == 1:
            nlp_model = TfidfProcessor(requirement_df)
        if mode == 2:
            nlp_model = Doc2VecDmProcessor(requirement_df)
        if mode == 3:
            nlp_model = Doc2VecDbowProcessor(requirement_df)
        if mode == 4:
            nlp_model = BertProcessor(requirement_df)
        nlp_model.prepare()
        return nlp_model

    @staticmethod
    def init_clustering(mode, requirement_df, vector_df):
        cluster_model = None
        if requirement_df.empty:
            return cluster_model
        if mode == 0:
            cluster_model = KmeansProcessor(requirement_df, vector_df)
        elif mode == 1:
            cluster_model = EMProcessor(requirement_df, vector_df)
        elif mode == 2:
            cluster_model = AgglomerativeProcessor(requirement_df, vector_df, 'average')
        elif mode == 3:
            cluster_model = AgglomerativeProcessor(requirement_df, vector_df, 'ward')
        elif mode == 4:
            cluster_model = AgglomerativeProcessor(requirement_df, vector_df, 'complete')
        elif mode == 5:
            cluster_model = AgglomerativeProcessor(requirement_df, vector_df, 'single')
        elif mode == 6:
            cluster_model = DbscanProcessor(requirement_df, vector_df)
        cluster_model.prepare()
        return cluster_model
