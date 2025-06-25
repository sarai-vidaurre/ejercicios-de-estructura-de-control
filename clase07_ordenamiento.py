def ordenamiento_burbuja(lista):
  n = len(lista)
  for i in range(n - 1) :
    hubo_intercambio = False
    for j in range(n - 1 - i):
      if lista[j] > lista[j + 1]:
        #intercambio
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        hubo_intercambio = True
    if not hubo_intercambio:
      break
  return lista
if __name__ == "__main__":
  numeros = [6,3,8,2,5]
  print("antes", numeros)
  ordenamiento_burbuja(numeros)
  print("despues", numeros)


#codigo 2
lista_a_ordenar = [64,34,25,12,22,11,90]
print(f"lista original: {lista_a_ordenar}")

ordenamiento_burbuja(lista_a_ordenar) #llamamos la funcion
print(f"lista ordenada: {lista_a_ordenar}")

#caso 1: lista desordenada
lista1 = [6,3,8,2,5]
ordenamiento_burbuja(lista1)
assert lista1 == [2,3,5,6,8], "Fallo en caso 1"

#caso 2: lista ya ordenada
lista2 = [1,2,3,4,5]
ordenamiento_burbuja(lista2)
assert lista2 == [1,2,3,4,5], "Fallo en caso 2"

#caso 3: lista ordenanda a la inversa(por caso)
lista3 = [5,4,3,2,1]
ordenamiento_burbuja(lista3)
assert lista3 == [1,2,3,4,5], "Fallo en caso 3"

#caso 4: lista con elementos duplicados
lista4 = [5,1,4,2,8,5,2]
ordenamiento_burbuja(lista4)
assert lista4 == [1,2,2,4,5,5,8], "fallo en caso 4"

#caso borde
assert ordenamiento_burbuja([]) == []
assert ordenamiento_burbuja([42]) == [42], "fallo en caso borde"


print ("todas las pruebas pasaron")
print ("fin del programa Sarai Vidaurre")

