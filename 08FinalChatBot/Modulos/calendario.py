from datetime import datetime, timedelta

class GestorEventos:
    @staticmethod
    def agregar_evento(nombre_evento, fecha_hora, duracion=1):
        """
        Simula la creación de un evento en Google Calendar.
        """
        try:
            # Convierte la fecha y hora de inicio a un objeto datetime
            hora_inicio = datetime.fromisoformat(fecha_hora)
            # Calcula la hora de fin del evento
            hora_fin = hora_inicio + timedelta(hours=duracion)
            return f"Evento '{nombre_evento}' creado desde {hora_inicio} hasta {hora_fin}."
        except ValueError:
            # Maneja el error si la fecha y hora no tienen el formato correcto
            return "Formato de fecha y hora incorrecto. Usa el formato 'YYYY-MM-DDTHH:MM'."
