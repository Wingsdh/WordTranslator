# -*- encoding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    base_dict.py
   Description :
   Author :       Wings DH
   Time：         2020/3/28 5:50 下午
-------------------------------------------------
   Change Activity:
                   2020/3/28: Create
-------------------------------------------------
"""
from abc import ABC, abstractmethod


class WordItem(ABC):
    @property
    def word(self):
        """
        :return:  str, 单词
        """
        return self._word

    @property
    def cn_paraphrase(self):
        """
        :return:  str, 中文解释
        """
        return self._cn_paraphrase

    @property
    def en_paraphrase(self):
        """
        :return:  str, 英文解释
        """
        return self._en_paraphrase

    def __init__(self, word, cn_paraphrase, en_paraphrase):
        """
        Args:
            :param word: str, 单词
            :param cn_paraphrase: str, 中文解释
            :param en_paraphrase: str, 英文解释
        """
        self._word = word
        self._cn_paraphrase = cn_paraphrase
        self._en_paraphrase = en_paraphrase


class WordRecord(ABC):

    @classmethod
    def create(cls):
        return cls()


class BaseDict(ABC):

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs):
        """
        构造方法
        :return:BaseDict，BaseDict实例
        """
        pass

    @abstractmethod
    def word_2_record(self, word):
        """
        :param word: str, 需要查询的单词
        :return: WordRecord, word对应的单词记录
        """
        pass
