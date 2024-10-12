function showMap() {
    const start = document.getElementById('start').value;
    const end = document.getElementById('end').value;

    // Coordenadas fijas para la demostración
    const startCoords = [0, 0]; // Coordenadas de ejemplo
    const endCoords = [1, 1]; // Coordenadas de ejemplo

    // Crear el mapa
    const map = L.map('map').setView(startCoords, 2); // Cambia la vista inicial según sea necesario

    // Agregar la capa de OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Agregar marcadores
    L.marker(startCoords).addTo(map).bindPopup('Inicio: ' + start).openPopup();
    L.marker(endCoords).addTo(map).bindPopup('Destino: ' + end).openPopup();
}
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TrafficMap = () => {
  const [route, setRoute] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/routes')
      .then(response => setRoute(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Best Route:</h2>
      <pre>{JSON.stringify(route, null, 2)}</pre>
    </div>
  );
};

export default TrafficMap;
