from flask import Flask

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./"
app.config["SECRET_KEY"] = "my name is Giovanni Giorgio, but everybody calls me Giorgio"

from manuel import index_routes, chart_links_routes, bulk_redirect_editor_routes
