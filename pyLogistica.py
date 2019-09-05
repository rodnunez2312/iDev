from flask import Flask, render_template
from data import Viajes

app = Flask(__name__)

Viajes = Viajes()

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/viajes')
def viajes():
    return render_template('viajes.html', viajes=Viajes)

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

if __name__ == '__main__':
    app.run()