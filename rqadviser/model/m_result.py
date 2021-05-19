from rqadviser.signals.signals import ClusterFound
from rqadviser.signals.signals import InaccuraciesFound


class ModelResult:
    def __init__(self):
        self.cluster_signal = ClusterFound()
        self.inaccuracies_signal = InaccuraciesFound()
        self._requirements_cluster = None
        self._inaccuracies = None

    @property
    def requirements_cluster(self):
        return self._requirements_cluster

    @requirements_cluster.setter
    def requirements_cluster(self, value):
        self._requirements_cluster = value
        self.cluster_signal.signal.emit()

    @property
    def inaccuracies(self):
        return self._inaccuracies

    @inaccuracies.setter
    def inaccuracies(self, value):
        self._inaccuracies = value
        self.inaccuracies_signal.signal.emit()

    def __repr__(self):
        return f"ModelResult: [requirements_cluster: {self._requirements_cluster}, " \
               f"inaccuracies: {self._inaccuracies}]"
