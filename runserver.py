from datetime import datetime
from flask import Flask, render_template, url_for, request, flash
from werkzeug.utils import secure_filename, redirect
import os
from csv import writer

from manuel_functions.listify_csv import listify_csv
from manuel_functions.parse_product_links import parse_product_links

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./"
app.config["SECRET_KEY"] = "my name is Giovanni Giorgio, but everybody calls me Giorgio"
file_content = []
csv_headers = []


# INDEX PAGE
@app.route('/')
def index():
    return render_template("index.html")


# CHART PRODUCT LINKS
@app.route("/chart-links", methods=["GET"])
def chart_links_get():
    is_post = False
    return render_template("chart-links.html", is_post=is_post)


@app.route("/chart-links", methods=["POST"])
def chart_links_post():
    is_post = True
    url = request.form["urlInput"]
    device = request.form["device"]
    names_links = parse_product_links(url, device).items()
    cnt = len(names_links)
    return render_template("chart-links.html", url=url, is_post=is_post, names_links=names_links, cnt=cnt)


# BULK REDIRECT EDITOR
@app.route("/bulk-redirect-editor", methods=["GET"])
def bulk_redirect_editor_get():
    return render_template("bulk-redirect-editor.html")


@app.route("/bulk-upload", methods=["POST"])
def bulk_upload():
    if not request.files["file"].filename.endswith(".csv"):
        return render_template("bulk-redirect-editor.html", not_CSV=True)
    else:
        raw_file = request.files["file"]
        raw_file.save(secure_filename(raw_file.filename))

        try:
            global file_content, csv_headers
            csv_headers, file_content = listify_csv(secure_filename(raw_file.filename))
        finally:
            os.unlink(secure_filename(raw_file.filename))
        return render_template("bulk-redirect-editor.html", headers=csv_headers, file=file_content)


@app.route("/delete-csv-line", methods=["POST"])
def delete_csv_line():
    first_value = request.form["deleteLine0"]
    second_value = request.form["deleteLine1"]
    values_to_delete = [first_value, second_value]

    global file_content, csv_headers
    try:
        file_content.remove(values_to_delete)
    except ValueError:
        flash("Error: You've attempted to delete an already deleted value. Please re-upload the file and start over")
        return redirect(url_for("bulk_redirect_editor_get"))
    return render_template("bulk-redirect-editor.html", headers=csv_headers, file=file_content)


@app.route("/add-csv-line", methods=["POST"])
def add_csv_line():
    first_value = request.form["addLine0"]
    second_value = request.form["addLine1"]
    values_to_add = [first_value.strip(), second_value.strip()]

    global file_content, csv_headers
    file_content.append(values_to_add)
    return render_template("bulk-redirect-editor.html", headers=csv_headers, file=file_content)


@app.route("/download-csv", methods=["POST"])
def download_csv_file():
    global file_content, csv_headers
    current_date = datetime.now().strftime("%d-%m-%Y")
    current_filename = secure_filename("Manuel-Bulk_--_" + current_date + ".csv")
    with open(current_filename, "w") as file:
        try:
            write = writer(file)
            write.writerow(csv_headers)
            write.writerows(file_content)
            file.close()
        except OSError:
            flash("An error occurred while trying to write file. Sorry, please try again")
            return redirect(url_for("bulk_redirect_editor_get"))

    def generate():
        with open(current_filename) as file_to_download:
            yield from file_to_download
        os.remove(current_filename)

    r = app.response_class(generate(), mimetype="text/csv")
    r.headers.set("Content-Disposition", "attachment", filename=current_filename)
    return r


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
