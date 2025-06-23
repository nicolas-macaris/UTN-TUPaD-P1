# 1) Dado el diccionario precios_frutas
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
# 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# 
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300
# 
# print(precios_frutas)
# 
#################################################################
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
# 
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800
# 
#################################################################
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
# 
# frutas = list(precios_frutas.keys())
# print(frutas)
# 
#################################################################
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# 
# contactos = {}
# def cargar_contacto():
#     nombre = input("Ingrese el nombre del contacto: ")
#     telefono = input("Ingrese el número de teléfono: ")
#     contactos[nombre] = telefono

# def consultar_contactos():
#     nombre = input("Ingrese el nombre del contacto a consultar: ")
#     if nombre in contactos:
#         print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
#     else:
#         print("Contacto no encontrado.")

# for _ in range(5):
#     cargar_contacto()
# consultar_contactos()
# 
#################################################################
# 5) Solicita al usuario una frase e imprime:
#     • Las palabras únicas (usando un set).
#     • Un diccionario con la cantidad de veces que aparece cada palabra.
# frase = input("Ingrese una frase: ")
# palabras = frase.split()
# palabras_unicas = set(palabras)
# conteo_palabras = {}
# for palabra in palabras:
#     if palabra in conteo_palabras:
#         conteo_palabras[palabra] += 1
#     else:
#         conteo_palabras[palabra] = 1
# print("Palabras únicas:", palabras_unicas)
# print("Conteo de palabras:", conteo_palabras)
#
#################################################################
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno
# 
# alumnos = {}
# 
# for _ in range(3):
#     nombre = input("Ingrese el nombre del alumno: ")
#     notas = []
#     for i in range(3):
#         nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
#         notas.append(nota)
#     promedio = sum(notas) / len(notas)
#     alumnos[nombre] = {"notas": tuple(notas), "promedio": promedio}
# 
# for alumno in alumnos:
#     print(f"El promedio de {alumno} es: {alumnos[alumno]['promedio']:.2f}")
# 
#################################################################
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
#     • Mostrá los que aprobaron ambos parciales.
#     • Mostrá los que aprobaron solo uno de los dos.
#     • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
# 
# parcial1 = {"Ana", "Luis", "Carlos", "María"}
# parcial2 = {"Carlos", "María", "Julián", "Sofía"}
# 
# ambos = parcial1 & parcial2
# solo_uno = parcial1 ^ parcial2
# al_menos_uno = parcial1 | parcial2
# 
# print(f"Aprobaron ambos parciales: {ambos}")
# print(f"Aprobaron solo uno de los dos: {solo_uno}")
# print(f"Total de estudiantes que aprobaron al menos un parcial: {al_menos_uno}")
# 
#################################################################
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
#     • Consultar el stock de un producto ingresado.
#     • Agregar unidades al stock si el producto ya existe.
#     • Agregar un nuevo producto si no existe.
# 
# productos = {'Manzanas': 50, 'Peras': 30, 'Naranjas': 10}
# def consultar_stock():
#     producto = input("Ingrese el nombre del producto a consultar: ")
#     if producto in productos:
#         print(f"Stock de {producto}: {productos[producto]}")
#     else:
#         print(f"{producto} no existe en el inventario.")
# 
# def agregar_stock():
#     producto = input("Ingrese el nombre del producto a agregar: ")
#     if producto in productos:
#         unidades = int(input(f"Ingrese la cantidad de unidades a agregar a {producto}: "))
#         productos[producto] += unidades
#         print(f"Nuevo stock de {producto}: {productos[producto]}")
#     else:
#         unidades = int(input(f"{producto} no existe. Ingrese la cantidad de unidades para agregarlo: "))
#         productos[producto] = unidades
#         print(f"{producto} agregado con un stock de {unidades} unidades.")
# 
# def menu():
#     print("Ingrese una opcion:")
#     print("1. Consultar stock de un producto")
#     print("2. Agregar unidades al stock de un producto")
#     print("3. Agregar un nuevo producto")
#     opcion = input("Opción: ")
#     if opcion == '1':
#         consultar_stock()
#     elif opcion == '2':
#         agregar_stock()
#     elif opcion == '3':
#         agregar_stock()
#     else:
#         print("Opción no válida. Intente nuevamente.")
# 
# menu()
# 
# #################################################################
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
# Permití consultar qué actividad hay en cierto día y hora.
# 
# agenda = {
#     ("Lunes", "10:00"): "Reunión con el equipo",
#     ("Lunes", "14:00"): "Clase de programación",
#     ("Martes", "09:00"): "Reunión con el cliente",
#     ("Miércoles", "11:00"): "Taller de desarrollo",
#     }
# 
# def consultar_evento(dia, hora):
#     evento = agenda.get((dia, hora))
#     if evento:
#         print(f"Evento el día {dia} a las {hora}: {evento}")
#     else:
#         print(f"No hay eventos programados para {dia} a las {hora}.")
# 
# input_dia = input("Ingrese el día (ejemplo: Lunes): ")
# input_hora = input("Ingrese la hora (ejemplo: 10:00): ")
# consultar_evento(input_dia, input_hora)
# 
#################################################################
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
#   • Las capitales sean las claves.
#   • Los países sean los valores.
# 
# diccionario_original = {
#     "Argentina": "Buenos Aires",
#     "Brasil": "Brasilia",
#     "Chile": "Santiago",
#     "Colombia": "Bogotá",
#     "Perú": "Lima"
#     }
# 
# diccionario_invertido = {}
# for pais, capital in diccionario_original.items():
#     diccionario_invertido[capital] = pais
# 
# print("Diccionario original:", diccionario_original)
# print("Diccionario invertido:", diccionario_invertido)
