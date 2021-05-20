"""
Контроллер инициализации моделей кластеризации и преобразования текста в вектора в зависимости от выбранного режима
"""
import pandas as pd

from rqadviser.clustering.agglomerative_processor import AgglomerativeProcessor
from rqadviser.clustering.dbscan_processor import DbscanProcessor
from rqadviser.clustering.em_processor import EMProcessor
from rqadviser.clustering.kmeans_processor import KmeansProcessor
from rqadviser.nlp.bert_processor import BertProcessor
from rqadviser.nlp.cosine_processor import CosineProcessor
from rqadviser.nlp.doc2vec_processor import Doc2VecProcessor
from rqadviser.nlp.tfidf_processor import TfidfProcessor


class ControllerInitModel:
    """
    Контроллер инициализации кластеризации и преобразования текста в вектора в зависимости от выбранного режима
    """
    @staticmethod
    def init_nlp_model(mode: int, requirement_df: pd.DataFrame):
        """
        :param mode: Тип модели преобразования текста в вектора (0-4)
        :param requirement_df: Спецификация требований в виде списка предложений
        :return: Инициализированная модель преобразования текста в вектора
        """
        nlp_model = None
        if requirement_df.empty:
            return nlp_model
        if mode == 0:
            nlp_model = CosineProcessor(requirement_df)
        if mode == 1:
            nlp_model = TfidfProcessor(requirement_df)
        if mode == 2:
            nlp_model = Doc2VecProcessor(requirement_df, mode="dm")
        if mode == 3:
            nlp_model = Doc2VecProcessor(requirement_df, mode="dbow")
        if mode == 4:
            nlp_model = BertProcessor(requirement_df)
        nlp_model.prepare()
        return nlp_model

    @staticmethod
    def init_clustering(mode: int, requirement_df: pd.DataFrame, vector_df: pd.DataFrame):
        """
        :param mode: Тип модели кластеризации (0-4)
        :param requirement_df: Спецификация требований в виде списка предложений
        :param vector_df: Спецификация требований в виде списка векторов
        :return: Инициализированная модель кластеризации
        """
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
