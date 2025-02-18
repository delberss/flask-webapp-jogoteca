from flask import Flask, render_template
from Jogo import Jogo

app = Flask(__name__) #__name__ referencia a propria pagina


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Fifa', 'Esporte', 'PS5/XBOX')
    jogo2 = Jogo('Call of Duty', 'FPS ', 'PC')
    jogo3 = Jogo('Counter-Strike', 'FPS ', 'PC')

    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista_jogos)

app.run(debug=True) #debug=True para toda vez que tiver mudança no código, Flask atualiza
