# 1. Crear una nueva sala de cine
def crear_sala(filas, columnas):
    """
    Crea una matriz con 'L' (Libre) en todas las posiciones.
    """
    return [['L' for _ in range(columnas)] for _ in range(filas)]

# 2. Mostrar la sala de forma visual
def mostrar_sala(sala):
    """
    Imprime la sala como una cuadrícula bonita con encabezados.
    """
    print("\n    " + "  ".join([f"C{j}" for j in range(len(sala[0]))]))
    print("   " + "---" * len(sala[0]))
    for i, fila in enumerate(sala):
        print(f"F{i} | " + "  ".join(fila))
    print()

# 3. Ocupar un asiento
def ocupar_asiento(sala, fila, columna):
    """
    Intenta ocupar el asiento (fila, columna).
    Retorna True si lo logra, False si no.
    """
    filas = len(sala)
    columnas = len(sala[0])

    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        print("⚠️ Error: ¡Coordenadas fuera de rango!")
        return False

    if sala[fila][columna] == 'O':
        print("❌ El asiento ya está ocupado.")
        return False

    sala[fila][columna] = 'O'
    print(f"✅ Asiento F{fila} C{columna} ocupado con éxito.")
    return True

# 4. (Opcional) Contar asientos libres
def contar_asientos_libres(sala):
    """
    Cuenta cuántos asientos 'L' hay en la sala.
    """
    return sum(fila.count('L') for fila in sala)

# --- Prueba del sistema ---
sala = crear_sala(5, 6)  # 5 filas, 6 columnas
mostrar_sala(sala)

ocupar_asiento(sala, 1, 2)
ocupar_asiento(sala, 4, 5)
ocupar_asiento(sala, 1, 2)  # Intentar ocupar uno ya ocupado
ocupar_asiento(sala, 7, 1)  # Coordenadas inválidas

mostrar_sala(sala)
print(f"Asientos libres restantes: {contar_asientos_libres(sala)}")
