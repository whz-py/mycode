# -*- coding: utf-8 -*-

# Scrapy settings for jd project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

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


BOT_NAME = 'jd'

SPIDER_MODULES = ['jd.spiders']
NEWSPIDER_MODULE = 'jd.spiders'

# LOG_LEVEL = 'WARNING'
LOG_FILE = './log.log'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'User-Agent': random.choice(USER_AGENTS),
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie': 'shshshfpa=f29b725a-be38-6f7c-6073-b78c9666b158-1584527806; shshshfpb=uKqDIfEGXyURsBR1%2FkxX7nQ%3D%3D; __jdu=15845278021431471266600; pinId=2hDq5R9mNGYguwrCDhih_LV9-x-f3wj7; areaId=22; user-key=40116653-91a2-486d-80ae-a4c10c22f4cc; unick=%E4%B8%B6Ever%E4%B8%B6; _tp=2Ln6pC%2BhfBybjRCcm19%2Biy2cYn4XBTyj9my4wrxz5Bs%3D; _pst=jd_447978952087c; ipLoc-djd=22-1930-50948-52157.986628109; ipLocation=%u56db%u5ddd; cn=4; unpl=V2_ZzNtbRBSQRF8C0VcKB5eVWJWFFxKVxMSIAxAAX5MVAdjVEBbclRCFnQURlRnGl4UZwYZXkRcQxBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdVQBjABRUQ1RDEHcIQ1J7GlsCYAITbXJQcyVFAU9dfxFeNWYzE20AAx8ScwFGV39UXAFuBhZeRF5CFnUNRFR%2bH1wGYAQVXENnQiV2; PCSYCityID=CN_510000_510100_510107; shshshfp=e871cfc749099fe6c014123b6b848c2f; __jdv=209449046|baidu|-|organic|not set|1606291621322; 3AB9D23F7A4B3C9B=XSKRMDSTHQTQLOD2WGMFSBNGY2QZMVLVFTEX3VN4WOMO4UGTHS3JDNGZWPOUM5EHWJ53Z6TV52NX4FVFUGOOMMUYFI; identity=b423fda4-028f-441c-a909-d4360046ab08; ssid="FnRi6ZDjQU2Eq/Bh7Fn6wQ=="; wlfstk_smdl=m7gle8ez5vmv82kchw2xymrybtk69dtv; TrackID=1u2W_SvAJAxhF6humoDGvXeOis33SYilqm1p9QFHlWQcddFRwBuzJJQc9VKbSBBIGCDAc19ebguaz2IZ-15dsir3oexNndAJnqujvms6GsT4; thor=DA0CE35F31FC38D92410494F0EE73FD867710AD7C00E832F28AF56522A3360FBF1477E64622FEEB191E07CE4532DD79160041E73C196FC6AD5C0F35CA7BF7DD5A05066E28547AA8DFAB1CBE3FA8FECCC0AA05A6435774A548FC52E5E75BA873CD8243E8F8E187A3CB6C0E97921238C72A0CE7FD6E27D8DE85953B0042F900F6DC2D1287C4EB699426C89E1B067B2B492EE9925D7326AA1D914D0D35FBB95B148; pin=jd_447978952087c; ceshi3.com=103; logining=1; __jda=209449046.15845278021431471266600.1584527802.1606291621.1606295763.97; __jdc=209449046; login=true; MNoticeIdjd_447978952087c=310; sidebarStatus=1; RT="z=1&dm=jd.com&si=9pfw5liiqi&ss=khx71cng&sl=2&tt=eh"; __jdb=209449046.8.15845278021431471266600|97.1606295763',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd.middlewares.JdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'jd.middlewares.UserAgentMiddleWare': 546,
    'jd.middlewares.JdSpiderProxyMiddleware': 544,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jd.pipelines.CategoryPipeline': 300,
    'jd.pipelines.ProductPipeline': 301,
    'jd.pipelines.MmeiPipeline': 302,
    'scrapy_redis.pipelines.RedisPipeline': 303  # 加上这个pipeline后结果会自动保存到redis里去
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MONGODB数据库的URL
MONGO_URL = 'mongodb://127.0.0.1:27017'
# 实现在setting中配置scrapy_redis
# REDIS数据库URL
REDIS_URL = 'redis://127.0.0.1:6379'
#
# 去重容器类: 用于已爬指纹存储到基于redis的set集合中
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度器: 用于把待爬取请求存储到基于redis的队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是不是进行调度持久化:
# 如果是True，当程序结束时，会保留redis中已爬指纹和待爬的请求
# 如果时False，当程序结束时，会清空redis中已爬指纹和待爬的请求
SCHEDULER_PERSIST = True

