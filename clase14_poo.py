# clase14_poo.py

class Libro:
    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.disponible = True  # atributo extra por defecto

    def mostrar_info(self):
        print("📚 Información del Libro 📚")
        print(f"Título     : {self.titulo}")
        print(f"Autor      : {self.autor}")
        print(f"ISBN       : {self.isbn}")
        print(f"Páginas    : {self.paginas}")
        print(f"Disponible : {'Sí' if self.disponible else 'No'}")

# Ejemplo de uso (no te preocupes por crear objetos todavía, ¡solo define la clase!)
if __name__ == "__main__":
    # Creación de ejemplo para demostrar el funcionamiento
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
    libro1.mostrar_info()

    # Cambiar disponibilidad
    libro1.disponible = False
    print("\nDespués de cambiar disponibilidad:")
    libro1.mostrar_info()

print("¡Clase Libro definida correctamente!")
print("Fin del archivo clase14_poo.py Sarai Vidaurre")