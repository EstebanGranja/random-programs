import re
import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(long_min=0, long_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    # Imprimir el mensaje si es que se ha escrito uno
    while True:
        texto = input("> ")
        if len(texto) >= long_min and len(texto) <= long_max:
            return texto



def dni_valido(dni, lista):
    # Formato DNI = 8 números del 1 al 9
    if not re.match('[0-9]{8}$', dni):
        print("DNI incorrecto, debe cumplir el formato")
        return False
    
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI en uso")
            return False
            
    return True

