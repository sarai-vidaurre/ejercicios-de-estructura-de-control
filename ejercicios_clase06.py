# clase06_busquedas.py
# clase06_busquedas.py
# 1. Definir la función busqueda_lineal
def busqueda_lineal(lista, elemento_buscado):
    for i in range(len(lista)):
        if lista[i] == elemento_buscado:
            return i
            # Si el elemento no está en la lista, devolver -1
    return -1
# ... (definición de la función aquí arriba) ...
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("Probando busqueda_lineal...")
assert busqueda_lineal(mi_lista_desordenada, 42) == 2
assert busqueda_lineal(mi_lista_desordenada, 10) == 0 # Al inicio
assert busqueda_lineal(mi_lista_desordenada, 25) == 6 # Al final
assert busqueda_lineal(mi_lista_desordenada, 99) == -1 # No existe
assert busqueda_lineal([], 5) == -1
print("¡Pruebas para busqueda_lineal pasaron! ")

# 2. Definir la función busqueda_binaria
#definicion de funcion
def busqueda_binaria(lista, elemento_buscado):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento_buscado:
            return medio
        elif lista[medio] < elemento_buscado:
             izquierda = medio + 1
        else:
                 derecha = medio - 1
            # Si el elemento no está en la lista, devolver -1
    return -1
    #pruba de busqueda binaria
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\nProbando busqueda_binaria...")
assert busqueda_binaria(lista_ordenada, 23) == 5
assert busqueda_binaria(lista_ordenada, 91) == 9 # Último
assert busqueda_binaria(lista_ordenada, 2) == 0 # Primero
assert busqueda_binaria(lista_ordenada, 3) == -1 # No existe
assert busqueda_binaria(lista_ordenada, 100) == -1 # Fuera de rango (mayor)
print("¡Pruebas para busqueda_binaria pasaron! ")


#Prueba del caos
print("\nRealizando el experimento del caos...")
# Definimos una lista desordenada
# y buscamos un elemento en ella usando búsqueda binaria
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
# Buscamos el 5. Sabemos que está en la lista.
# ¿Qué devolverá la búsqueda binaria?
resultado_caos = busqueda_binaria(mi_lista_desordenada, 5)
# Imprimimos el resultado
print("Resultado del experimento del caos:", resultado_caos) # Probablemente devuelva -1 (fallo), o un índice incorrecto.
# Probablemente devuelva -1 (fallo), o un índice incorrecto.