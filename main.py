from Modulos.calendario import GestorEventos  # Clase para gestionar eventos en Google Calendar
from Modulos.clima import GestorClima  # Clase para consultar información meteorológica
from Modulos.conversionMoneda import ConvertidorMoneda  # Clase para convertir monedas
from Modulos.recordatorios import GestorRecordatorios  # Clase para gestionar recordatorios locales
from datetime import datetime  # Clase para trabajar con fechas y horas

def main():
    recordatorios = GestorRecordatorios()  # Crea una instancia de GestorRecordatorios para gestionar recordatorios
    print("¡Bienvenido al Asistente Virtual!")  # Imprime un mensaje de bienvenida

    while True:  # Bucle infinito para el menú principal
        print("\n¿Qué te gustaría hacer?")
        print("1. Crear un evento en Google Calendar")
        print("2. Eliminar un evento en Google Calendar")
        print("3. Listar eventos de Google Calendar")
        print("4. Consultar el clima")
        print("5. Convertir moneda")
        print("6. Gestionar recordatorios")
        print("7. Salir")

        opcion = input("Elige una opción (1-7): ")  # Solicita al usuario que elija una opción
        
        if opcion == "1":  # Crear un evento
            nombre_evento = input("Nombre del evento: ")  # Solicita el nombre del evento
            fecha_hora = input("Fecha y hora del evento (YYYY-MM-DDTHH:MM): ")  # Solicita la fecha y hora del evento
            duracion = int(input("Duración del evento (en horas): "))  # Solicita la duración del evento en horas
            resultado = GestorEventos.agregar_evento(nombre_evento, fecha_hora, duracion)  # Llama al método agregar_evento
            print(resultado)  # Imprime el resultado

        elif opcion == "2":  # Eliminar un evento
            evento_id = input("ID del evento a eliminar: ")  # Solicita el ID del evento a eliminar
            resultado = GestorEventos.eliminar_evento(evento_id)  # Llama al método eliminar_evento
            print(resultado)  # Imprime el resultado

        elif opcion == "3":  # Listar eventos
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")  # Solicita la fecha de inicio
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")  # Solicita la fecha de fin
            resultado = GestorEventos.listar_eventos(fecha_inicio, fecha_fin)  # Llama al método listar_eventos
            print(resultado)  # Imprime el resultado

        elif opcion == "4":  # Consultar el clima
            ciudad = input("Nombre de la ciudad: ")  # Solicita el nombre de la ciudad
            resultado = GestorClima.obtener_clima(ciudad)  # Llama al método obtener_clima
            print(resultado)  # Imprime el resultado

        elif opcion == "5":  # Convertir moneda
            try:
                monto = float(input("Monto a convertir: "))  # Solicita el monto a convertir
                moneda_origen = input("Moneda de origen (ej. USD): ").upper()  # Solicita la moneda de origen y la convierte a mayúsculas
                moneda_destino = input("Moneda de destino (ej. EUR): ").upper()  # Solicita la moneda de destino y la convierte a mayúsculas
                resultado = ConvertidorMoneda.convertir_moneda(monto, moneda_origen, moneda_destino)  # Llama al método convertir_moneda
                print(resultado)  # Imprime el resultado
            except ValueError:
                print("Monto inválido. Ingresa un número válido.")  # Maneja el error si el monto no es válido

        elif opcion == "6":  # Gestionar recordatorios
            print("\nGestión de recordatorios:")
            print("1. Añadir un recordatorio")
            print("2. Mostrar todos los recordatorios")
            print("3. Eliminar un recordatorio")
            opcion_recordatorio = input("Elige una opción (1-3): ")  # Solicita al usuario que elija una opción

            if opcion_recordatorio == "1":
                texto_recordatorio = input("Escribe el recordatorio: ")  # Solicita el texto del recordatorio
                fecha_vencimiento = input("Fecha del recordatorio (YYYY-MM-DD): ")  # Solicita la fecha de vencimiento del recordatorio
                resultado = recordatorios.añadir_recordatorio(texto_recordatorio, fecha_vencimiento)  # Llama al método añadir_recordatorio
                print(resultado)  # Imprime el resultado

            elif opcion_recordatorio == "2":
                resultado = recordatorios.mostrar_recordatorios()  # Llama al método mostrar_recordatorios
                print(resultado)  # Imprime el resultado

            elif opcion_recordatorio == "3":
                id_recordatorio = input("ID del recordatorio a eliminar: ")  # Solicita el ID del recordatorio a eliminar
                resultado = recordatorios.eliminar_recordatorio(id_recordatorio)  # Llama al método eliminar_recordatorio
                print(resultado)  # Imprime el resultado

            else:
                print("Opción no válida.")  # Maneja el caso de una opción no válida

        elif opcion == "7":  # Salir
            print("¡Gracias por usar el asistente virtual! ¡Hasta luego!")  # Imprime un mensaje de despedida
            break  # Sale del bucle

        else:
            print("Opción no válida. Intenta de nuevo.")  # Maneja el caso de una opción no válida

if __name__ == "__main__":
    main()  # Llama a la función main si el archivo es ejecutado directamente
