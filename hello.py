from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color:red;text-align:center;'>This is my landing page</h1>"

@app.route("/About/")
def about():
    return "<h1 style='color:blue;'>This About page</h1>"





if __name__ == '__main__':

    app.run(debug=True)
