from flask import Flask, Response

app = Flask(__name__)


@app.route("/helloWorld")
def hello_world():
    return "Hello Flask..."


@app.route('/words')
def read_words():
    # 读取json文件内容,返回字典格式
    with open('./data_file/words.json', 'r', encoding='utf8')as fp:
        json_data = fp.read()
        return json_data


@app.route('/voice/<word>')
def stream_mp3(word):
    def generate():
        # path = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/apple--_gb_1.mp3' us代表Uncle Sam “gb”代表Great Britain
        path = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_gb_1.mp3'
        # path = f'./data_file/media/{word}.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8987, debug=True)