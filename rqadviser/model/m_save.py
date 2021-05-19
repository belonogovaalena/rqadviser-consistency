from rqadviser.signals.saved_project import SavedProject


class ModelSave:
    def __init__(self):
        self._save_state = True
        self.saved_signal = SavedProject()

    @property
    def save_state(self):
        return self._save_state

    @save_state.setter
    def save_state(self, value):
        self._save_state = value
        self.saved_signal.signal.emit()
