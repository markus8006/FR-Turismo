from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route("/")
def main_page():
    return render_template("index.html")


@main.route("/serviços")
def servicos():
    return render_template("serviços_page.html")