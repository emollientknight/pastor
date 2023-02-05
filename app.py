from time import sleep
from flask import Flask, jsonify, request

from sessions import Sessions


app = Flask(__name__)

sessions = Sessions()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/ask', methods=['POST'], )
def ask():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if (content_type == 'application/json'):
        json = request.json
        # data = sessions.ask(json['token'], json['input'])
        sleep(3)
        # return jsonify({"data": data['choices'][0]['text']}), 200
        return "test"
    else:
        return 'Content-Type not supported!'
    