import subprocess
import sys

try:
    import psutil
except ImportError:
    print("psutil no está instalado. Comenzando Instalación...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

import socket
import platform

def obtener_informacion_sistema():
    system_info = platform.uname()
    print(f"Sistema Operativo: {system_info.system}")
    print(f"Versión: {system_info.version}")
    print(f"Arquitectura del Procesador: {system_info.machine}")

def obtener_informacion_red():
    network_info = psutil.net_if_addrs()
    print("\nInformación de Red:")
    for interface, addresses in network_info.items():
        print(f"\t{interface}:")
        for address in addresses:
            print(f"\t\t{address.family} - {address.address}")

def obtener_historial_conexiones():
    connections = psutil.net_connections(kind='inet')
    print("\nHistorial de Conexiones:")
    for conn in connections:
        print(f"\t{conn}")

def obtener_estado_disco():
    disk_usage = psutil.disk_usage("/")
    print("\nEspacio en Disco:")
    print(f"\tTotal: {disk_usage.total} bytes")
    print(f"\tUsado: {disk_usage.used} bytes")
    print(f"\tLibre: {disk_usage.free} bytes")

def main():
    while True:

        print("-------------------------------")
        print("\t\t\tMenú:")
        print("-------------------------------")
        print("1. Información del Sistema")
        print("2. Información de Red")
        print("3. Historial de Conexiones")
        print("4. Estado del Disco")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            obtener_informacion_sistema()
        elif opcion == "2":
            obtener_informacion_red()
        elif opcion == "3":
            obtener_historial_conexiones()
        elif opcion == "4":
            obtener_estado_disco()
        elif opcion == "5":
            print("")
            print("\tCreate by @alvarosalamanca")
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
