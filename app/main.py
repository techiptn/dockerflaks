from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template("index.html")

# @app.route("/<pagename>")
# def get_post(pagename):
#     return render_template(pagename)