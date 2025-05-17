# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
#
# def imprimir_hola_mundo():
#     print('Hola Mundo!')
#
# imprimir_hola_mundo()
#
#####################################################################
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
#
# def saludar_usuario(nombre):
#     print(f'Hola {nombre}!')

# nombre_usuario = input('Ingrese su nombre: ')
# saludar_usuario(nombre_usuario)
# 
#####################################################################
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados
#
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')
# 
# nombre_usuario = input('Ingrese su nombre: ')
# apellido_usuario = input('Ingrese su apellido: ')
# edad_usuario = input('Ingrese su edad: ')
# residencia_usuario = input('Ingrese el lugar donde reside: ')
# 
# informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
# 
#####################################################################
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
# 
# pi = 3.14
# def calcular_area_circulo(radio):
#     return round(pi * (radio ** 2))
#
# def calcular_perimetro_circulo(radio):
#     return round(2 * pi * radio)
#
# radio = int(input('Ingrese el radio: '))
#
# print(f'El area para el radio dado es: {calcular_area_circulo(radio)}')
# print(f'El perimetro para el radio dado es: {calcular_perimetro_circulo(radio)}')
#
#####################################################################
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.
#
# def segundos_a_horas(segundos):
#     return round(segundos / 360, 1)
#
# segundos = int(input('Ingrese los segundos que desea pasar a horas: '))
#
# print(f'{segundos} es igual a: {segundos_a_horas(segundos)} horas')
#
#####################################################################
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.
#
# def tabla_multiplicar(numero):
#     for n in range(1, numero + 1):
#         print(f'{n} x {numero} = {n * numero}')
#
# numero_usuario = int(input('Ingrese un numero: '))
# tabla_multiplicar(numero_usuario)
#
#####################################################################
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.
#
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b
#     return (suma, resta, multiplicacion, round(division))

# numero1 = int(input('Ingrese un numero: '))
# numero2 = int(input('Ingrese otro numero: '))

# resultado = operaciones_basicas(numero1, numero2)
# print(f'El resultado de sumar {numero1} + {numero2} es: {resultado[0]}')
# print(f'El resultado de restar {numero1} - {numero2} es: {resultado[1]}')
# print(f'El resultado de multiplicar {numero1} x {numero2} es: {resultado[2]}')
# print(f'El resultado de dividir {numero1} / {numero2} es: {resultado[3]}')
#
#####################################################################
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales
#
# def calcular_imc(peso, altura):
#     return round(peso / (altura ** 2), 2)
#
# peso_usuario = float(input('Ingrese su peso en kg: '))
# altura_usuario = float(input('Ingrese su altura en metros: '))
#
# print(f'Su IMC es: {calcular_imc(peso_usuario, altura_usuario)}')
#
#####################################################################
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
#
# def celsius_a_fahrenheit(celsius):
#     return round((celsius * 9/5) + 32)
#
# celsius_usuario = int(input('Ingrese la temperatura en Celsius: '))
# print(f'{celsius_usuario} grados celsius en Fahrenheit es: {celsius_a_fahrenheit(celsius_usuario)}')
#
#####################################################################
# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
#
# def calcular_promedio(a, b, c):
#     return round((a + b + c) / 3)
#
# numero1 = int(input('Ingrese un numero: '))
# numero2 = int(input('Ingrese otro numero: '))
# numero3 = int(input('Ingrese otro numero: '))
#
# print(f'El promedio de {numero1}, {numero2} y {numero3} es: {calcular_promedio(numero1, numero2, numero3)}')
#
#####################################################################