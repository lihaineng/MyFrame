# scrapy_plus/utils/log.py
import logging
import sys

from spiderframe.conf.settings import DEFAULT_LOG_FMT, DEFAULT_LOG_FILENAME, DEFAULT_LOG_LEVEL, DEFUALT_LOG_DATEFMT


class Logger(object):

    def __init__(self):
        # 1. 获取一个logger对象
        self._logger = logging.getLogger()
        # 2. 设置format对象
        self.formatter = logging.Formatter(fmt=DEFAULT_LOG_FMT,datefmt=DEFUALT_LOG_DATEFMT)
        # 3. 设置日志输出
        # 3.1 设置文件日志模式, 添加一个日志的处理方式, 用于把日志信息以指定格式写入到文件中
        self._logger.addHandler(self._get_file_handler(DEFAULT_LOG_FILENAME))
        # 3.2 设置终端日志模式 用于把日志信息以指定格式打印控制台上
        self._logger.addHandler(self._get_console_handler())
        # 4. 设置日志等级
        self._logger.setLevel(DEFAULT_LOG_LEVEL)

    def _get_file_handler(self, filename):
        '''返回一个文件日志handler'''
        # 1. 获取一个文件日志handler, 用于把日志信息以utf-8的编码, 写入到指定文件汇总
        filehandler = logging.FileHandler(filename=filename,encoding="utf-8")
        # 2. 设置日志格式
        filehandler.setFormatter(self.formatter)
        # 3. 返回
        return filehandler

    def _get_console_handler(self):
        '''返回一个输出到终端日志handler'''
        # 1. 获取一个输出到终端日志handler
        # sys.stdout: 系统标准输出流, 用于把数据输出到控制台上
        console_handler = logging.StreamHandler(sys.stdout)
        # 2. 设置日志格式
        console_handler.setFormatter(self.formatter)
        # 3. 返回handler
        return console_handler

    @property
    def logger(self):
        return self._logger

# 初始化并配一个logger对象，达到单例的
# 使用时，直接导入logger就可以使用
logger = Logger().logger
