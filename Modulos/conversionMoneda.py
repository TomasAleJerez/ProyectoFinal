import requests  # Permite enviar solicitudes HTTP para interactuar con APIs externas.

class ConvertidorMoneda:
    API_KEY = "2e25582f8633944fa91dbabb"  # Reemplaza con tu API Key de ExchangeRate-API

    @staticmethod
    def convertir_moneda(monto, moneda_origen, moneda_destino):
        """
        Convierte una cantidad de una moneda a otra usando la API de ExchangeRate-API.
        """
        try:
            # Construye la URL para la solicitud a la API
            url = f"https://v6.exchangerate-api.com/v6/{ConvertidorMoneda.API_KEY}/latest/{moneda_origen}"
            respuesta = requests.get(url)  # Realiza la solicitud HTTP a la API
            datos = respuesta.json()  # Convierte la respuesta a formato JSON
            if respuesta.status_code == 200:  # Verifica si la solicitud fue exitosa
                tasa = datos["conversion_rates"].get(moneda_destino)  # Obtiene la tasa de conversión
                if tasa:
                    convertido = monto * tasa  # Calcula el monto convertido
                    return f"{monto} {moneda_origen} son {convertido:.2f} {moneda_destino}."
                else:
                    return f"No se encontró información para convertir {moneda_destino}."
            else:
                return f"Error: {datos.get('error-type', 'No se pudo realizar la conversión.')}"
        except requests.RequestException as e:
            # Maneja errores de conexión
            return f"Error de conexión: {e}"
        
        
