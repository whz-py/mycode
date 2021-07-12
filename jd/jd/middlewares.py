# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import sys
import random
import requests
import json
from scrapy import signals
import logging

sys.setrecursionlimit(2000000)
logger = logging.getLogger(__name__)


class JdSpiderProxyMiddleware(object):
    def __init__(self):
        self.api_url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=fd69f3980c824e26bb7b10bc9ef3635d&orderno=YZ20216243369IoolQ0&returnType=2&count=3"
        self.check_url = "http://httpbin.org/get"
        self.ip_list = []
        # count 表示正在使用ip_list中第几个ip，刚开始索引是0，也就是第一个ip
        self.count = 0
        # eve_count表示每个ip的使用次数，最多使用3次，切换下一个ip
        self.eve_count = 0
        self.new_list = []

    def getIp(self):
        '''
        通过api获取ip数据
        :return:
        '''
        print('开始提取ip')
        res = requests.get(url=self.api_url).text
        self.ip_list.clear()  # 清空上一个循环列表里的ip
        for eve_ip in json.loads(res)['RESULT']:
            self.ip_list.append({
                'ip': eve_ip['ip'],
                'port': eve_ip["port"]
            })
        print('ip列表是：', self.ip_list)

    def changeProxy(self, request):
        '''
        切换ip，为什么是self.count-1， 因为索引是从0开始
        :param request:
        :return:
        '''
        request.meta['proxy'] = 'http://' + str(self.ip_list[self.count - 1]['ip']) + ":" + str(
            self.ip_list[self.count - 1]['port'])

    def yanzheng(self):
        '''
        验证ip是否可用
        :return:
        '''
        print(self.ip_list[self.count - 1]['ip'])
        # print("取列表中ip时的count值:", self.count)
        requests.get(url=self.check_url, proxies={
            "http://": str(self.ip_list[self.count - 1]['ip']) + ":" + str(self.ip_list[self.count - 1]['port'])}, timeout=5)


    def ifUsed(self, request):
        '''
        进行切换并验证
        :param request:
        :return:
        '''
        try:
            self.changeProxy(request)   # 切换ip
            self.yanzheng()  # 验证如果可用，就会进行请求，如果报错，进行下面的步骤
        except:
            print('验证失败，重新提取ip')
            if self.count == 0 or self.count == 4:
                print('count值为0或者4，开始获取新的ip')
                self.getIp()
                self.count = 1   # 重置count值
                self.eve_count = 0   # 重置eve——count值
            else:
                if 0 < self.count < 3:
                    self.count += self.count
                    print("此时的coun数是", self.count)
                    self.ifUsed(request)


    def process_request(self, request, spider):
        if self.count == 0 or self.count == 4:  #刚开始或者用完了列表里ip时
            self.getIp()        # 重新取ip数据
            self.count = 1   # count置为1
            # print('第一个count数是:', self.count)

        if self.eve_count == 10:   # 如果一个ip使用了3次
            self.count += 1  # count数也加1，相当于切换列表里下一个ip
            self.eve_count = 1  # 并且把self.eve_count重置为1次
            # print("3次调用ip后的eve-count：", self.eve_count)
        else:
            self.eve_count += 1
            # print('此时的eve——count是：', self.eve_count)
        self.ifUsed(request)   # 切换ip并且验证ip，不断循环


class UserAgentMiddleWare(object):

    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    ]

    def process_request(self, request, spider):
        ua = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = ua
