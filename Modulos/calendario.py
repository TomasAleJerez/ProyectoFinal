
from datetime import datetime, timedelta  # Importa las clases datetime y timedelta del módulo datetime
from Modulos.autenticacion import obtener_servicio_calendario  # Importa la función para autenticar con Google Calendar

class GestorEventos:
    @staticmethod
    def agregar_evento(titulo, fecha_inicio, duracion_horas):
        """
        Agrega un evento a Google Calendar.
        """
        try:
            service = obtener_servicio_calendario()  # Obtiene el servicio de Google Calendar

            # Configuración del evento
            evento = {
                'summary': titulo,  # Título del evento
                'start': {
                    'dateTime': fecha_inicio.isoformat(),  # Fecha y hora de inicio en formato ISO
                    'timeZone': 'America/Argentina/Salta',  # Zona horaria
                },
                'end': {
                    'dateTime': (fecha_inicio + timedelta(hours=duracion_horas)).isoformat(),  # Fecha y hora de fin en formato ISO
                    'timeZone': 'America/Argentina/Salta',  # Zona horaria
                },
            }

            # Inserta el evento en el calendario
            evento_creado = service.events().insert(calendarId='primary', body=evento).execute()
            return f"Evento creado: {evento_creado.get('htmlLink')}"  # Devuelve el enlace al evento creado
        except Exception as e:
            return f"Error al crear el evento: {e}"  # Maneja cualquier excepción y devuelve un mensaje de error

    @staticmethod
    def eliminar_evento(event_id):
        """
        Elimina un evento de Google Calendar usando su ID.
        """
        try:
            service = obtener_servicio_calendario()  # Obtiene el servicio de Google Calendar
            service.events().delete(calendarId='primary', eventId=event_id).execute()  # Elimina el evento usando su ID
            return "Evento eliminado correctamente."  # Devuelve un mensaje de éxito
        except Exception as e:
            return f"Error al eliminar el evento: {e}"  # Maneja cualquier excepción y devuelve un mensaje de error

    @staticmethod
    def listar_eventos():
        """
        Lista los eventos en el calendario.
        """
        try:
            service = obtener_servicio_calendario()  # Obtiene el servicio de Google Calendar
            now = datetime.utcnow().isoformat() + 'Z'  # Hora actual en formato RFC3339
            eventos_resultado = service.events().list(
                calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
                orderBy='startTime').execute()  # Obtiene los próximos 10 eventos ordenados por hora de inicio
            eventos = eventos_resultado.get('items', [])  # Obtiene la lista de eventos

            if not eventos:
                return "No hay eventos próximos."  # Devuelve un mensaje si no hay eventos

            eventos_listados = []
            for evento in eventos:
                inicio = evento['start'].get('dateTime', evento['start'].get('date'))  # Obtiene la fecha y hora de inicio del evento
                eventos_listados.append(f"{inicio} - {evento['summary']} (ID: {evento['id']})")  # Añade el evento a la lista formateada
            return "\n".join(eventos_listados)  # Devuelve la lista de eventos como una cadena de texto
        except Exception as e:
            return f"Error al listar eventos: {e}"  # Maneja cualquier excepción y devuelve un mensaje de error

