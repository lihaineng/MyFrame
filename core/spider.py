from ..http.request import Request
from ..http.item import Item


class Spider(object):
    # 起始URL
    start_url = 'http://www.baidu.com'

    def start_request(self, start_url):
        """
        1. 准备起始请求
        :return:
        """
        # 根据起始URL, 构建一个请求对象, 交给引擎
        return Request(self.start_url)

    def parse(self, response):
        """
        2. 解析响应数据 (1 提取数据, 2 提取URL)
        """
        print(response.body.decode())

        return Item(response.url)