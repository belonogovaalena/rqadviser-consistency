import os
import pickle


class ControllerDownload:
    def __init__(self):
        self.__project_path = ""

    def set_project_path(self, path):
        self.__project_path = path

    def __get_pickle_path(self, name):
        return os.path.join(self.__project_path, "{0}.pkl".format(name))

    def __check_model_exists(self, model):
        path = self.__get_pickle_path(model)
        return os.path.exists(path)

    def download_model_if_exists(self, model):
        if not self.__check_model_exists(model):
            return None
        else:
            path = self.__get_pickle_path(model)
            try:
                with open(path, 'rb') as f:
                    result = pickle.load(f)
            except pickle.PickleError as e:
                print(e)
                return None
            return result

