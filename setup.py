from os.path import dirname, join
# from pip.req import parse_requirements
# 等价: from setuptools import  find_packages,setup
from setuptools import (
    find_packages,
    setup,
)

# 用于从文件中读取依赖第三方模块
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# 打开 VERSION.txt 文件, 读内容, 取出两端空白符, 赋值给version
# 用于读取当前框架的版本号.
with open(join(dirname(__file__), './VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='my_spider',  # 模块名称
    version=version, # 当前框架版本号, 比如: 1.0, 2.0
    description='A mini spider framework, like Scrapy',  # 描述
    packages=find_packages(exclude=['测试']), # exclude: 排除那些包在外
    author='lihaineng',
    author_email='1085436468@email.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='#',
    install_requires=parse_requirements("requirements.txt"),  # 所需的运行环境, 依赖第三方模块
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
