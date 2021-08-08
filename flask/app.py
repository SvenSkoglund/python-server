from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<string:page>")
def page_route(page):
    return render_template(page)

@app.route("/")
def my_home():
    return render_template("./index.html")