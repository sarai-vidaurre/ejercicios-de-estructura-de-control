notas_parciales = [80, 95, 73, 60, 88]
primera_nota = notas_parciales[0] # Índice 0 para el PRIMER elemento
print(f"La primera nota fue: {primera_nota}") # Imprimirá 80
tercera_nota = notas_parciales[2] # Índice 2 para el TERCER elemento
print(f"La tercera nota fue: {tercera_nota}") # Imprimirá 73

print(f"Lista original: {notas_parciales}")
# Supongamos que se recalificó el 4to parcial (índice 3)
notas_parciales[3] = 65 # Asignamos un nuevo valor al índice 3
print(f"Lista modificada: {notas_parciales}")

cantidad_de_notas = len(notas_parciales)
print(f"Tenemos un total de {cantidad_de_notas} notas.") # Imprimirá 5

mis_hobies = ["cantar", "jugar", "escribir"]
print (f"Lista original: {mis_hobies}" " Sarai, yo tengo 3 hobbies")