from flask import Flask, render_template, request, redirect
 
app = Flask (__name__)
 
@app.route("/")
def index ():
    return render_template ("index.html")
 
@app.route("/validar_notas" , methods=['POST'])
def calcular_notas():
     nome_do_aluno = request.form ["nome_do_aluno"]
     primeira_nota = float (request.form ["primeira_nota"])
     segunda_nota = float ( request.form ["segunda_nota"])
     terceira_nota = float (request.form ["terceira_nota"])
 
     soma = primeira_nota + segunda_nota + terceira_nota
     media = soma/3
 
     caminho_arquivo = 'models/notas.txt'
 
     with open(caminho_arquivo, 'a' ) as arquivo:
        arquivo.write(f"{nome_do_aluno};{primeira_nota};{segunda_nota};{terceira_nota};{media}\n")
   
     return redirect("/")



@app.route("/ver_notas")
def ver_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'
 
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            if len(item) == 5:
                notas.append({
                'nome_do_aluno': item [0],
                'primeira_nota': item [1],
                'segunda_nota': item [2],
                'terceira_nota': item [3],
                'media': item[4]
         })
       
    return render_template("ver_notas.html" , prod=notas)
 
app.run(host='127.0.0.1', port=80, debug=True)