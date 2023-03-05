# -*- coding: utf-8 -*-


from jinja2.exceptions import FilterArgumentError
from jinja2._compat import string_types


def sort_dict(value, case_sensitive=False, by='key', reverse=False, index=0):
    """
    字典排序
    :param value: 字典对象
    :param case_sensitive: 是否大小写敏感
    :param by: 排序对象
    :param reverse: 排序方式（正序：True、倒序：False）
    :param index: 索引号（此处针对 value 为 list 情况下可根据 list 的某一 index 排序）
    :return:
    """
    if by == 'key':
        pos = 0
    elif by == 'value':
        pos = 1
    else:
        raise FilterArgumentError('You can only sort by either "key" or "value"')
    def sort_func(item):
        value = item[pos]
        if index:
            try:
                value = value[index]
            except:
                pass
        if isinstance(value, string_types) and not case_sensitive:
            value = value.lower()
        return value

    return sorted(value.items(), key=sort_func, reverse=reverse)
