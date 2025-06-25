# Modelo 1: Canción
cancion = {
    "titulo": "Caminando bajo la lluvia",
    "artista": "Luna Morada",
    "album": "Sueños Acuáticos",
    "duracion_segundos": 245,
    "genero": "Indie Pop",
    "colaboradores": ["Nico Beat", "Valeria Flow"],
    "fecha_lanzamiento": "2023-11-15",
    "reproducciones": 358726
}

# Modelo 2: Coche
coche = {
    "marca": "Toyota",
    "modelo": "Corolla Hybrid",
    "año": 2021,
    "color": "Azul Medianoche",
    "placa": "CBZ-854",
    "kilometraje": 32500,
    "dueños_previos": 1,
    "servicios_regulares": ["2022-06-01", "2023-01-15", "2023-12-05"],
    "electricidad": True
}

# Modelo 3: Post de Red Social
post = {
    "id_post": 304,
    "autor": "Harumi",
    "contenido_texto": "¡Hoy perdi el miedo a postear mi primer libro!  #book #feliz",
    "lista_de_likes": ["lucas_dev", "ani.lu", "mariox23", "sofia_dsg"],
    "fecha_publicacion": "2025-06-24",
    "comentarios": [
        {"usuario": "lucas_dev", "comentario": "¡Esooo! ¡Felicidades!" },
        {"usuario": "ani.lu", "comentario": "Qué crack, Harumi!"}
    ],
    "publicado_desde": "Web"
}

# Función para imprimir diccionarios con formato
def imprimir_diccionario(titulo, diccionario):
    print(f"\n--- {titulo} ---")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

# Mostrar cada modelo
imprimir_diccionario("Canción", cancion)
imprimir_diccionario("Coche", coche)
imprimir_diccionario("Post de Red Social", post)
