# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
# 
# for i in range(101):
#     print(i)
# 
#########################################
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
# 
# inputUsuario = int(input('Ingrese un numero entero: '))
# count = 0
# temp = inputUsuario
# 
# while round(temp) != 0:
#     temp = temp / 10
#     count += 1
# print(f'El número ingresado tiene {count} dígitos')
# 
#########################################
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
# 
# inputUsuario1 = int(input('Ingrese un número entero: '))
# inputUsuario2 = int(input('Ingrese otro número entero: '))
# count = 0
# for i in range(inputUsuario1 + 1, inputUsuario2):
#     count += i
# print(f'La suma de los números enteros comprendidos entre {inputUsuario1} y {inputUsuario2}, excluyendo estos dos valores, es: {count}')
# 
#########################################
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
# 
# inputUsuario = 1
# print('Ingrese una serie de números enteros\n(si ingresa 0 el programa mostrara la suma de todos los numeros ingresados)\n')
# count = 0
# while inputUsuario != 0:
#     inputUsuario = int(input('Ingrese un número entero: '))
#     count += inputUsuario
# print(f'El total acumulado es: {count}')
# 
#########################################
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
# 
# import random

# randomNumber = random.randrange(0, 10)
# inputUser = 10
# count = 0

# while inputUser != randomNumber:
#     inputUser = int(input('Adivina el número, entre 0 y 9: '))
#     count += 1
# print(f'La cantidad de intentos hasta adiviar el numero fueron: {count}!')
# 
#########################################
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
# 
# for i in range(100, 0, -1):
#     if i % 2 == 0:
#         print(i)
# 
#########################################
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
# 
# numUser = int(input('Ingrese un número entero positivo: '))
# count = 0
# 
# for i in range(0, numUser):
#     count += i
# 
# print(f'La suma de todos los numeros comprandidos entre 0 y {numUser} es: {count}')
# 
#########################################
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
#
# maxNum = 100
# numCount = 0
# parCounter = 0
# imparCounter = 0
# positivoCounter = 0
# negativoCounter = 0
# 
# while numCount != maxNum:
#     numCount +=1
#     userInput = int(input('Ingrese un número: '))
#     if userInput == 0:
#         continue
#     if userInput % 2 == 0:
#         parCounter += 1
#     else:
#         imparCounter += 1
#     if userInput > 0: 
#         positivoCounter += 1
#     else: 
#         negativoCounter += 1
# 
# print(f'''
# De los números ingresados:
# {parCounter} son pares.
# {imparCounter} son impares.
# {positivoCounter} son positivos.
# {negativoCounter} son negativos.
# ''')
# 
#########################################
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
# 
# maxNum = 10
# numCount = 0
# acumulador = 0

# while numCount != maxNum:
#     numCount += 1
#     userInput = int(input('Ingrese un número: '))
#     acumulador += userInput
    
# print(f'La media de los valores ingresados es {acumulador / maxNum}')
# 
#########################################
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# 
# inputUser = int(input('Ingrese un número de varios dígitos: '))
# numero = inputUser
# numeroInvertido = 0
# while numero > 0:
#     digito = numero % 10
#     numeroInvertido = numeroInvertido * 10 + digito
#     numero //= 10

# print(f'El numero {inputUser} invertido es {numeroInvertido}')