from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Ruta para la página principal
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Cambia el puerto si es necesario
