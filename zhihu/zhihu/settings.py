# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

LOG_LEVEL = 'WARNING'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

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
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'referer': 'https://www.zhihu.com/people/Germey/following',
    'x-zse-83': '3_2.0',
    'x-zse-86': '2.0_aR2qHUH8eXtfQTxq8TNq6Qe8Q0FYFBNBYXxBQQUBSLtf',
    'cookie': '_zap=abcb94a6-851f-45d3-9d96-5cdae052adfc; d_c0="AHDY1EeR6xCPTmMYY4bhnbqflIw6LWiOimc=|1583466574"; _ga=GA1.2.1211890025.1583466578; _xsrf=IpjE8qHRSbDlHuPyVhtwS3FfaYNUidu4; __utmv=51854390.000--|3=entry_date=20200426=1; __utma=51854390.1211890025.1583466578.1587886842.1608962321.5; __utmz=51854390.1608962321.5.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); capsion_ticket="2|1:0|10:1610343867|14:capsion_ticket|44:NWYzOTliMDdjYjVlNGIxOTk2OTFkMzg5NDhiNjQyMTc=|54ef959f6a5bccdd35c28df134cb60c247e41580de736d0bf8f81766bdcce464"; z_c0="2|1:0|10:1610344051|4:z_c0|92:Mi4xamIwQkFRQUFBQUFBY05qVVI1SHJFQ2NBQUFDRUFsVk5jbk1qWUFETDNiTFpHMnpqVjR5N0djb3VEN1pNWmhtcjZn|71bf0631aba987294cf29d3a9660348d830176baf1c16fa47388fe16dcd0f954"; tst=h; tshl=; q_c1=f10bd6a20dee48a3a95f5b6177f7d6b8|1610344423000|1587869645000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1612491787,1612492514,1612505677,1612579370; SESSIONID=aPK08NwLV4fKyUSX6Ib16geREnTlE4IYER2H7FqtmSe; JOID=UlsVB0tcurLK9-ijdljpbBmhtytnPun9_s-l1z4KjdeFir3zLXW_rK706KR2ilNrkuZjFtI2JzOzmnRszSGrqYk=; osd=W1sQCkxVurfH8OGjc1XuZRmkuixuPuzw-cal0jMNhNeAh7r6LXCyq6f07alxg1Nun-FqFtc7IDqzn3lrxCGupI4=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1612579383; KLBRSID=ca494ee5d16b14b649673c122ff27291|1612579382|1612579366'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.ZhihuPipeline': 300,
#}

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
