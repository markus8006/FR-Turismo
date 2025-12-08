from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route("/")
def home_page():
    return render_template("home.html")

@main.route("/agendamento")
def agendamento_page():
    return render_template("agendamento.html")

@main.route("/serviços")
def servicos_page():
    return render_template("servicos.html")

@main.route("/contato")
def contato_page():
    return render_template("contato.html")

@main.route("/depoimentos")
def depoimentos_page():
    return render_template("depoimentos.html")

@main.route("/sobre")
def sobre_page():
    return render_template("sobre.html")

