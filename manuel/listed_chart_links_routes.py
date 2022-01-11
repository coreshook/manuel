from flask import render_template, request

from manuel import app
from manuel_functions.parse_listed_product_links import parse_listed_product_links


@app.route("/listed-chart-links", methods=["GET"])
def listed_chart_links_get():
    is_post = False
    return render_template("listed-chart-links-get.html", is_post=is_post)


@app.route("/listed-chart-links", methods=["POST"])
def listed_chart_links_post():
    urls = request.form["urlInput"]
    device = request.form["device"]

    urls.replace(",", "")
    urls = urls.split("\r\n")

    names_links = parse_listed_product_links(urls, device).items()
    cnt = len(names_links)
    return render_template("listed-chart-links-post.html", url=urls, names_links=names_links, cnt=cnt)
