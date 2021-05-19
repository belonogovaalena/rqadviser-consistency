import logging
import os
import pickle  # noqa: S403


class ControllerSave:
    def __init__(self):
        self.__project_path = ""

    def set_project_path(self, path):
        self.__project_path = path

    def __get_pickle_path(self, name):
        return os.path.join(self.__project_path, "{0}.pkl".format(name))

    def save_to_file(self, model, name):
        file_path = self.__get_pickle_path(name)
        try:
            with open(file_path, 'wb') as output:
                pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)
            return True
        except pickle.PickleError as e:
            logger.error(e)
            return False


logger = logging.getLogger("rqadviser")
