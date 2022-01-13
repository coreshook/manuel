from flask import render_template

from manuel import app
from manuel_functions.ip_sheet import ip_sheet


@app.route("/ip-sheet")
def ip_sheet_get():
    ip_items = ip_sheet.items()
    return render_template("ip-sheet.html", ip_items=ip_items)
