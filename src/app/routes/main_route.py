from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route("/")
def main_page():
    return render_template("home.html")


@main.route("/serviços")
def servicos():
    return render_template("servicos.html")