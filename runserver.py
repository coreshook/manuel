from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart-links', methods=["GET"])
def chart_links_get():
    return render_template("chart-links.html")


@app.route('/chart-links', methods=["POST"])
def chart_links_post():
    url = {"nice": "awesome", "dick": "balls"}
    url_items = url.items()
    # product_links = url.values()
    # url = request.form['urlInput']

    return render_template("chart-links.html", url_items=url_items)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
