from flask import Flask, render_template, request, redirect,session
 
app = Flask(__name__)
app.secret_key = 'chave_secreta_aleatoria'  # Necessário para usar sessões
 
 
def cal_cat_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"
 
@app.route("/")
def index():
    return render_template("index.html")
 
 
@app.route("/index.html", methods=['POST'])
def cal_imc():
    nome = request.form["nome"]
    peso = float (request.form["peso"])
    altura= float (request.form["altura"])
 
    resultado = peso / (altura ** 2)
    resultado = round(resultado, 2) #round arredonda números
    categoria = cal_cat_imc(resultado)
 
    session['nome'] = nome #permite armazenar dados temporários
    session['imc'] = resultado
    session['categoria'] = categoria
 
    nome = session.get('nome') #os valores são diretamente da session
    imc = session.get('imc')
    categoria = session.get('categoria')
    return render_template('resultado.html', nome=nome, imc=imc, categoria=categoria)
 
@app.route("/ver_imc")
def ver_imc():
    nome = session.get('nome') #os valores são diretamente da session
    imc = session.get('imc')
    categoria = session.get('categoria')
    return render_template('resultado.html', nome=nome, imc=imc, categoria=categoria)
 
 
app.run(host='127.0.0.1', port=80, debug=True)