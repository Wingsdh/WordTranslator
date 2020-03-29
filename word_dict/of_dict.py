# -*- encoding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    of_dict.py
   Description :
   Author :       Wings DH
   Time：         2020/3/29 8:51
-------------------------------------------------
   Change Activity:
                   2020/3/29: Create
-------------------------------------------------
"""
import os
import re
from utils.log_utils import logger
from utils.file_utils import list_all_file
from word_dict.base_dict import BaseDict, WordEntry, WordRecord


class OfDict(BaseDict):

    @classmethod
    def create(cls, *args, **kwargs):
        def parse_args():
            if len(args) > 0:
                _d_path = args[0]
            elif 'd_path' in kwargs:
                _d_path = kwargs['d_path']
            else:
                raise ValueError('Creating a OfDict need a d_path')

            if not os.path.exists(_d_path):
                raise FileNotFoundError('d_path <{}> must exist'.format(_d_path))

            return _d_path

        d_path = parse_args()

        return cls(d_path)

    def refer_to_word(self, word):
        pass

    def load_txt(self, f_path):
        logger.info('Loading from {}'.format(f_path))
        with open(f_path, 'r', encoding='gbk', errors='ignore') as fd:
            for idx, line in enumerate(fd):
                if idx > 1000:
                    print(idx, line)
                if idx > 1010:
                    break

    def __init__(self, d_path):
        self._word_2_record = {}
        f_paths = list_all_file(d_path, recursive=True, check_func=lambda x: x.endswith('txt'))
        for f_path in f_paths:
            self.load_txt(f_path)
