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


class WordEntry(ABC):
    """
    单词词条
    """

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
    """
    一个单词在词典中的记录, 包含若干词条
    """

    @property
    def word(self):
        """
        :return: str, 被描述的单词
        """
        return self._word

    @classmethod
    def create(cls, word):
        return cls(word)

    def __init__(self, word):
        self._items = []
        self._word = word

    def add_entry(self, word_entry):
        """
        新增单词词条
        :param word_entry: WordEntry, 需要新增的词条
        :return: None
        """

        if isinstance(word_entry, WordEntry):
            self._items.append(word_entry)
        else:
            raise ValueError('Only inst of WordEntry can be added but {}'.format(type(word_entry)))


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
    def refer_to_word(self, word):
        """
        :param word: str, 需要查询的单词
        :return: WordRecord, word对应的单词记录
        """
        pass
