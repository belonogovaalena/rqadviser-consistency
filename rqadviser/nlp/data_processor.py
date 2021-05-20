"""
Модуль лемматизации
"""
import string

import nltk
from nltk.corpus import stopwords

import pandas as pd

import pymorphy2

nltk.download('stopwords')


class DataProcessor:
    """
    Модуль лемматизации
    """
    def __init__(self):
        super().__init__()
        self._norm_df = None
        self._morph = pymorphy2.MorphAnalyzer()

    def prepare_unsupervised(self, file_name):
        """
        Подготавливает данные для машинного обучения без учителя
        """
        self._parse_csv(file_name)
        # приводим строки
        self._tokenize()

    def _parse_csv(self, filename: str, sep=","):
        """
        Загружает требования из файла
        :param filename: название файла в формате *.csv
        :param sep: разделитель в файле
        """
        self._norm_df = pd.read_csv(filename, sep=sep, encoding='utf-8')

    def _tokenize(self):
        """
        Удаляет союзы, предлоги, пунктуациоанные знаки и пр., разбивает на слова, приводит к нижнему регистру и к
        нормальной форме слова
        """
        self._norm_df["Requirement"] = self._norm_df["Requirement"].str.replace('[{}]'.format(string.punctuation), '')
        self._norm_df["Requirement"] = self._norm_df["Requirement"].str.lower()
        self._norm_df["Requirement"] = self._norm_df["Requirement"].str.split(" ", expand=False)
        stop_word = stopwords.words('russian')
        self._norm_df["Requirement"] = self._norm_df.apply(lambda row: [self._morph.parse(word)[0].normal_form for
                                                                        word in row["Requirement"] if word not in
                                                                        stop_word and word != "" and not str(word).
                                                           isdigit()], axis=1)

    @property
    def norm_df(self):
        """
        :return: Нормализированный датафрейм
        """
        return self._norm_df
