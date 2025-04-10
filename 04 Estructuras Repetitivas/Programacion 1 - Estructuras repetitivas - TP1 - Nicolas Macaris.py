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