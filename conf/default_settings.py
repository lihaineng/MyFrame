"""
用于定义框架中一些默认配置信息
"""

import logging

# 默认的配置
DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称

# 11. 3.1. 修改default_settings.py, 增加爬虫, 管道, 下载器中间件, 爬虫中间件的默认配置;
# 配置和开启爬虫
SPIDERS = []

# 配置和开启管道
PIPELINES = []

# 配置和开启下载器中间件
DOWNLOADER_MIDDLEWARES = []

# 配置和开启爬虫中间件
SPIDER_MIDDLEWARES = []