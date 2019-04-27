from queue import Queue

"""
调度器模块: 1. 缓冲请求, 2 请求去重

步骤:
 1. 初始一个队列, 用于缓存请求
 2. 提供添加请求的方法
 3. 提取获取请求的方法
 4. 请求去重的方法
"""

class Scheduler(object):

    def __init__(self):
        #  1. 初始一个队列, 用于缓存请求
        self.queue = Queue()

    def add_request(self, request):
        """
         2. 提供添加请求的方法
        :param request: 请求对象
        """
        self.queue.put(request)

    def get_request(self):
        """
         3. 提取获取请求的方法
        :return: 请求对象
        """
        request = self.queue.get()
        return request

    def request_seen(self, request):
        """
         4. 请求去重的方法
        :param request:
        :return: 如果返回True , 说明该请求重复了, 否则说明该请求是新的请求
        """
        # todo
        pass
