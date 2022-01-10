from flask import render_template, request

from manuel import app
from manuel_functions.parse_listed_product_links import parse_listed_product_links


@app.route("/listed-chart-links", methods=["GET"])
def listed_chart_links_get():
    is_post = False
    return render_template("listed-chart-links.html", is_post=is_post)


@app.route("/listed-chart-links", methods=["POST"])
def listed_chart_links_post():
    is_post = True
    urls = request.form["urlInput"]
    device = request.form["device"]
    if "\r\n" in urls:
        urls = urls.split("\r\n")
    else:
        urls = urls.split("\n")

    names_links = parse_listed_product_links(urls, device).items()
    cnt = len(names_links)
    return render_template("listed-chart-links.html", url=urls, is_post=is_post, names_links=names_links, cnt=cnt)
