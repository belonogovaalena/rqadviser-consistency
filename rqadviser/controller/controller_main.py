from rqadviser.view.main_view import MainView


class ControllerMain:
    def __init__(self, model):
        self.__model = model
        self.__view = MainView(self, self.__model)
        self.__view.show()
