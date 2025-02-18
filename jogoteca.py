from flask import Flask, render_template, request, redirect
from Jogo import Jogo

app = Flask(__name__) #__name__ referencia a propria pagina

jogo1 = Jogo('Fifa', 'Esporte', 'PS5/XBOX')
jogo2 = Jogo('Call of Duty', 'FPS ', 'PC')
jogo3 = Jogo('Counter-Strike', 'FPS ', 'PC')

lista_jogos = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect('/')


app.run(debug=True) #debug=True para toda vez que tiver mudança no código, Flask atualiza
