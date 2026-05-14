from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Website</h1>"

@app.route("/about")
def about():
    return "<h2>About Page</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
