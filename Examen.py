import csv
from datetime import datetime
from tabulate import tabulate

ARCHIVO = "equipos_control.csv"

def crear_equipo():
    with open(ARCHIVO, mode="a", newline="") as file:
        writer = csv.writer(file)
        id_equipo = int(input("ID del equipo: "))
        nombre = input("Nombre del equipo: ")
        tipo = input("Tipo de equipo (Sensor, Actuador, PLC): ")
        valor_cal = float(input("Valor de calibración: "))
        fecha_mantenimiento = input("Fecha de último mantenimiento (AAAA-MM-DD): ")
        writer.writerow([id_equipo, nombre, tipo, valor_cal, fecha_mantenimiento])
        print("Equipo agregado correctamente.")

def listar_equipos():
    try:
        with open(ARCHIVO, mode="r") as file:
            reader = csv.reader(file)
            equipos = [row for row in reader]
            print(tabulate(equipos, headers=["ID", "Nombre", "Tipo", "Valor Calibración", "Último Mantenimiento"], tablefmt="grid"))
    except FileNotFoundError:
        print("No se encontró el archivo de equipos.")

def buscar_por_id():
    try:
        with open(ARCHIVO, mode="r") as file:
            reader = csv.reader(file)
            equipos = list(reader)
            id_buscar = input("Ingrese el ID del equipo: ")
            for equipo in equipos:
                if equipo[0] == id_buscar:
                    print(tabulate([equipo], headers=["ID", "Nombre", "Tipo", "Valor Calibración", "Último Mantenimiento"], tablefmt="grid"))
                    return
            print("Equipo no encontrado.")
    except FileNotFoundError:
        print("No se encontró el archivo.")

def equipos_por_tipo():
    try:
        tipo_buscar = input("Ingrese el tipo de equipo: ")
        with open(ARCHIVO, mode="r") as file:
            reader = csv.reader(file)
            equipos = [row for row in reader if row[2].lower() == tipo_buscar.lower()]
            if equipos:
                print(tabulate(equipos, headers=["ID", "Nombre", "Tipo", "Valor Calibración", "Último Mantenimiento"], tablefmt="grid"))
            else:
                print("No se encontraron equipos de ese tipo.")
    except FileNotFoundError:
        print("No se encontró el archivo.")

def equipos_mantenimiento_rango():
    try:
        inicio = datetime.strptime(input("Fecha inicio (AAAA-MM-DD): "), "%Y-%m-%d")
        fin = datetime.strptime(input("Fecha fin (AAAA-MM-DD): "), "%Y-%m-%d")
        with open(ARCHIVO, mode="r") as file:
            reader = csv.reader(file)
            equipos = []
            for row in reader:
                fecha_mant = datetime.strptime(row[4], "%Y-%m-%d")
                if inicio <= fecha_mant <= fin:
                    equipos.append(row)
            if equipos:
                print(tabulate(equipos, headers=["ID", "Nombre", "Tipo", "Valor Calibración", "Último Mantenimiento"], tablefmt="grid"))
            else:
                print("No hay equipos en ese rango de fechas.")
    except FileNotFoundError:
        print("No se encontró el archivo.")
    except ValueError:
        print("Error en formato de fecha.")

def menu():
    while True:
        print("\n=== Gestión de Equipos de Control ===")
        print("1. Agregar equipo")
        print("2. Listar equipos")
        print("3. Buscar por ID")
        print("4. Buscar por tipo (índice)")
        print("5. Equipos por rango de mantenimiento")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_por_id()
        elif opcion == "4":
            equipos_por_tipo()
        elif opcion == "5":
            equipos_mantenimiento_rango()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

menu()