from flask import Blueprint, flash, redirect, render_template, request, url_for

from src.repository.depoimentos_repository import DepoimentosRepository

main = Blueprint("main", __name__)


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


@main.route("/depoimentos", methods=["GET", "POST"])
def depoimentos_page():
    depoimentos_repo = DepoimentosRepository()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        avaliacao_raw = request.form.get("avaliacao", "").strip()
        conteudo = request.form.get("conteudo", "").strip()

        if not nome or not conteudo:
            flash("Informe seu nome e depoimento para enviar.")
            return redirect(url_for("main.depoimentos_page"))

        try:
            avaliacao = int(avaliacao_raw) if avaliacao_raw else 5
        except ValueError:
            avaliacao = 5

        avaliacao = min(max(avaliacao, 1), 5)

        depoimentos_repo.add(author_name=nome, rating=avaliacao, conteudo=conteudo)

        flash("Depoimento enviado com sucesso! Obrigado por compartilhar sua experiência.")
        return redirect(url_for("main.depoimentos_page"))

    depoimentos = sorted(
        depoimentos_repo.get_all(), key=lambda depoimento: depoimento.created_at or 0, reverse=True
    )
    return render_template("depoimentos.html", depoimentos=depoimentos)


@main.route("/sobre")
def sobre_page():
    return render_template("sobre.html")
