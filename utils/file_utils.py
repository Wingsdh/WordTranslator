# -*- encoding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    file_utils.py
   Description :
   Author :       Wings DH
   Time：         2020/3/29 9:02
-------------------------------------------------
   Change Activity:
                   2020/3/29: Create
-------------------------------------------------
"""
import os


def list_all_file(dir_path, *, recursive=False, check_func=None):
    """
    列出目录中的所有合法文件路径
    :param dir_path: 目标路径
    :param recursive: bool, optional, 是否递归搜索文件
    :param check_func: func, optional, 检查文件名是否满足要求
    :return: list, 所有文件路径
    """
    if not os.path.exists(dir_path):
        return []

    paths = os.listdir(dir_path)

    file_names = []
    for p in paths:
        abs_p = os.path.join(dir_path, p)
        if os.path.isdir(abs_p):
            if not recursive:
                continue

            sub_files = list_all_file(abs_p, recursive=recursive, check_func=check_func)
            if len(sub_files) > 0:
                file_names.extend(sub_files)
        else:
            if check_func is None or check_func(abs_p):
                file_names.append(abs_p)
    return file_names
