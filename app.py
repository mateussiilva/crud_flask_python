from flask import Flask, render_template, request, redirect,url_for
from teste import get_for_id


app = Flask(__name__)


clientes = [
    {"id": 1, "nome": "Mateus jose da silva", "idade": 23},

]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", clientes=clientes)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "GET":
        return render_template("form.html")
    
    elif request.method == "POST":
        nome = request.form["nomeDoCliente"]
        idade = request.form["idadeDoCliente"]

        return f"{nome}{idade}"


@app.route("/edit/<int:id>")
def edit(id):
    cliente = get_for_id(id)
    return f"EDITAND : {cliente}"



@app.route("/delete/<int:id>")
def delete(id):
    return redirect(url_for("index"))



if __name__ == '__main__':
    # app.run(debug=True,host="0.0.0.0")
    app.run(debug=True)
