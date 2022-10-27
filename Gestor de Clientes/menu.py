import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("==========================")
        print(">> Bienvenido al Gestor <<")
        print("==========================")
        print("[1]  Mostrar los clientes |")
        print("[2]  Buscar un cliente    |")
        print("[3]  Añadir un cliente    |")
        print("[4]  Modificar un cliente |")
        print("[5]  Borrar un cliente    |")
        print("[6]  SALIR                |")
        print("==========================")
        
        opcion = input("> ")
        
        helpers.limpiar_pantalla()

        if opcion == "1":
            print("Mostrando los clientes...")
            for cliente in db.Clientes.lista:
                print(cliente)

        elif opcion == "2":
            print("Buscando un cliente...")
            dni = helpers.leer_texto(8, 8, "DNI (8 int)")
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")

        elif opcion == "3":
            print("Añadiendo un cliente...")

            dni = None      # buena práctica
            while True:
                dni = helpers.leer_texto(8, 8, "DNI (8 int)")
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break 

            nombre = helpers.leer_texto(2, 30, "Nombre (2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")


        elif opcion == "4":
            print("Modificando un cliente...")
            dni = helpers.leer_texto(8, 8, "DNI (8 int)")
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")


        elif opcion == "5":
            print("Borrando un cliente...")
            dni = helpers.leer_texto(8, 8, "DNI (8 int)")
            print("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado")


        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opcion no válida.")
    

        input("Presiona ENTER para continuar")