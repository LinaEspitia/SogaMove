from flask import Flask, render_template

app = Flask(__name__)
 # Función para geocodificar una dirección
def geocodificar(direccion):
    
    api_key = os.getenv("GOOGLE_MAPS_API_KEY", "TU_CLAVE_API")  
    
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={direccion}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data['results']:
        location = data['results'][0]['geometry']['location']
        return (location['lat'], location['lng'])
    else:
        return None

# Ruta principal para renderizar el formulario de la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para generar la ruta
@app.route('/generar_ruta', methods=['POST'])
def generar_ruta():
    data = request.get_json()
    direccion_origen = data['origen']
    direccion_destino = data['destino']

    # Geocodificación de direcciones
    coordenadas_origen = geocodificar(direccion_origen)
    coordenadas_destino = geocodificar(direccion_destino)

    if not coordenadas_origen or not coordenadas_destino:
        return jsonify({'error': 'No se pudo geocodificar una o ambas direcciones'}), 400

    # Crear la URL para Directions API
    api_key = os.getenv("GOOGLE_MAPS_API_KEY", "TU_CLAVE_API")
    directions_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={coordenadas_origen[0]},{coordenadas_origen[1]}&destination={coordenadas_destino[0]},{coordenadas_destino[1]}&key={api_key}"
    response = requests.get(directions_url)
    ruta = response.json()

    return jsonify(ruta)

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
