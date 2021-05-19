import os

from rqadviser.view.main_view import MainView
from rqadviser.controller.ctrl_process_csv import ControllerProcessCsv
from rqadviser.controller.ctrl_settings import ControllerSettings
from rqadviser.controller.ctrl_init_model import ControllerInitModel
from rqadviser.controller.ctrl_save import ControllerSave
from rqadviser.model.model_main import ModelMain
from rqadviser.controller.ctrl_download import ControllerDownload


class ControllerMain:
    _model: ModelMain

    def __init__(self, model):
        self._model = model

        self._view = MainView(self, self._model)

        self._ctrl_process_csv = ControllerProcessCsv()
        self._ctrl_settings = ControllerSettings()
        self._ctrl_init_model = ControllerInitModel()
        self._ctrl_save = ControllerSave()
        self._ctrl_download = ControllerDownload()

        self._model.result.inaccuracies_signal.signal.connect(self._view.full_check_complete)
        self._model.data_frame.df_signal.signal.connect(self._view.df_changed_slot)
        self._model.result.cluster_signal.signal.connect(self._view.single_check_complete)
        self._model.save.saved_signal.signal.connect(self._view.project_saved)

        self._view.show()

    def req_file_chosen_slot(self, csv_file_path):
        root_path = self._ctrl_settings.init_root_path()
        if root_path:
            self._model.settings.saves_path = root_path
            self._create_project(csv_file_path, self._model.settings.saves_path)
            self._parse_data_frame()
        else:
            print("Ошибка инициализации пути проекта")

    def _create_project(self, csv_file_path, root_path):
        project_name = self._ctrl_settings.create_project(csv_file_path, root_path)
        if project_name:
            self._model.settings.project_name = project_name

    def _parse_data_frame(self):
        file_path = os.path.join(self._model.settings.saves_path, self._model.settings.project_name, 'data.csv')
        norm_req_df = self._ctrl_process_csv.parse_csv_normalized(file_path)
        req_df = self._ctrl_process_csv.parse_csv(file_path)
        if not norm_req_df.empty and not req_df.empty:
            self._model.data_frame.df = req_df
            self._model.data_frame.prepared_df = norm_req_df
        else:
            print("Ошибка обработки данных CSV")

    def check_single_requirement_slot(self, cluster_mode, nlp_mode, requirement_id):
        nlp_model = self._init_nlp_model(nlp_mode)
        if nlp_model:
            cluster_model = self._ctrl_init_model.init_clustering(cluster_mode, self._model.data_frame.df, nlp_model.conv_df)
            if cluster_model:
                cluster = cluster_model.get_nearest(requirement_id)
                self._model.result.requirements_cluster = cluster
            else:
                print("Ошибка инициализации кластеризационной модели")
        else:
            print("Ошибки иницализаци NLP модели")

    def check_full_requirements_slot(self, cluster_mode, nlp_mode, measure):
        nlp_model = self._init_nlp_model(nlp_mode)
        if nlp_model:
            cluster_model = self._ctrl_init_model.init_clustering(cluster_mode, self._model.data_frame.df,
                                                                  nlp_model.conv_df)
            if cluster_model:
                inaccuracies = cluster_model.get_inaccuracies(measure)
                self._model.result.inaccuracies = inaccuracies
            else:
                print("Ошибка инициализации кластеризационной модели")
        else:
            print("Ошибки иницализаци NLP модели")

    def _init_nlp_model(self, nlp_mode):
        if nlp_mode == 0:
            if self._model.nlp.cosine is None:
                nlp_model = self._ctrl_init_model.init_nlp_model(nlp_mode, self._model.data_frame.prepared_df)
                self._model.nlp.cosine = nlp_model
            else:
                nlp_model = self._model.nlp.cosine
        elif nlp_mode == 1:
            if self._model.nlp.tfidf is None:
                nlp_model = self._ctrl_init_model.init_nlp_model(nlp_mode, self._model.data_frame.prepared_df)
                self._model.nlp.tfidf = nlp_model
            else:
                nlp_model = self._model.nlp.tfidf
        elif nlp_mode == 2:
            if self._model.nlp.doc2vec_dm is None:
                nlp_model = self._ctrl_init_model.init_nlp_model(nlp_mode, self._model.data_frame.df)
                self._model.nlp.doc2vec_dm = nlp_model
            else:
                nlp_model = self._model.nlp.doc2vec_dm
        elif nlp_mode == 3:
            if self._model.nlp.doc2vec_dbow is None:
                nlp_model = self._ctrl_init_model.init_nlp_model(nlp_mode, self._model.data_frame.df)
                self._model.nlp.doc2vec_dbow = nlp_model
            else:
                nlp_model = self._model.nlp.doc2vec_dbow
        elif nlp_mode == 4:
            if self._model.nlp.bert is None:
                nlp_model = self._ctrl_init_model.init_nlp_model(nlp_mode, self._model.data_frame.df)
                self._model.nlp.bert = nlp_model
            else:
                nlp_model = self._model.nlp.bert
        else:
            nlp_model = None
        return nlp_model

    def save_project_slot(self):
        state = True
        self._ctrl_save.set_project_path(
            os.path.join(self._model.settings.saves_path, self._model.settings.project_name))
        if self._model.nlp.cosine is not None:
            state = state and self._ctrl_save.save_to_file(self._model.nlp.cosine, "cosine")
        if self._model.nlp.tfidf is not None:
            state = state and self._ctrl_save.save_to_file(self._model.nlp.tfidf, "tfidf")
        if self._model.nlp.doc2vec_dbow is not None:
            state = state and self._ctrl_save.save_to_file(self._model.nlp.doc2vec_dbow, "doc2vec_dbow")
        if self._model.nlp.doc2vec_dm is not None:
            state = state and self._ctrl_save.save_to_file(self._model.nlp.doc2vec_dm, "doc2vec_dm")
        if self._model.nlp.bert is not None:
            state = state and self._ctrl_save.save_to_file(self._model.nlp.bert, "bert")
        self._model.save.save_state = state

    def download_project_slot(self, file_path):
        root = os.path.dirname(file_path)
        if root:
            project_name = str(file_path).split("/")[-1]
            self._model.settings.project_name = project_name
            self._model.settings.saves_path = root
            self._parse_data_frame()
            self._ctrl_download.set_project_path(
                os.path.join(self._model.settings.saves_path, self._model.settings.project_name))

            self._model.nlp.cosine = self._ctrl_download.download_model_if_exists("cosine")
            self._model.nlp.tfidf = self._ctrl_download.download_model_if_exists("tfidf")
            self._model.nlp.doc2vec_dm = self._ctrl_download.download_model_if_exists("doc2vec_dm")
            self._model.nlp.doc2vec_dbow = self._ctrl_download.download_model_if_exists("doc2vec_dbow")
            self._model.nlp.bert = self._ctrl_download.download_model_if_exists("bert")
        else:
            print("Ошибка определения пути проекта")
