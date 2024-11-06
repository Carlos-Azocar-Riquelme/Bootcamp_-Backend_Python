from flask import Flask, render_template, redirect, request, url_for, flash
from datetime import datetime

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)


# @app.route('/usuario/<nombre>')
# def usuario(nombre):
#     return f"hola! {nombre}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    integrantes = ["Carlos", "Nicolas", "Camila", "Stefy", "Cristobal" , "Luis"]
    grupo = "Grupo 6"
    descripcion = "Grupo de bootcamp python"
    tiempo = datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S")
    return render_template('about.html', grupo = grupo, descripcion = descripcion, integrantes = integrantes, tiempo = tiempo)

@app.route('/perfil')
def perfil():
    nombre = request.args.get('nombre', 'Invitado')
    edad = request.args.get('edad', 0)
    profesion = request.args.get('profesion', 'trabajador independiente')
    return render_template('perfil.html', nombre = nombre, edad = edad, profesion = profesion)

# ruta en caso de querer correr perfil con información pasada por la URL
# http://127.0.0.1:5000/perfil?nombre=carlos&edad=50&profesion=programador

app.secret_key = 'clave123'
anuncios_list = [] 

@app.route('/anuncio', methods=['GET', 'POST'])
def anuncio():
    if request.method == 'POST':
        titulo = request.form.get('titulo', None)
        contenido = request.form['contenido']
        prioridad = request.form['prioridad'],

        if not titulo:
            flash("Favor ingrese el titulo")
        if not contenido:
            flash("Favor ingrese el contenido")
        nuevo_anuncio = {'titulo': titulo, 'contenido': contenido, 'prioridad': prioridad}
        anuncios_list.append(nuevo_anuncio)        
        return redirect(url_for('anuncio'))
    return render_template('anuncio.html')

@app.route('/anuncios', methods=['GET'])
def anuncios():
    return render_template('anuncios.html', anuncios = anuncios_list)


if __name__ == '__main__':
    app.run(debug=True)


