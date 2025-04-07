# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
# 
# edadUsuario = int(input("Ingrese su edad: "))
# if (edadUsuario > 18):
#     print("Es mayor de edad")
# 
#########################################
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”
# 
# notaUsuario = int(input("Ingrese la nota: "))
# if (notaUsuario >= 6):
#     print("Aprobado")
# else:
#   print("Desaprobado")
# 
##########################################
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
# 
# numeroUsuario = int(input("Ingrese un numero par: "))
# if (numeroUsuario % 2 == 0):
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")
# 
###########################################
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
# 
# edadUsuario = int(input("Ingrese su edad: "))
# if (12 > edadUsuario > 0):
#     print("Usted es un/a niño/a")
# elif (18 > edadUsuario >= 12):
#     print("Usted es adolescente")
# elif (30 > edadUsuario >= 18):
#     print("Usted es adulto/a joven")
# elif (edadUsuario >= 30):
#     print("Usted es adulto/a")
# else:
#     print("Ingrese una edad válida")
# 
###########################################
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
# 
# claveUsuario = input("Por favor ingrese su clave: ")
# claveLength = len(claveUsuario)
# if (14 >= claveLength >= 8):
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# 
###########################################
# El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# 
# import random
# from statistics import mode, median, mean

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# moda = mode(numeros_aleatorios)
# media = median(numeros_aleatorios)
# mediana = mean(numeros_aleatorios)

# if (media > mediana > moda):
#     print("Sesgo positivo o a la derecha")
# elif (moda > mediana > media):
#     print("Sesgo negativo o a la izquierda")
# elif (media == mediana == moda):
#     print("Sin sesgo")
# else:
#     print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
# 
###########################################
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
# 
# stringUsuario = input("Ingrese una frase o palabra: ")
# vocales = ['a', 'e', 'i', 'o', 'u']
# if (stringUsuario[-1].lower() in vocales):
#     print(f'{stringUsuario}!')
# else:
#     print(stringUsuario)
# 
###########################################
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
# 
# nombreUsuario = input("Ingrese su nombre: ")
# opcionUsuario = int(input("Ingrese una opcion:\n 1: Mayusculas\n 2: Minusculas\n 3: Primer letra mayuscula\n"))

# if (opcionUsuario == 1):
#     print(nombreUsuario.upper())
# elif (opcionUsuario == 2):
#     print(nombreUsuario.lower())
# elif (opcionUsuario == 3):
#     print(nombreUsuario.title())
# else:
#     print("Ingrese una opcion válida")
# 
# ###########################################
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
# 
# magnitudUsuario = int(input("Ingrese la magnitud del terremoto: "))
# if (3 > magnitudUsuario > 0):
#     print("Magnitud del terremoto: Muy leve (imperceptible).")
# elif (4 > magnitudUsuario >= 3):
#     print("Magnitud del terremoto: Leve (ligeramente perceptible).")
# elif (5 > magnitudUsuario >= 4):
#     print("Magnitud del terremoto: Moderado (sentido por personas, pero generalmente no causa daños).")
# elif (6 > magnitudUsuario >= 5):
#     print("Magnitud del terremoto: Fuerte (puede causar daños en estructuras débiles).")
# elif (7 > magnitudUsuario >= 6):
#     print("Magnitud del terremoto: Muy Fuerte (puede causar daños significativos).")
# elif (magnitudUsuario >= 7):
#     print("Magnitud del terremoto: Extremo (puede causar graves daños a gran escala).")
# else:
#     print("Ingrese un dato válido")
#
###########################################
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
# 
hemisferioUsuario = input("Ingrese en que hemisferio se encuentra (N/S): ").upper()
mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el dia: "))

periodo1 = ['diciembre', 'enero', 'febrero', 'marzo']
periodo2 = ['marzo', 'abril', 'mayo', 'junio']
periodo3 = ['junio', 'julio', 'agosto', 'septiembre']
periodo4 = ['septiembre', 'octubre', 'noviembre', 'diciembre']

if (mes in periodo1):
    msg = 'Invierno' if hemisferioUsuario == 'N' else 'Verano'
    if (mes == periodo1[0] and dia <= 20) or (mes == periodo1[-1] and dia >= 21):
        pass
    else:
        print(msg)
if (mes in periodo2):
    msg = 'Primavera' if hemisferioUsuario == 'N' else 'Otoño'
    if (mes == periodo2[0] and dia <= 20) or (mes == periodo2[-1] and dia >= 21):
        pass
    else:
        print(msg)
if (mes in periodo3):
    msg = 'Verano' if hemisferioUsuario == 'N' else 'Invierno'
    if (mes == periodo3[0] and dia <= 20) or (mes == periodo3[-1] and dia >= 21):
        pass
    else:
        print(msg)
if (mes in periodo4):
    msg = 'Otoño' if hemisferioUsuario == 'N' else 'Primavera'
    if (mes == periodo4[0] and dia <= 20) or (mes == periodo4[-1] and dia >= 21):
        pass
    else:
        print(msg)

