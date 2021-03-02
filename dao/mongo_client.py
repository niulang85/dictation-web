import logging
import sys

import pymongo

from conf import mongo_config


class MongodbUtil:
    __instance = None

    def __init__(self, user, password, host, port, database, max_pool_size=2):
        try:
            client = pymongo.MongoClient(host=host, port=port, maxPoolSize=max_pool_size)
            use_db = client[database]  # 指定连接的库
            use_db.authenticate(user, password)  # 身份验证
            MongodbUtil.__instance = use_db  # 赋值属性，通过该属性执行其他操作
        except Exception as exp:
            logging.error(
                "MongoDB_Util.__init__ : Exception has occured : %s" % str(sys.exc_info()[1]))
            raise exp

    @staticmethod
    def get_instance():
        if MongodbUtil.__instance is None:
            db_conf = mongo_config.get_db_conf()
            MongodbUtil.__instance = MongodbUtil(db_conf['mongo_host'],
                                                 db_conf['mongo_pass'],
                                                 db_conf['mongo_host'],
                                                 db_conf['mongo_port'],
                                                 db_conf['mongo_db_name'])
        return MongodbUtil.__instance
