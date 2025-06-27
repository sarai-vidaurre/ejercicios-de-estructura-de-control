# Desafío de Programación Orientada a Objetos
#Instrucciones: Implementa una clase CarritoDeCompras en Python y sube el PDF de la captura de pantalla como el documento de los ejercicios prácticos. Considera que tu programa cumpla con los siguientes requisitos, basándote en los conceptos de POO presentados.
#Requisitos:
#La clase debe tener un constructor __init__ que inicialice un atributo self.productos como una lista vacía.
#Debe tener un método agregar_producto(self, producto) que reciba un diccionario producto y lo añada a la lista self.productos. El producto tendrá claves como "nombre" y "precio"
#Debe tener un método calcular_total(self) que recorra la lista de productos y devuelva la suma de todos sus precios
#Debe tener un método mostrar_carrito(self) que imprima de forma clara cada producto en el carrito y el total final.

class CarritoDeCompras:
  #primero se crea el constructor
  def __init__(self):
      self.productos = []
#se crea la lista de productos
  def agregar_producto(self, producto):
      # Agregamos el producto a la lista
      self.productos.append(producto)
#creamos la función para calcular el total para la gastación
  def calcular_total(self):
      # Sumamos los precios de todos los productos
      total = 0
      for producto in self.productos:
          total += producto["precio"]
      return total
#creamos la función para mostrar el carrito de la gastación y ver que productos se compraron
  def mostrar_carrito(self):
      # Mostramos todos los productos
      if not self.productos:
        #si esta vacio el carrito de la gastación, se imprime que esta vacio
          print("El carrito está vacío.")
          return
#sino se imprime los productos que se compraron
      print("Productos en el carrito:")
      for producto in self.productos:
          print("- Nombre:", producto["nombre"])
          print("  Precio:   Bs", producto["precio"])
#en bolivianitos por que no hay dolares :(
      total = self.calcular_total()
      print("Total a pagar: Bs", total)
      print("ni modo a pagar y fin de la gastación")
      print("gracias por usar el carrito de la gastación")
      print("fin del programa Sarai Vidaurre")

#creamos el carrito de la gastación
carrito = CarritoDeCompras()

#Colocamos los productos con sus respectivos precios y lloramos por que esta caro
producto1 = {"nombre": "Pan", "precio": 2.5}
producto2 = {"nombre": "Leche", "precio": 7.5}
producto3 = {"nombre": "Huevos", "precio": 10}
producto4 = {"nombre": "Carne", "precio": 70}
producto5 = {"nombre": "papa", "precio": 50}
producto6 = {"nombre": "arroz", "precio": 10}
producto7 = {"nombre": "cebolla", "precio": 45.5}
# Agregamos productos al carrito de la gastación
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)
carrito.agregar_producto(producto4)
carrito.agregar_producto(producto5)
carrito.agregar_producto(producto6)
carrito.agregar_producto(producto7)
# Mostramos el carrito de la gastación
carrito.mostrar_carrito()
