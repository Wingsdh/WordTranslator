# -*- encoding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    test_of_dict.py
   Description :
   Author :       Wings DH
   Time：         2020/3/29 10:34
-------------------------------------------------
   Change Activity:
                   2020/3/29: Create
-------------------------------------------------
"""

import sys
import unittest
import ddt

from word_dict.of_dict import OfDict


@ddt.ddt
class OfDictTestCase(unittest.TestCase):
    """
    OfDict 测试用例
    """
    build_data = {
        '../../../Data/Oxford_dict'
    }

    @ddt.data(*build_data)
    def test_create(self, test_data):
        print('Create OfDict from {}'.format(test_data))
        of_dict = OfDict.create(test_data)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    unittest.main()


if __name__ == "__main__":
    sys.exit(main())
