# TP 1 - Estructuras secuenciales

# Ejercicio 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

# print('Hola Mundo!')

# Ejercicio 2
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

# nombreUsuario = input('Ingrese su nombre: ')
# print(f'Hola {nombreUsuario}!')

# Ejercicio 3
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

# nombreUsuario = input('Ingrese su nombre: ')
# apellidoUsuario = input('Ingrese su apellido: ')
# edadUsuario = input('Ingrese su edad: ')
# residenciaUsuario = input('Ingrese su recidencia: ')

# print(f'Soy {nombreUsuario} {apellidoUsuario}, tengo {edadUsuario} años y vivo en {residenciaUsuario}')

# Ejercicio 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

# radio = int(input('Ingrese el radio: '))
# pi = 3.14
# area = pi * radio ** 2
# perimetro = 2 * pi * radio
# print(f'El area del circulo es {area}')
# print(f'El perimetro del circulo es {perimetro}')

# Ejercicio 5
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

# segundos = int(input('Ingrese una cantidad de segundos: '))
# horas = segundos / 3600
# print(f'{segundos} segundos equivalen a {horas} horas')

# Ejercicio 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

# numero = int(input('Ingrese un numero: '))
# print(f'La tabla del {numero} es:')
# for i in range(1, 11):
#     print(f'{numero} x {i} = {numero * i}')

# Ejercicio 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# numero1 = int(input('Ingrese un numero entero distinto de 0: '))
# numero2 = int(input('Ingrese otro numero entero distinto de 0: '))
# print(f'El resultado de sumar {numero1} mas {numero2} es: {numero1 + numero2}')
# print(f'El resultado de restarle a {numero1}, {numero2} es: {numero1 - numero2}')
# print(f'El resultado de multiplicar {numero1} por {numero2} es: {numero1 * numero2}')
# print(f'El resultado de dividir {numero1} por {numero2} es: {numero1 / numero2}')

# Ejercicio 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

# alturaUsuario = float(input('Ingrese su altura en metros: '))
# pesoUsuario = float(input('Ingrese su peso en kilos: '))
# imc = pesoUsuario / alturaUsuario ** 2
# print(f'Tu indice de masa corporal es de {imc}')

# Ejercicio 9
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

# temperaturaCelcius = int(input('Ingrese la temperatura en grados Celcius: '))
# temperaturaFahrenheit = 9/5 * temperaturaCelcius + 32
# print(f'{temperaturaCelcius} grados centigrados equivalen a {temperaturaFahrenheit} grados fahrenheit.')

# Ejercicio 10
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

# numero1 = int(input('Ingrese un numero: '))
# numero2 = int(input('Ingrese otro numero: '))
# numero3 = int(input('Ingrese otro numero: '))
# promedio = int((numero1 + numero2 + numero3) / 3)
# print(f'El promedio de los numeros ingresados es: {promedio}')
