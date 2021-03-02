import logging


# 初始化logging
logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='dic.log',
                    filemode='a')

# set to print log to console at the same time
console = logging.StreamHandler()
console.setLevel(logging.NOTSET)
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
