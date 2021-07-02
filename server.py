from flask import Flask

PORT = 8000
MESSAGE = "Hello team!\nThank you for your attention ;)"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=PORT)
