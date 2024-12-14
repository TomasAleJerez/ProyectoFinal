class GestorRecordatorios:
    archivo_recordatorios = "recordatorios.txt"  # Nombre del archivo de texto donde se guardarán los recordatorios

    @staticmethod
    def añadir_recordatorio(texto_recordatorio, fecha_vencimiento):
        """
        Añade un recordatorio al archivo .txt.
        """
        try:
            with open(GestorRecordatorios.archivo_recordatorios, "a") as archivo:
                archivo.write(f"{fecha_vencimiento}: {texto_recordatorio}\n")  # Guarda el recordatorio con la fecha
            return "Recordatorio añadido con éxito."
        except Exception as e:
            return f"Error al añadir el recordatorio: {e}"

    @staticmethod
    def mostrar_recordatorios():
        """
        Muestra todos los recordatorios guardados en el archivo .txt.
        """
        try:
            with open(GestorRecordatorios.archivo_recordatorios, "r") as archivo:
                recordatorios = archivo.readlines()
            if not recordatorios:
                return "No hay recordatorios almacenados."
            return "".join(recordatorios)  # Devuelve los recordatorios como un string
        except FileNotFoundError:
            return "No se ha encontrado el archivo de recordatorios. Puede que no haya recordatorios guardados aún."
        except Exception as e:
            return f"Error al leer los recordatorios: {e}"
