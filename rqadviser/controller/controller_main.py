from rqadviser.view.main_view import MainView
from rqadviser.controller.controller_csv import ControllerCsv
from rqadviser.model.model_main import ModelMain


class ControllerMain:
    __model: ModelMain

    def __init__(self, model):
        self.__model = model

        self.__csv = ControllerCsv()

        self.__view = MainView(self, self.__model)

        self.__model.data_frame.df_signal.signal.connect(self.__view.df_changed_slot)
        self.__view.show()

    def file_chosen_slot(self, file_name):
        df = self.__csv.parse_csv(file_name)
        self.__model.data_frame.df = df
