from flask import session, Blueprint, request, redirect, render_template
from ..model.sensors import fetch_iot_data


index_pages = Blueprint("index", __name__)

@index_pages.route("/")
def index_page():
    if not session.get("auth", False):
        return redirect("/login", code=302)
    sensors = fetch_iot_data()
    return render_template("index.html", sensors=sensors)

@index_pages.route("/contact")
def contact_page():
    return render_template("contact.html")

