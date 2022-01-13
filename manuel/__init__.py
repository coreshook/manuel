from flask import Flask
from manuel.security_stuff import secret_key

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./"
app.config["SECRET_KEY"] = secret_key

from manuel import index_routes, chart_links_routes, bulk_redirect_editor_routes
from manuel import listed_chart_links_routes, text_comparison_routes, link_prettifier_routes, ip_sheet_routes
