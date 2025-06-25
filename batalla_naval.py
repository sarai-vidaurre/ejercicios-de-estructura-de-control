import random
import json
import os

# Configuración
FILAS = 4
COLUMNAS = 4
NUM_BARCOS = 3
ARCHIVO_PARTIDA = "batalla_naval_save.json"

def crear_tablero():
    return [["🌊" for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("\n  " + " ".join(str(i+1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        print(chr(65+i) + " ", end="")
        for celda in fila:
            if ocultar_barcos and celda == "⛵":
                print("🌊", end=" ")
            else:
                print(celda, end=" ")
        print()

def colocar_barcos(tablero, modo, jugador=""):
    if modo == "auto":
        for _ in range(NUM_BARCOS):
            while True:
                fila = random.randint(0, FILAS-1)
                col = random.randint(0, COLUMNAS-1)
                if tablero[fila][col] == "🌊":
                    tablero[fila][col] = "⛵"
                    break
        return tablero

    print(f"\n{jugador}, coloca tus {NUM_BARCOS} barcos:")
    for i in range(1, NUM_BARCOS + 1):
        while True:
            try:
                coord = input(f"Barco {i} - Coordenada (ej. A1): ").upper()
                fila = ord(coord[0]) - 65
                col = int(coord[1:]) - 1
                if not (0 <= fila < FILAS and 0 <= col < COLUMNAS):
                    print("¡Fuera de rango! Usa A-D y 1-4.")
                    continue
                if tablero[fila][col] == "🌊":
                    tablero[fila][col] = "⛵"
                    mostrar_tablero(tablero)
                    break
                else:
                    print("¡Ya hay un barco ahí!")
            except:
                print("Formato inválido. Usa formato como A1, B2, etc.")
    return tablero

def realizar_disparo(tablero, jugador):
    while True:
        try:
            coord = input(f"{jugador}, disparo (A1) o escribe GUARDAR: ").upper()
            if coord == "GUARDAR":
                return "guardar"
            fila = ord(coord[0]) - 65
            col = int(coord[1:]) - 1
            if not (0 <= fila < FILAS and 0 <= col < COLUMNAS):
                print("¡Coordenadas inválidas!")
                continue
            if tablero[fila][col] in ["💥", "💦"]:
                print("¡Ya disparaste ahí!")
                continue
            if tablero[fila][col] == "⛵":
                tablero[fila][col] = "💥"
                print("¡Impacto! 🎯")
                return "impacto"
            else:
                tablero[fila][col] = "💦"
                print("Agua 💦")
                return "agua"
        except:
            print("Formato inválido.")

def quedan_barcos(tablero):
    return any("⛵" in fila for fila in tablero)

def guardar_partida(datos):
    with open(ARCHIVO_PARTIDA, 'w') as f:
        json.dump(datos, f)
    print("Partida guardada correctamente.")

def cargar_partida():
    if not os.path.exists(ARCHIVO_PARTIDA):
        return None
    try:
        with open(ARCHIVO_PARTIDA, 'r') as f:
            return json.load(f)
    except:
        return None

def jugar_vs_cpu():
    nombre = input("Tu nombre: ")
    jugador = nombre

    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    disparos_cpu = []

    print("\n[COLOCACIÓN DE BARCOS]")
    modo = input("¿Manual (M) o Automático (A)? ").upper()
    tablero_jugador = colocar_barcos(tablero_jugador, "manual" if modo == "M" else "auto", jugador)
    tablero_cpu = colocar_barcos(tablero_cpu, "auto")

    while True:
        print("\n[TU TABLERO]")
        mostrar_tablero(tablero_jugador)
        print("\n[TABLERO CPU]")
        mostrar_tablero(tablero_cpu, ocultar_barcos=True)

        resultado = realizar_disparo(tablero_cpu, jugador)
        if resultado == "guardar":
            guardar_partida({
                "modo": "cpu",
                "jugador": jugador,
                "tablero_jugador": tablero_jugador,
                "tablero_cpu": tablero_cpu,
                "disparos_cpu": disparos_cpu
            })
            return

        if not quedan_barcos(tablero_cpu):
            print(f"\n¡{jugador} GANASTE! 🏆")
            return

        print("\nTurno de la CPU...")
        while True:
            fila = random.randint(0, FILAS-1)
            col = random.randint(0, COLUMNAS-1)
            if (fila, col) not in disparos_cpu:
                disparos_cpu.append((fila, col))
                break

        if tablero_jugador[fila][col] == "⛵":
            tablero_jugador[fila][col] = "💥"
            print(f"CPU disparó en {chr(65+fila)}{col+1}: ¡Impacto!")
        else:
            tablero_jugador[fila][col] = "💦"
            print(f"CPU disparó en {chr(65+fila)}{col+1}: Agua 💦")

        if not quedan_barcos(tablero_jugador):
            print("\n¡LA CPU GANA! 😢")
            return

def jugar_2_jugadores():
    jugador1 = input("Nombre Jugador 1: ")
    jugador2 = input("Nombre Jugador 2: ")

    tablero1 = crear_tablero()
    tablero2 = crear_tablero()

    print(f"\n[{jugador1} COLOCA TUS BARCOS]")
    modo = input("¿Manual (M) o Automático (A)? ").upper()
    tablero1 = colocar_barcos(tablero1, "manual" if modo == "M" else "auto", jugador1)

    print(f"\n[{jugador2} COLOCA TUS BARCOS]")
    modo = input("¿Manual (M) o Automático (A)? ").upper()
    tablero2 = colocar_barcos(tablero2, "manual" if modo == "M" else "auto", jugador2)

    while True:
        print(f"\n[{jugador1} ATACA]")
        mostrar_tablero(tablero2, ocultar_barcos=True)
        if realizar_disparo(tablero2, jugador1) == "guardar":
            guardar_partida({
                "modo": "2jugadores",
                "jugador1": jugador1,
                "jugador2": jugador2,
                "tablero1": tablero1,
                "tablero2": tablero2
            })
            return
        if not quedan_barcos(tablero2):
            print(f"\n¡{jugador1} GANÓ! 🏆")
            return

        print(f"\n[{jugador2} ATACA]")
        mostrar_tablero(tablero1, ocultar_barcos=True)
        if realizar_disparo(tablero1, jugador2) == "guardar":
            guardar_partida({
                "modo": "2jugadores",
                "jugador1": jugador1,
                "jugador2": jugador2,
                "tablero1": tablero1,
                "tablero2": tablero2
            })
            return
        if not quedan_barcos(tablero1):
            print(f"\n¡{jugador2} GANÓ! 🏆")
            return

def continuar_partida():
    partida = cargar_partida()
    if not partida:
        print("No hay partida guardada.")
        return

    if partida["modo"] == "cpu":
        partida["tablero_jugador"] = [[celda for celda in fila] for fila in partida["tablero_jugador"]]
        partida["tablero_cpu"] = [[celda for celda in fila] for fila in partida["tablero_cpu"]]
        jugar_vs_cpu()
    elif partida["modo"] == "2jugadores":
        jugar_2_jugadores()

def menu_principal():
    while True:
        print("\n=== BATALLA NAVAL ===")
        print("1. Jugar vs CPU")
        print("2. Jugar 2 Jugadores")
        print("3. Continuar Partida")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar_vs_cpu()
        elif opcion == "2":
            jugar_2_jugadores()
        elif opcion == "3":
            continuar_partida()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")

# ✅ Corrección final: esta es la forma correcta
if __name__ == "__main__":
    menu_principal()
