import os

from rqadviser.view.main_view import MainView
from rqadviser.controller.controller_csv import ControllerCsv
from rqadviser.controller.controller_settings import ControllerSettings
from rqadviser.controller.controller_single_check import ControllerSingleCheck
from rqadviser.model.model_main import ModelMain


class ControllerMain:
    __model: ModelMain

    def __init__(self, model):
        self.__model = model

        self.__csv_controller = ControllerCsv()
        self.__setting_controller = ControllerSettings()
        self.__single_check_controller = ControllerSingleCheck()

        self.__view = MainView(self, self.__model)

        self.__model.data_frame.df_signal.signal.connect(self.__view.df_changed_slot)
        self.__model.cluster.cluster_signal.signal.connect(self.__view.single_check_complete)

        self.__view.show()

    def file_chosen_slot(self, file_name):
        self.__create_project(file_name, self.__model.settings.saves_path)
        self.__parse_data_frame()

    def __create_project(self, file_name, root):
        project_name = self.__setting_controller.create_project(file_name, root)
        self.__model.settings.project_name = project_name

    def __parse_data_frame(self):
        file_path = os.path.join(self.__model.settings.saves_path, self.__model.settings.project_name, 'data.csv')
        new_df, old_df = self.__csv_controller.parse_csv(file_path)
        self.__model.data_frame.df = old_df
        self.__model.data_frame.prepared_df = new_df

    def check_single_requirement_slot(self, cluster_mode, nlp_mode, requirement_id):
        if nlp_mode == 0:
            if self.__model.nlp.cosine is None:
                nlp_model = self.__single_check_controller.init_nlp_model(nlp_mode, self.__model.data_frame.prepared_df)
                self.__model.nlp.cosine = nlp_model
            else:
                nlp_model = self.__model.nlp.cosine
        elif nlp_mode == 1:
            if self.__model.nlp.tfidf is None:
                nlp_model = self.__single_check_controller.init_nlp_model(nlp_mode, self.__model.data_frame.prepared_df)
                self.__model.nlp.tfidf = nlp_model
            else:
                nlp_model = self.__model.nlp.tfidf
        elif nlp_mode == 2:
            if self.__model.nlp.doc2vec_dm is None:
                nlp_model = self.__single_check_controller.init_nlp_model(nlp_mode, self.__model.data_frame.prepared_df)
                self.__model.nlp.doc2vec_dm = nlp_model
            else:
                nlp_model = self.__model.nlp.doc2vec_dm
        elif nlp_mode == 3:
            if self.__model.nlp.doc2vec_dbow is None:
                nlp_model = self.__single_check_controller.init_nlp_model(nlp_mode, self.__model.data_frame.prepared_df)
                self.__model.nlp.doc2vec_dbow = nlp_model
            else:
                nlp_model = self.__model.nlp.doc2vec_dbow
        else:
            nlp_model = None

        cluster_model = self.__single_check_controller.init_clustering(cluster_mode,
                                                                       self.__model.data_frame.df,
                                                                       nlp_model.conv_df)
        cluster = cluster_model.get_nearest(requirement_id)
        self.__model.cluster.requirements_cluster = cluster

