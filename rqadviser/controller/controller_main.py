from rqadviser.view.main_view import MainView
from rqadviser.controller.controller_csv import ControllerCsv
from rqadviser.controller.controller_settings import ControllerSettings
from rqadviser.model.model_main import ModelMain


class ControllerMain:
    __model: ModelMain

    def __init__(self, model):
        self.__model = model

        self.__csv_controller = ControllerCsv()
        self.__setting_controller = ControllerSettings()

        self.__view = MainView(self, self.__model)

        self.__model.data_frame.df_signal.signal.connect(self.__view.df_changed_slot)
        self.__view.show()

    def file_chosen_slot(self, file_name):
        self.__create_project(file_name, self.__model.settings.saves_path)
        self.__parse_data_frame(file_name)

    def __create_project(self, file_name, root):
        project_name = self.__setting_controller.create_project(file_name, root)
        self.__model.settings.project_name = project_name

    def __parse_data_frame(self, file_name):
        df = self.__csv_controller.parse_csv(file_name)
        self.__model.data_frame.df = df
