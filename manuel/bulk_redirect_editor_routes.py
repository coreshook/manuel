from _csv import writer
from datetime import datetime
from os import unlink, remove

from flask import render_template, request, flash, url_for
from werkzeug.utils import secure_filename, redirect

from manuel import app
from manuel_functions.listify_csv import listify_csv

file_content = []
csv_headers = []


@app.route("/bulk-redirect-editor", methods=["GET"])
def bulk_redirect_editor_get():
    return render_template("bulk-redirect-editor-get.html")


@app.route("/bulk-upload", methods=["POST"])
def bulk_upload():
    if not request.files["file"].filename.endswith(".csv"):
        return render_template("bulk-redirect-editor-get.html", not_CSV=True)
    else:
        raw_file = request.files["file"]
        raw_file.save(secure_filename(raw_file.filename))

        try:
            global file_content, csv_headers
            csv_headers, file_content = listify_csv(secure_filename(raw_file.filename))
        finally:
            unlink(secure_filename(raw_file.filename))
        return render_template("bulk-redirect-editor-post.html", headers=csv_headers, file=file_content)


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
    return render_template("bulk-redirect-editor-post.html", headers=csv_headers, file=file_content)


@app.route("/add-csv-line", methods=["POST"])
def add_csv_line():
    first_value = request.form["addLine0"]
    second_value = request.form["addLine1"]
    values_to_add = [first_value.strip(), second_value.strip()]

    global file_content, csv_headers
    file_content.append(values_to_add)
    return render_template("bulk-redirect-editor-post.html", headers=csv_headers, file=file_content)


@app.route("/download-csv", methods=["POST"])
def download_csv_file():
    global file_content, csv_headers
    current_date = datetime.now().strftime("%d-%m-%Y")
    current_filename = secure_filename("Manuel-Bulk_--_" + current_date + ".csv")
    with open(current_filename, "w", newline='') as file:
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
        remove(current_filename)

    r = app.response_class(generate(), mimetype="text/csv")
    r.headers.set("Content-Disposition", "attachment", filename=current_filename)
    return r
