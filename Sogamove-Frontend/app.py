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

if __name__ == '__main__':
    app.run(debug=True)