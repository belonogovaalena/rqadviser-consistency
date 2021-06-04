"""
Проверка модели хранения обученных моделей
"""
import unittest

from rqadviser.model.m_nlp import ModelNlp


class TestModelNlp(unittest.TestCase):
    """
    Проверка модели хранения обученных моделей
    """
    @staticmethod
    def test_1_save_and_get():
        """
        Тест получения и сохранения состояния модели
        """
        model = ModelNlp()
        model.bert = 1
        model.tfidf = 2
        model.doc2vec_dm = 3
        model.doc2vec_dbow = 4
        model.cosine = 5
        repr(model)
        assert model.bert == 1
        assert model.tfidf == 2
        assert model.doc2vec_dm == 3
        assert model.doc2vec_dbow == 4
        assert model.cosine == 5
