#請建立一個Flask應用程式，並在根路由 ("/") 回傳 "Hello, World!" 的訊息。
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
if __name__ == "__main__":
    app.run(debug=True)