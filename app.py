from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    valor1 = request.args.get("valor1", 0)
    valor2 = request.args.get("valor2", 0)

    valor1 = float(valor1)
    valor2 = float(valor2)
    
    resultado = valor1 + valor2
    return f'<h1> o resultado é:{resultado} </h1>'

if __name__ == "__main__":
    app.run(debug=True)

#subtração
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/subtração")
def subtração ():
    valor1 = request.args.get("valor1", 0)
    valor2 = request.args.get("valor2", 0)

    valor1 = float(valor1)
    valor2 = float(valor2)
    
    resultado = valor1 - valor2
    return f'<h1> o resultado é:{resultado} </h1>'

if __name__ == "__main__":
    app.run(debug=True)

    #multiplicação

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/multiplicação")
def multiplicação ():
    valor1 = request.args.get("valor1", 0)
    valor2 = request.args.get("valor2", 0)

    valor1 = float(valor1)
    valor2 = float(valor2)
    
    resultado = valor1 * valor2
    return f'<h1> o resultado é:{resultado} </h1>'

if __name__ == "__main__":
    app.run(debug=True)

    #divisao
    from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/divisao")
def divisao ():
    valor1 = request.args.get("valor1", 0)
    valor2 = request.args.get("valor2", 0)

    valor1 = float(valor1)
    valor2 = float(valor2)
    
    resultado = valor1 / valor2
    return f'<h1> o resultado é:{resultado} </h1>'

if __name__ == "__main__":
    app.run(debug=True)

