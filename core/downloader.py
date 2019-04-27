import requests
from ..http.response import Response
"""
下载器模块: 发送请求, 获取响应数据
"""

class Downloader(object):

    def get_response(self, request):
        """根据请求, 获取响应数据"""

        if request.method.upper() == 'GET':
            # 如果是GET请求, 就是requests, 发送GET请求获取数据
            resp = requests.get(request.url, params=request.params, headers=request.headers)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, data=request.data, headers=request.headers)
        else:
            raise Exception('暂时只支持GET和POST请求!!')

        # 为了让代码有更好可以扩展性, 需要使用我们自定义的响应对象, 对requests中响应对象进行封装
        return  Response(resp.url, status_code=resp.status_code, headers=resp.headers, body=resp.content)


