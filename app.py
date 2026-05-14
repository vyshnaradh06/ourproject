from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Website</h1>
    <p>This website is running with Python Flask.</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About Page</h2>
    <p>This is a simple Flask web application.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
