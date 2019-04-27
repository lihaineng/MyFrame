from datetime import datetime

from ..middleware.downloader_middlewares import DownloaderMiddleware
from ..middleware.spider_middlewares import SpiderMiddleware
from .spider import Spider
from .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline
from ..http.request import Request
# 导入日志对象
from ..utils.log import logger

"""
引擎模块: 调度各个模块, 实现各个模块间数据传递
实现思路:
1. 初始爬虫, 调度器, 下载器, 管道
2. 提供一个外界启动爬虫框架的方法
3. 提供一个私有启动方法, 用于封装框架运行的核心逻辑


4. 在需要记录日志的使用导致log.py中日志对象, 记录日志就可以了
   4.1 在引擎中我们统计一下, 引擎开始时间, 结束时间, 总耗时; 在start方法中
"""

class Engine(object):

    def __init__(self):
        """
        1. 初始爬虫, 调度器, 下载器, 管道
        """
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline() #
        # 在init方法, 创建爬虫中间件 和下载器中间件
        self.spider_middleware = SpiderMiddleware()
        self.downloader_middware = DownloaderMiddleware()

    def start(self):
        """
            2. 提供一个外界启动爬虫框架的方法
        """
        # 开始时间
        start = datetime.now()
        logger.info('开始运行的时间: {}'.format(start))
        self.__start()
        # 结束时间
        end = datetime.now()
        logger.info('结束运行de 时间: {}'.format(end))
        # 总耗时
        logger.info('总耗时: {}秒'.format((end-start).total_seconds()))

    def __start(self):
        """
        3. 提供一个私有启动方法, 用于封装框架运行的核心逻辑
        :return:
        """
        # 1. 调用爬虫start_requests,获取起始请求
        request = self.spider.start_request()

        # 调用爬虫中间件的process_request来处理请求
        request = self.spider_middleware.process_request(request)

        # 2. 调用调度器的add_request方法, 把请求放到调度器中
        self.scheduler.add_request(request)
        # 3. 调用调度器的get_request方法, 获取请求对象
        request = self.scheduler.get_request()

        # 在把请求交个下载器之前, 使用下载中间件, 对请求进行处理
        request = self.downloader_middware.process_request(request)

        # 4. 调用下载器的get_response方法, 根据请求获取响应数据
        response = self.downloader.get_response(request)

        # 调用下载器中间的prcess_response方法, 对响应进行处理
        response = self.downloader_middware.process_response(response)

        # 在把响应数据交给爬虫之前, 先经过爬虫中间进行处理
        response = self.spider_middleware.process_response(response)

        # 5. 调用爬虫模块的parse函数, 解析响应数据, 获取解析结果
        result = self.spider.parse(response)

        # 如果处理的结果是请求, 就添加到调度器中
        # isinstance: 判断 result 是不是 Request 实例对象
        if isinstance(result, Request):
            # 如果是解析结果是请求, 就使用爬虫中间件对请求进行处理
            result = self.spider_middleware.process_request(result)
            self.scheduler.add_request(result)
        else:
            # 否则, 把处理结果交给管道
            self.pipeline.process_item(result, self.spider)


