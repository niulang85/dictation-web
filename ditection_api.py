import pathlib as path
import sys

import requests
from flask import Flask, Response

import dao.mongo_client as mongo_client

app = Flask(__name__)

mongo_db = mongo_client.MongodbUtil.get_instance()
data_path = path.join(path.dirname(path.abspath(__file__)), 'dictation-web-data')


@app.route("/helloWorld")
def hello_world():
    # mc.collection_names()
    return "Hello Flask..."


@app.route('/words')
def read_words():
    # 读取json文件内容,返回字典格式
    with open(data_path + '/data_file/words.json', 'r', encoding='utf8')as fp:
        json_data = fp.read()
        return json_data


@app.route('/voice/<word>')
def stream_mp3(word):
    # cache_path = f'../data_file/media/{word}.mp3'

    cache_path = f'{data_path}/data_file/media/{word}.mp3'
    cache_word(word, cache_path)

    def generate():
        with open(cache_path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")


def cache_word(word, cache_path):
    cache_path = path.Path(cache_path)
    # cache_path.mkdir(parents=True)
    if cache_path.exists():
        return

    # us代表Uncle Sam “gb”代表Great Britain
    # url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/apple--_us_1.mp3'
    url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_gb_1.mp3'
    res = requests.get(url)
    with open(cache_path, 'wb') as file:
        file.write(res.content)
        file.flush()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8987, debug=True)
    user_name = sys.argv[1]
