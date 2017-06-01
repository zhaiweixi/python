# coding: utf-8
"""
    zwx 2017-06-01
    爬虫类
"""
import urllib2


class Crawler:

    def __init__(self, login_url, param):
        self.__login_url = login_url
        self.__param = param

    def __connect(self):
        pass

    def get_data_json(self):
        pass

    def get_data_xml(self):
        pass

    def get_data_html(self):
        pass