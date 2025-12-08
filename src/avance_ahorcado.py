import random

palabras = ["python", "ahorcado", "programacion", "logica"]
palabra = random.choice(palabras)

progreso = ["_"] * len(palabra)
intentos = 6

print("=== JUEGO DEL AHORCADO (AVANCE) ===")
print(" ".join(progreso))

letra = input("Ingresa una letra: ")

if letra in palabra:
    for i in range(len(palabra)):
        if palabra[i] == letra:
            progreso[i] = letra
else:
    intentos -= 1

print("Progreso:", " ".join(progreso))
print("Intentos restantes:", intentos)

