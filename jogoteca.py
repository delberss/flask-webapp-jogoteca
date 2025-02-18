from flask import Flask, render_template

app = Flask(__name__) #__name__ referencia a propria pagina


@app.route('/inicio')
def ola():
    lista_jogos=['Batman', 'Fifa']
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista_jogos)

app.run(debug=True) #debug=True para toda vez que tiver mudança no código, Flask atualiza
