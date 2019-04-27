"""
管道模块: 处理提取出来的数据
"""

class Pipeline(object):

    def process_item(self, item, spider):
        """
        处理数据
        :param item: 提取出来的数据
        :param spider:  数据对应爬虫
        :return:  item
        """
        # 打印数据
        print(item.data)

        return item