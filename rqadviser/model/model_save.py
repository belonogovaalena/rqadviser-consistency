from rqadviser.signals.saved_project import SavedProject


class ModelSave:
    def __init__(self):
        self.__save_state = True
        self.saved_signal = SavedProject()

    @property
    def save_state(self):
        return self.__save_state

    @save_state.setter
    def save_state(self, value):
        self.__save_state = value
        self.saved_signal.signal.emit()
