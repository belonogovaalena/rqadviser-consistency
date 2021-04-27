import pandas as pd
from rqadviser.nlp.nlp_abstract import NlpAbstract


class CosineProcessor(NlpAbstract):
    def __init__(self, df):
        super().__init__(df)
        self.__word_cloud = set()

    def prepare(self):
        """
        Расчитывает дополнительные данные для работы с методом на основе косинусного расстояния
        """
        self.__compute_word_cloud()
        self.__compute_word_matrix()

    def __compute_word_cloud(self):
        """
        Вычисляет облако слов
        """
        self._df.apply(lambda row: self.__word_cloud.update(set((row["Requirement"]))), axis=1)
        sorted(self.__word_cloud)

    def __compute_word_matrix(self):
        """
        Вычисляет матрицу присутствия слов в датафрейме
        """
        self._conv_df = pd.DataFrame(columns={"Vector"})
        for _, row in self._df["Requirement"].items():
            self._conv_df = self._conv_df.append(self.__get_row(row), ignore_index=True)
        self._conv_df['ID'] = self._df['ID'].to_numpy()

    def __get_row(self, row: pd.DataFrame):
        """
        Преборазует предложение в вектор в пространстве облака слов
        :param row: Предложение из dataframe
        :return: Вектор в пространстве облака слов
        """
        word_vector = list()
        value = 0
        for word in self.__word_cloud:
            if word in row:
                value = 1
            else:
                value = 0
            word_vector.append(value)
        return {"Vector": word_vector}

