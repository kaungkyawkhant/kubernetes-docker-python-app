from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>The web application running in Docker container</h1>'


if __name__ == "__main__":
    app.run(debug=True)