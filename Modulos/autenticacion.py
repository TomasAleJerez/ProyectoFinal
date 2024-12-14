
import os  # Proporciona funciones para interactuar con el sistema operativo, como verificar si un archivo existe.
import pickle  # Permite serializar y deserializar objetos de Python para almacenarlos en archivos, como las credenciales de usuario.
from google_auth_oauthlib.flow import InstalledAppFlow  # Gestiona el flujo de autenticación OAuth 2.0 para acceder a las APIs de Google.
from googleapiclient.discovery import build  # Crea un objeto de servicio para interactuar con la API de Google, como Google Calendar.
from googleapiclient.errors import HttpError  # Maneja excepciones específicas de errores HTTP al interactuar con las APIs de Google.
from datetime import datetime, timedelta  # Ofrece herramientas para trabajar con fechas y horas, como crear, modificar o calcular diferencias.
from google.auth.transport.requests import Request  # Refresca credenciales expiradas utilizando un flujo seguro de transporte.



# Alcances necesarios para acceder al calendario
SCOPES = ['https://www.googleapis.com/auth/calendar']

def obtener_servicio_calendario():
    """Autentica al usuario y devuelve el servicio de Google Calendar."""
    creds = None  # Inicializa las credenciales como None
    # Carga las credenciales si ya existe el archivo token.pickle
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)  # Carga las credenciales desde el archivo token.pickle

    # Si las credenciales no son válidas, inicia el flujo de autenticación
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Refresca las credenciales si están expiradas y hay un token de refresco
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)  # Crea el flujo de OAuth 2.0 desde el archivo de secretos del cliente
            creds = flow.run_local_server(port=0)  # Ejecuta el servidor local para completar el flujo de OAuth

        # Guarda las credenciales para la próxima vez
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)  # Guarda las credenciales en el archivo token.pickle

    try:
        # Obtiene el servicio de Google Calendar
        service = build('calendar', 'v3', credentials=creds)
        return service  # Retorna el servicio de Google Calendar
    except HttpError as error:
        print(f'Error al obtener el servicio de Google Calendar: {error}')  # Imprime un mensaje de error si ocurre una excepción
        return None  # Retorna None si ocurre un error

def crear_evento(service, nombre_evento, fecha_hora, duracion):
    """Crea un evento en Google Calendar."""
    # Convierte la fecha y hora de inicio a un objeto datetime
    fecha_inicio = datetime.strptime(fecha_hora, "%Y-%m-%dT%H:%M:%S")
    # Calcula la fecha y hora de finalización sumando la duración
    fecha_fin = fecha_inicio + timedelta(hours=duracion)
    
    # Crea el evento con los datos correctos
    evento = {
        'summary': nombre_evento,  # Título del evento
        'start': {
            'dateTime': fecha_inicio.isoformat(),  # Fecha y hora de inicio en formato ISO
            'timeZone': 'America/Argentina/Buenos_Aires',  # Zona horaria
        },
        'end': {
            'dateTime': fecha_fin.isoformat(),  # Fecha y hora de fin en formato ISO
            'timeZone': 'America/Argentina/Buenos_Aires',  # Zona horaria
        },
    }
    
    try:
        # Intenta agregar el evento al calendario
        evento_creado = service.events().insert(calendarId='primary', body=evento).execute()
        return f"Evento creado: {evento_creado.get('htmlLink')}"  # Devuelve el enlace al evento creado
    except HttpError as error:
        return f'Ha ocurrido un error al crear el evento: {error}'  # Maneja cualquier excepción y devuelve un mensaje de error
    







