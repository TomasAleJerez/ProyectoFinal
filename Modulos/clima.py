import requests  # Permite enviar solicitudes HTTP para interactuar con APIs externas.

class GestorClima:
    API_KEY = "e4a3e247aaa85d85fb2802f59ec21057"  # Reemplaza con tu API Key de OpenWeather

    @staticmethod
    def obtener_clima(ciudad):
        """
        Obtiene el clima de una ciudad usando la API de OpenWeather.
        """
        try:
            # Construye la URL para la solicitud a la API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={GestorClima.API_KEY}&units=metric&lang=es"
            respuesta = requests.get(url)
            datos = respuesta.json()
            if respuesta.status_code == 200:
                # Extrae la temperatura y la descripción del clima de la respuesta
                temp = datos["main"]["temp"]
                clima = datos["weather"][0]["description"]
                return f"El clima en {ciudad} es {temp}°C con {clima}."
            else:
                return f"Error: {datos.get('message', 'No se pudo obtener el clima.')}"
        except requests.RequestException as e:
            # Maneja errores de conexión
            return f"Error de conexión: {e}"
