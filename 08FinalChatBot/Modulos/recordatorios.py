from datetime import datetime, timedelta

class GestorRecordatorios:
    def __init__(self):
        self.recordatorios = []  # Lista para almacenar los recordatorios

    def añadir_recordatorio(self, texto, fecha_vencimiento):
        """
        Añade un recordatorio a la lista.
        """
        try:
            # Verifica que la fecha tenga el formato correcto
            datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
            # Añade el recordatorio a la lista
            self.recordatorios.append({"texto": texto, "fecha_vencimiento": fecha_vencimiento})
            return f"Recordatorio añadido: '{texto}' para {fecha_vencimiento}."
        except ValueError:
            # Maneja el error si la fecha no tiene el formato correcto
            return "Formato de fecha incorrecto. Usa el formato 'YYYY-MM-DD'."

    def mostrar_recordatorios(self):
        """
        Muestra todos los recordatorios.
        """
        if self.recordatorios:
            resultado = "Tus recordatorios:\n"
            for idx, recordatorio in enumerate(self.recordatorios, start=1):
                # Formatea cada recordatorio para mostrarlo
                resultado += f"{idx}. {recordatorio['texto']} - Fecha: {recordatorio['fecha_vencimiento']}\n"
            return resultado
        else:

            return "No tienes recordatorios."