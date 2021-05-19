import pandas as pd
import string
import pymorphy2
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


class DataProcessor:
    def __init__(self):
        super().__init__()
        self._df = None
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
        self._df = pd.read_csv(filename, sep=sep, encoding='utf-8')

    def _tokenize(self):
        """
        Удаляет союзы, предлоги, пунктуациоанные знаки и пр., разбивает на слова, приводит к нижнему регистру и к
        нормальной форме слова
        """
        self._df["Requirement"] = self._df["Requirement"].str.replace('[{}]'.format(string.punctuation), '')
        self._df["Requirement"] = self._df["Requirement"].str.lower()
        self._df["Requirement"] = self._df["Requirement"].str.split(" ", expand=False)
        stop_word = stopwords.words('russian')
        self._df["Requirement"] = self._df.apply(lambda row: [self._morph.parse(word)[0].normal_form for word in
                                                                row["Requirement"] if word not in stop_word and
                                                                word != "" and not str(word).isdigit()], axis=1)

    @property
    def df(self):
        return self._df
