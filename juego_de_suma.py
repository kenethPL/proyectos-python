import random

def suma_aleatoria():
    numero1 = random.randint(1, 1000)
    numero2 = random.randint(1, 1000)
    resultado_correcto = numero1 + numero2
    
    print("¡Bienvenido al juego de suma!")
    print(f"¿Cuanto es {numero1} + {numero2}?")

    while True:
        try:
            respuesta = int(input("Ingresa tu respuesta: "))
            if respuesta == resultado_correcto:
                print("¡Correcto! ¡Bien echo!")
                break
            else:
                print("Incorrecto, ingresa un numero válido.")
        except ValueError:
            print("Por favor, ingresa un número válido")

#Ejecutar el programa
__name__ == "__main__"
suma_aleatoria()