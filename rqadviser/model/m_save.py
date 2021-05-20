"""
Модель состояния сохранения
"""
from rqadviser.signals.signals import SavedProject


class ModelSave:
    """
    Модель состояния сохранения
    """
    def __init__(self):
        self._save_state = True
        self.saved_signal = SavedProject()

    @property
    def save_state(self) -> bool:
        """
        :return: Состояние сохранения
        """
        return self._save_state

    @save_state.setter
    def save_state(self, value: bool):
        """
        :param value: Состояние сохранения
        """
        self._save_state = value
        self.saved_signal.signal.emit()

    def __repr__(self):
        return f"ModelSave: [save_state: {self._save_state}]"
