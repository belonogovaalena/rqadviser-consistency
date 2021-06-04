"""
Проверка мастер-контроллера
"""
import os
import shutil
import unittest
from unittest import mock

import pandas as pd

from rqadviser.clustering.kmeans_processor import KmeansProcessor
from rqadviser.controller.ctrl_main import ControllerMain
from rqadviser.controller.tests.common import OUTPUT_PATH, TEST_CSV_PATH
from rqadviser.model.m_main import ModelMain


class TestControllerMain(unittest.TestCase):
    """
    Проверка мастер-контроллера
    """
    @staticmethod
    @mock.patch('rqadviser.controller.ctrl_main.ControllerMain._setup_view')
    def test_1_create_project(_):
        """
        Проверка создания проекта из файла спецификации
        """
        model = ModelMain()
        ctrl = ControllerMain(model)
        ctrl.req_file_chosen_slot(TEST_CSV_PATH)
        assert model.data_frame

    @staticmethod
    @mock.patch('rqadviser.controller.ctrl_main.ControllerMain._setup_view')
    @mock.patch('rqadviser.controller.ctrl_init_model.ControllerInitModel.prepare')
    @mock.patch('rqadviser.controller.ctrl_init_model.ControllerInitModel.init_clustering')
    def test_2_check(*args):
        """
        Проверка частичной и полной проверки спецификации
        """
        requirement_df = pd.read_csv(TEST_CSV_PATH)
        vector_df = pd.DataFrame([[0.9, 0.5, 0.6], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0],
                                  [0.6, 0.4, 0.6], [0.4, 0.6, 1.0], [1.0, 0.7, 1.0]])
        return_value = KmeansProcessor(requirement_df, vector_df)
        return_value.prepare()
        args[0].return_value = return_value
        model = ModelMain()
        model.data_frame.req_df = requirement_df
        model.data_frame.norm_req_df = requirement_df
        ctrl = ControllerMain(model)
        for i in range(5):
            for j in range(7):
                ctrl.check_single_requirement_slot(i, j, "R-0001")
                assert not model.result.requirements_cluster.empty
                ctrl.check_full_requirements_slot(i, j, 1.0)
                assert not model.result.inaccuracies.empty

    @staticmethod
    @mock.patch('rqadviser.controller.ctrl_main.ControllerMain._setup_view')
    def test_3_save(_):
        """
        Проверка сохранения
        """
        model = ModelMain()
        model.settings.root_path = OUTPUT_PATH
        model.settings.project_name = "test"
        os.mkdir(os.path.join(OUTPUT_PATH, "test"))
        shutil.copy(TEST_CSV_PATH, os.path.join(OUTPUT_PATH, "test", "data.csv"))
        model.nlp.tfidf = {"a": 1}
        model.nlp.cosine = {"b": 1}
        model.nlp.bert = {"c": 1}
        model.nlp.doc2vec_dm = {"d": 1}
        model.nlp.doc2vec_dbow = {"e": 1}
        ctrl = ControllerMain(model)
        ctrl.save_project_slot()
        assert model.save.save_state

    @staticmethod
    @mock.patch('rqadviser.controller.ctrl_main.ControllerMain._setup_view')
    def test_4_download(_):
        """
        Проверка загрузки
        """
        model = ModelMain()
        ctrl = ControllerMain(model)
        ctrl.download_project_slot(os.path.join(OUTPUT_PATH, "test"))
        assert model.nlp.bert and model.nlp.cosine and model.nlp.tfidf and model.nlp.doc2vec_dm \
               and model.nlp.doc2vec_dm

    @staticmethod
    def test_5_tear_down():
        """
        Очистка окружения: TODO сделать нормальные тесты через pytestfixture
        """
        project_path = os.path.join(OUTPUT_PATH, "test")
        files = [os.path.join(project_path, file) for file in os.listdir(project_path)]
        for file in files:
            os.remove(file)
        os.rmdir(project_path)
