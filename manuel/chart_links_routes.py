from flask import render_template, request

from manuel import app
from manuel_functions.parse_product_links import parse_product_links


@app.route("/chart-links", methods=["GET"])
def chart_links_get():
    is_post = False
    return render_template("chart-links-get.html", is_post=is_post)


@app.route("/chart-links", methods=["POST"])
def chart_links_post():
    url = request.form["urlInput"]
    device = request.form["device"]
    names_links = parse_product_links(url, device).items()
    cnt = len(names_links)
    return render_template("chart-links-post.html", url=url, names_links=names_links, cnt=cnt)
