from flask import render_template, request

from manuel import app
from manuel_functions.prettify_link import prettify_link


@app.route("/link-prettifier", methods=["GET"])
def link_prettifier_get():
    return render_template("link-prettifier-get.html")


@app.route("/link-prettifier", methods=["POST"])
def link_prettifier_post():
    url = request.form["urlInput"]
    link = prettify_link(url)
    return render_template("link-prettifier-post.html", link=link)
