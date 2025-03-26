import time
import random

def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    inicio_tiempo = time.time()
    
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
    while True:
        try:
            intento = int(input("Ingresa tu número: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                fin_tiempo = time.time()
                tiempo_total = round(fin_tiempo - inicio_tiempo, 2)
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos y {tiempo_total} segundos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el juego
if __name__ == "__main__":
    adivina_numero()
