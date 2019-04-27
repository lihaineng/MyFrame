"""
Item模块: 用于封装提取出来的数据
"""

class Item(object):

    def __init__(self, data):
        # data爬虫提取字典数据/其他数据
        self.__data = data

    @property # 让该方法变成只读属性; 使用方式: item = Item({}); item.data
    def data(self):
        return self.__data

