from rqadviser.signals.cluster_found import ClusterFound


class ModelCluster:
    def __init__(self):
        self.__requirements_cluster = None
        self.cluster_signal = ClusterFound()

    @property
    def requirements_cluster(self):
        return self.__requirements_cluster

    @requirements_cluster.setter
    def requirements_cluster(self, value):
        self.__requirements_cluster = value
        self.cluster_signal.signal.emit()
