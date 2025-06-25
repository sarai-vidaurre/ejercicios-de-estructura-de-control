# --- Funciones del sistema ---

def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    print("\n    " + "  ".join([f"C{j}" for j in range(len(sala[0]))]))
    print("   " + "---" * len(sala[0]))
    for i, fila in enumerate(sala):
        print(f"F{i} | " + "  ".join(fila))
    print()

def ocupar_asiento(sala, fila, columna):
    filas = len(sala)
    columnas = len(sala[0])
    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        print("⚠️ Coordenadas fuera de rango.")
        return False
    if sala[fila][columna] == 'O':
        print("❌ Ese asiento ya está ocupado.")
        return False
    sala[fila][columna] = 'O'
    print(f"✅ Asiento F{fila} C{columna} ocupado correctamente.")
    return True

# --- Programa Principal ---

sala = crear_sala(5, 8)  # Sala de 5 filas x 8 columnas

while True:
    mostrar_sala(sala)
    print("🎟️  MENÚ DE OPCIONES")
    print("1. Ocupar un asiento")
    print("0. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        try:
            fila = int(input("Ingresa la fila del asiento (ej. 0 a 4): "))
            columna = int(input("Ingresa la columna del asiento (ej. 0 a 7): "))
            ocupar_asiento(sala, fila, columna)
        except ValueError:
            print("❗Por favor, ingresa números válidos.")
    elif opcion == '0':
        print("🎬 ¡Gracias por usar el sistema de cine! Hasta luego.")
        break
    else:
        print("❗Opción inválida. Intenta de nuevo.")
