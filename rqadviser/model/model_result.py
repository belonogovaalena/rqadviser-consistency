from rqadviser.signals.cluster_found import ClusterFound
from rqadviser.signals.inaccuracies_found import InaccuraciesFound


class ModelResult:
    def __init__(self):
        self.cluster_signal = ClusterFound()
        self.inaccuracies_signal = InaccuraciesFound()
        self.__requirements_cluster = None
        self.__inaccuracies = None

    @property
    def requirements_cluster(self):
        return self.__requirements_cluster

    @requirements_cluster.setter
    def requirements_cluster(self, value):
        self.__requirements_cluster = value
        self.cluster_signal.signal.emit()

    @property
    def inaccuracies(self):
        return self.__inaccuracies

    @inaccuracies.setter
    def inaccuracies(self, value):
        self.__inaccuracies = value
        self.inaccuracies_signal.signal.emit()
