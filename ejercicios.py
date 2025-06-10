edad_str= input("Bienvenido al cine,¿cual es tu edad?:" )
edad = int(edad_str)

if edad<0:
  print("edad no valida. Por favor, ingresa un numero positivo.")
elif edad>=18:
  print("¡puedes ver peliculas clasificadas R!")
elif edad >=13:
  print ("¡pudes ver peliculas clasificadas PG-13!")
else: 
  print ("¡puedes ver la pelicula clasificada PG!")