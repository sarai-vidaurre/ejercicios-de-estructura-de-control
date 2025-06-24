def merge_sort(lista):
  # Paso Vencer (Condición base de la recursividad)
  if len(lista) <= 1:
      return lista

  # Paso 1: DIVIDIR
  medio = len(lista) // 2
  mitad_izquierda = lista[:medio]
  mitad_derecha = lista[medio:]

  # Paso 2: VENCER (ordenar recursivamente cada mitad)
  izquierda_ordenada = merge_sort(mitad_izquierda)
  derecha_ordenada = merge_sort(mitad_derecha)

  # Paso 3: COMBINAR (mezclar ambas mitades ordenadas)
  return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
  resultado = []
  i = j = 0

  # Comparar elementos y mezclar en orden
  while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
          resultado.append(izquierda[i])
          i += 1
      else:
          resultado.append(derecha[j])
          j += 1

  # Agregar los elementos restantes (si quedan)
  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])

  return resultado

# Ejemplo de uso
mi_lista = [38, 27, 43, 3, 9, 82, 10]
ordenada = merge_sort(mi_lista)
print("Lista ordenada:", ordenada)
