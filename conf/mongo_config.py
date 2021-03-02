import configparser
import sys


def get_db_conf():
    cf = configparser.ConfigParser()
    cf.read(sys.argv[1])

    mongo_host = cf.get("db", "db_host")
    mongo_port = cf.getint("db", "db_port")
    mongo_user = cf.get("db", "db_user")
    mongo_pass = cf.get("db", "db_pass")
    mongo_db_name = cf.get("db", "db_name")

    return {'mongo_host': mongo_host,
            'mongo_port': mongo_port,
            'mongo_user': mongo_user,
            'mongo_pass': mongo_pass,
            'mongo_db_name': mongo_db_name}
