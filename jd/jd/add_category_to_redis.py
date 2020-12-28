import pickle

import pymongo
from redis import StrictRedis
from jd.settings import MONGO_URL, REDIS_URL
from jd.spiders.jd_product import JdProductSpider


def add_category_to_redis():

    # 连接mongodb数据库
    mongo = pymongo.MongoClient(MONGO_URL)
    # 连接redis数据库
    redis = StrictRedis.from_url(REDIS_URL)
    # 选定存数据的集合
    collection = mongo["jd"]["categorys"]
    # 从集合中取出数据，cursor是个列表
    cursor = collection.find()
    for category in cursor:
        # 把字典数据序列化，mongodb转存redis
        data = pickle.dumps(category)
        # 用lpush的方式往redis数据库存入数据
        redis.lpush(JdProductSpider.redis_key, data)

    mongo.close()


if __name__ == '__main__':
    add_category_to_redis()