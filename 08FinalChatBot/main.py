from Modulos.calendario import GestorEventos
from Modulos.clima import GestorClima
from Modulos.conversionMoneda import ConvertidorMoneda
from Modulos.recordatorios import GestorRecordatorios

def main():
    recordatorios = GestorRecordatorios()  # Instancia para gestionar recordatorios
    print("¡Bienvenido al Asistente Virtual!")

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Crear un evento en Google Calendar")
        print("2. Consultar el clima")
        print("3. Convertir moneda")
        print("4. Gestionar recordatorios")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            nombre_evento = input("Nombre del evento: ")
            fecha_hora = input("Fecha y hora del evento (YYYY-MM-DDTHH:MM): ")
            duracion = int(input("Duración del evento (en horas): "))
            resultado = GestorEventos.agregar_evento(nombre_evento, fecha_hora, duracion)
            print(resultado)

        elif opcion == "2":
            ciudad = input("Nombre de la ciudad: ")
            resultado = GestorClima.obtener_clima(ciudad)
            print(resultado)

        elif opcion == "3":
            try:
                monto = float(input("Monto a convertir: "))
                moneda_origen = input("Moneda de origen (ej. USD): ").upper()
                moneda_destino = input("Moneda de destino (ej. EUR): ").upper()
                resultado = ConvertidorMoneda.convert_currency(monto, moneda_origen, moneda_destino)
                print(resultado)
            except ValueError:
                print("Monto inválido. Ingresa un número válido.")

        elif opcion == "4":
            print("\nGestión de recordatorios:")
            print("1. Añadir un recordatorio")
            print("2. Mostrar todos los recordatorios")
            opcion_recordatorio = input("Elige una opción (1-2): ")

            if opcion_recordatorio == "1":
                texto_recordatorio = input("Escribe el recordatorio: ")
                fecha_vencimiento = input("Fecha del recordatorio (YYYY-MM-DD): ")
                resultado = recordatorios.añadir_recordatorio(texto_recordatorio, fecha_vencimiento)
                print(resultado)

            elif opcion_recordatorio == "2":
                resultado = recordatorios.mostrar_recordatorios()
                print(resultado)

            else:
                print("Opción no válida.")

        elif opcion == "5":
            print("¡Gracias por usar el asistente virtual! ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

