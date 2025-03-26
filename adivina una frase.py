import time
import random

def juego_adivina_palabra():
    palabras = ["pyton", "computadora", "programación", "teclado", "raton"]
    palabra_secreta = random.choice(palabras)
    intentos = 0
    tiempo_inicio = time.time()

    print("Bienvenido al juego de adivinanza de palabras")
    print("Debes adivinar la palabra secreta por la letra")

    progreso = ["_" for _ in palabra_secreta]

    while "".join(progreso) != palabra_secreta:
        print(" ".join(progreso))
        letra = input("Introduce una letra: ").lower()
        intentos += 1

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                  progreso[i] = letra
        else:
            print("Letra incorrecta, intenta de nuevo.")
    
    tiempo_fin = time.time()
    tiempo_total = round(tiempo_fin - tiempo_inicio, 2)
    print(f"¡Felicidades! Adivinaste la palabra'{palabra_secreta}' en {intentos} intentos y  {tiempo_total} seguntos." )

#Ejecutar el juego
if __name__ == "__main__":
    juego_adivina_palabra()

