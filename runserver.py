from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart-links')
def chart_links():
    return render_template("chart-links.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
