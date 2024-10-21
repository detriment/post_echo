import json

from flask import Flask, request
from icecream import ic

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handle_post():
    data = request.data
    ic(json.loads(data))
    with open("log.txt", "a") as f:
        f.write(data.decode() + "\n")
    return "POST request received!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
