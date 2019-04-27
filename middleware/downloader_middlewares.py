"""
下载器中间: 在引擎和下载器之间, 用于处理请求和响应的
"""

class DownloaderMiddleware(object):

    def process_request(self, request):
        """
        处理请求
        :param request: 请求对象
        :return:
        """
        print('DownloaderMiddleware-process_request_{}'.format(request.url))

        return request

    def process_response(self, response):
        """
        用于处理响应的
        :param response:
        :return:
        """
        print('DownloaderMiddleware-process_response_{}'.format(response.url))

        return response
