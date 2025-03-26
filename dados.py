import time
import random

def juego_dados():
    print("¡Bienvenido al juego de los dados!")
    print("Tienes que lanzar un dado y alcanzar un total de 20 puntos para ganar")

    puntaje = 0
    intentos = 0
    tiempo_inicio = time.time()

    while puntaje < 20:
        input("Presiona Enter para lanzar el dado...")
        dado = random.randint(1, 6)
        puntaje += dado
        intentos += 1
        print(f"sacaste un {dado}. Tu puntaje actual es {puntaje}. ")

        if puntaje >= 20:
            tiempo_fin = time.time()
            tiempo_total = round(tiempo_fin - tiempo_inicio, 2)
            print(f"¡Felicidades! Alcanzaste 20 puntos en {intentos} intentos y {tiempo_total} segundos")
            break

if __name__ == "__main__":
    juego_dados()