from primer_app import app
from flask import render_template, request, redirect


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente 
def hola_mundo():                   # y a menos que no indiquemos otro metodo de consulta, es por default GET
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta


@app.route('/repeat/<int:numero>/<palabra>')
def index(numero, palabra):
    return render_template("index.html", palabra=palabra, numero=numero) #entregar la plantilla html al cliente con 2 variables
  

@app.route('/play/<int:numero>/<color>')
def repetir_prisma(numero, color):
    return render_template('jugar.html', numero=numero, color=color)

@app.route('/registro')
def formulario_registro():
    return render_template('registro.html')

@app.route('/usuarios', methods=['POST'])
def envio_formualario():
    print(request.form, "#./"*20)
    print(request.form['nombre'], "Aqui viene el nombre del formulario")

    return redirect ('/')
    # return 'Formulario enviado exitosamente'

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404