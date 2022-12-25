import random
def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("Ingrese una cantidad en pesos " + tipo_pesos + ": "))
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)      #reducir el numero de decimales
    print("Usted tiene $" + str(dolar) + " dolares")
def generador():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W,", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbolos = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "?", "<", ">", ",", ".", "/"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8","9" "0"]
    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        random_password = random.choice(caracteres)
        password.append(random_password)
    
    password = "".join(password)
    
    return password
def es_primo(numero):
    contador = 0 

    for i in range(1, numero + 1):

        if i == 1 or i == numero:
            continue

        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False
def run():
    while True:


        menu = (""" 
Bienvenido al menú interactivo,
estas son las funcionalidades hasta el momento:

1 - Conversor de pesos a dolares
2 - Generador de contraseña aleatoria
3 - Minijuego 
4 - Determinador de numeros primos
5 - Salir
        
Que desea hacer? elija una opción: """)

        opcion = int(input(menu))

        if opcion == 1:
            conversor("argentinos", 294)

            volver = input("Quiere volver al menu?: ")
            if volver == "no":
                print("Muchas gracias por usarme, saludos! :D")
                break
        elif opcion == 2:
            password = generador()
            print("Su contraseña aleatoria generada es " + password )
            volver = input("Quiere volver al menu?: ")
            if volver == "no":
                print("Muchas gracias por usarme, saludos! :D")
                break
        elif opcion == 3:
            vidas = 5
            numero_random = random.randint(1, 100)
            numero_elegido = int(input("Juguemos un juego, elige un numero del 1 al 100, tenes 5 vidas:  "))

            while numero_elegido != numero_random:

                vidas = vidas-1
                if vidas == 0:
                    print(">>> PERDISTE <<<")
                    print("El numero era " + str(numero_random))
                    break

                if numero_elegido < numero_random:
                    print("Prueba con un numero mas alto")

                else:
                    print("Prueba con un numero mas bajo")
    

                print("Te quedan " + str(vidas) + " vidas")
        
                numero_elegido = int(input("intenta de nuevo: "))

            else:
                print(">>> Ganaste! sos GOD <<<")

            volver = input("Quiere volver al menu?: ")
            if volver == "no":
                print("Muchas gracias por usarme, saludos! :D")
                break
        
        elif opcion == 4:
            numero = int(input("Ingrese un numero para saber si es primo o no: "))
            if es_primo(numero):
                print(str(numero)+ " es un numero primo")
            else:
                print(str(numero) + " no es un numero primo")
            volver = input("Quiere volver al menu?: ")
            if volver == "no":
                print("Muchas gracias por usarme, saludos! :D")
                break
        elif opcion == 5:
            print("Adios! espero haberte ayudado")
            break
        else: 
            print("Opcion no valida!, vamos de nuevo...")



            

    


if __name__ == "__main__":
    run()