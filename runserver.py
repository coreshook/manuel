from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

from manuel_functions.listify_csv import listify_csv
from manuel_functions.parse_product_links import parse_product_links

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./"


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/chart-links", methods=["GET"])
def chart_links_get():
    is_post = False
    return render_template("chart-links.html", is_post=is_post)


@app.route("/chart-links", methods=["POST"])
def chart_links_post():
    is_post = True
    url = request.form["urlInput"]
    names_links = parse_product_links(url).items()
    cnt = len(names_links)
    return render_template("chart-links.html", url=url, is_post=is_post, names_links=names_links, cnt=cnt)


@app.route("/bulk-redirect-editor", methods=["GET"])
def bulk_redirect_editor_get():
    return render_template("bulk-redirect-editor.html")


@app.route("/bulk-upload", methods=["POST"])
def bulk_upload():
    raw_file = request.files["file"]
    raw_file.save(secure_filename(raw_file.filename))

    csv_headers, file_content = listify_csv(secure_filename(raw_file.filename))
    return render_template("bulk-redirect-editor.html", headers=csv_headers, file=file_content)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
