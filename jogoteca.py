from flask import Flask, render_template, request, redirect, session, flash, url_for
from Jogo import Jogo

jogo1 = Jogo('Fifa', 'Esporte', 'PS5/XBOX')
jogo2 = Jogo('Call of Duty', 'FPS ', 'PC')
jogo3 = Jogo('Counter-Strike', 'FPS ', 'PC')

lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__) #__name__ referencia a propria pagina
app.secret_key = 'dssoares'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #usando o ?proxima=novo como parametro para proxima pagina
        return redirect(url_for('login', proxima=url_for('novo'))) 
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect(url_for('index')) # passa a função que instancia a pagina

@app.route('/login')
def login():
    proxima = request.args.get('proxima') #pega o argumento se existir
    #passa esse argumento para tela renderizada
    return render_template('login.html', proxima=proxima) 

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    proxima_pagina = request.form['proxima']

    if not proxima_pagina or proxima_pagina == "None":
        proxima_pagina = url_for('index')

    if senha == 'admin':
        session['usuario_logado'] = usuario
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


app.run(debug=True) #debug=True para toda vez que tiver mudança no código, Flask atualiza
