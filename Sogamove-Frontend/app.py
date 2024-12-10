from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registro')
def registrar_usuario():
    return render_template('registro.html')

@app.route('/ingresoUsuarios')
def ingreso_usuarios():
    return render_template('ingresoUsuarios.html')

@app.route('/usuarioRegistrado')
def usuario_registrado():
    return render_template('usuarioRegistrado.html')

@app.route('/comentarios')
def comentarios():
    return render_template('comentarios.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)