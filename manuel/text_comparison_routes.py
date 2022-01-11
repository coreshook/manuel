from flask import render_template, request

from manuel import app
from manuel_functions.compare_texts import compare_texts


@app.route("/text-comparison", methods=["GET"])
def text_comparison_get():
    return render_template("text-comparison-get.html")


@app.route("/text-comparison", methods=["POST"])
def text_comparison_post():
    text1 = request.form["textOneInput"]
    text2 = request.form["textTwoInput"]

    diff = compare_texts(text1, text2)

    return render_template("text-comparison-post.html", diff=diff)
