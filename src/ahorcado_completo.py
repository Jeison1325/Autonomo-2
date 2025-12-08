# JUEGO COMPLETO DEL AHORCADO
# Autor: Jeison Andrés Serrano

import random

def seleccionar_palabra():
    palabras = ["python", "ahorcado", "programacion", "logica", "software"]
    return random.choice(palabras)

def mostrar_progreso(progreso):
    print(" ".join(progreso))

def jugar():
    palabra = seleccionar_palabra()
    progreso = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []

    print("=== JUEGO DEL AHORCADO ===")

    while intentos > 0:
        mostrar_progreso(progreso)
        print(f"Intentos restantes: {intentos}")
        print("Letras usadas:", letras_usadas)

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_usadas:
            print("Ya usaste esa letra, intenta otra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            print("¡Correcto!")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    progreso[i] = letra
        else:
            print("Incorrecto.")
            intentos -= 1

        if "_" not in progreso:
            print("\n¡Ganaste! La palabra era:", palabra)
            return

    print("\nPerdiste... La palabra era:", palabra)

jugar()


