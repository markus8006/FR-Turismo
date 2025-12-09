from flask import Blueprint, render_template, request, redirect, flash, url_for


main = Blueprint('main', __name__)


@main.route("/")
def home_page():
    return render_template("home.html")


@main.route("/agendamento", methods=["GET", "POST"])
def agendamento_page():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        servico = request.form.get("servico", "").strip()
        data = request.form.get("data", "").strip()

        if nome and email and servico and data:
            flash("Seu agendamento foi enviado! Entraremos em contato em breve.")
        else:
            flash("Preencha todos os campos obrigatórios para enviar seu agendamento.")

        return redirect(url_for("main.agendamento_page"))

    return render_template("agendamento.html")


@main.route("/servicos")
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
