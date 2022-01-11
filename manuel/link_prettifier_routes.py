from flask import render_template, request

from manuel import app
from manuel_functions.prettify_link import prettify_link


@app.route("/link-prettifier", methods=["GET"])
def link_prettifier_get():
    return render_template("link-prettifier-get.html")


@app.route("/link-prettifier", methods=["POST"])
def link_prettifier_post():
    url = request.form["urlInput"]
    try:
        link = prettify_link(url)
    except KeyError:
        link = "is not a Top10 partner's link, so I failed to prettify it"
    return render_template("link-prettifier-post.html", link=link)
