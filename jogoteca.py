from flask import Flask, render_template

app = Flask(__name__) #__name__ referencia a propria pagina

@app.route('/inicio')
def ola():
    return render_template('lista.html')

app.run()