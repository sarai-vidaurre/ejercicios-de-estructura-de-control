# Crear una lista vacía
inventario = []

#Diccionarios de productos
producto1 = {
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "stock": 50
}

producto2 = {
    "nombre": "Café de los Yungas",
    "stock": 100
}

producto3 = {
    "nombre": "Quinua Real en Grano",
    "stock": 80
}

# Añadir productos a la lista
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# imprimir el inventario
print("Cantidad de productos en el inventario:", len(inventario))

#el resumen del inventario
print("--- Inventario Actual ---")
for producto in inventario:
    nombre = producto["nombre"]
    stock = producto["stock"]
    print(f"- {nombre}: {stock} unidades en stock.")
print("-------------------------")
print("fin del programa Sarai Vidaurre")