"""Adivina el número - juego de consola en Python.

La computadora elige un número secreto y el jugador debe adivinarlo
con las menos pruebas posibles. Hay tres niveles de dificultad y el
mejor resultado de cada nivel se guarda en un archivo JSON.
"""

import json
import os
import random

ARCHIVO_RECORDS = "records.json"

# nivel: (nombre, número máximo, intentos permitidos)
NIVELES = {
    "1": ("Fácil", 20, 7),
    "2": ("Medio", 50, 7),
    "3": ("Difícil", 100, 6),
}


def cargar_records():
    """Devuelve el diccionario de récords (vacío si no existe el archivo)."""
    if not os.path.exists(ARCHIVO_RECORDS):
        return {}
    with open(ARCHIVO_RECORDS, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_records(records):
    with open(ARCHIVO_RECORDS, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


def elegir_nivel():
    print("\nElige la dificultad:")
    for clave, (nombre, maximo, intentos) in NIVELES.items():
        print(f"  {clave}. {nombre} (número entre 1 y {maximo}, {intentos} intentos)")
    while True:
        opcion = input("Opción: ").strip()
        if opcion in NIVELES:
            return NIVELES[opcion]
        print("Opción no válida.")


def pedir_numero(maximo):
    """Pide un número entero entre 1 y maximo."""
    while True:
        texto = input("Tu número: ").strip()
        if texto.isdigit() and 1 <= int(texto) <= maximo:
            return int(texto)
        print(f"Escribe un número entero entre 1 y {maximo}.")


def jugar(records):
    nombre, maximo, intentos_max = elegir_nivel()
    secreto = random.randint(1, maximo)
    print(f"\nPensé un número entre 1 y {maximo}. ¡Tienes {intentos_max} intentos!")

    for intento in range(1, intentos_max + 1):
        print(f"\nIntento {intento}/{intentos_max}")
        numero = pedir_numero(maximo)
        if numero == secreto:
            print(f"🎉 ¡Correcto! Lo lograste en {intento} intento(s).")
            mejor = records.get(nombre)
            if mejor is None or intento < mejor:
                records[nombre] = intento
                guardar_records(records)
                print("🏆 ¡Nuevo récord en este nivel!")
            return
        pista = "mayor" if secreto > numero else "menor"
        print(f"❌ No es. El número secreto es {pista}.")

    print(f"\n😢 Se acabaron los intentos. El número era {secreto}.")


def mostrar_records(records):
    if not records:
        print("\nAún no hay récords. ¡Juega una partida!")
        return
    print("\n🏆 Mejores resultados (menos intentos):")
    for nombre, intentos in records.items():
        print(f"  {nombre}: {intentos} intento(s)")


def menu():
    records = cargar_records()
    while True:
        print("\n=== ADIVINA EL NÚMERO ===")
        print("1. Jugar")
        print("2. Ver récords")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            jugar(records)
        elif opcion == "2":
            mostrar_records(records)
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
