# -*- encoding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    log_utils.py
   Description :
   Author :       Wings DH
   Time：         2020/3/29 10:47
-------------------------------------------------
   Change Activity:
                   2020/3/29: Create
-------------------------------------------------
"""
try:
    from loguru import logger
except ModuleNotFoundError:
    import logging as logger
