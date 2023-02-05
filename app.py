import os
from time import sleep
from dotenv import load_dotenv
from flask import Flask, jsonify, request

from sessions import Sessions

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__, static_folder=os.getenv("STATIC_FOLDER"), static_url_path="/")

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
        data = sessions.ask(json['token'], json['input'])
        return jsonify({"data": data['choices'][0]['text']}), 200
    else:
        return 'Content-Type not supported!'
    