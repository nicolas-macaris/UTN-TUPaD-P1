# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# numero_usuario = int(input("Ingrese un número entero: "))
#
# for i in range(1, numero_usuario + 1):
#     print(f'El factorial de {i} es {factorial(i)}')
#
###########################################################################
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
###########################################################################
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# 
# numero_usuario = int(input("Ingrese la posición de la serie Fibonacci hasta la que desea imprimir: "))
# 
# print(f'La serie fibonacci hasta la posición {numero_usuario} es:')
# for i in range(numero_usuario + 1):
#     print(fibonacci(i), end=' ')
# 
###########################################################################
# Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.
# 
# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)
    
# numero_base = int(input("Ingrese la base: "))
# numero_exponente = int(input("Ingrese el exponente: "))
# 
# resultado = potencia(numero_base, numero_exponente)
# print(f'El resultado de {numero_base} elevado a {numero_exponente} es: {resultado}')
# 
###########################################################################
# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# 
# def decimal_a_binario(n):
#     if n == 0:
#         return ""
#     else:
#         return decimal_a_binario(n // 2) + str(n % 2)
# 
# numero_usuario = int(input("Ingrese un número entero positivo: "))
# if numero_usuario < 0:
#     print("El numero debe ser entero positivo.")
# else:
#     resultado = decimal_a_binario(numero_usuario)
#     if resultado == "":
#         resultado = "0"
#     print(f'{numero_usuario} a numero binario es igual a: {resultado}')
# 
###########################################################################
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
# 
# def es_palindromo(palabra):
#     palabra = palabra.lower()
#  
#     if len(palabra) <= 1:
#         return True
#  
#     if palabra[0] != palabra[-1]:
#         return False
# 
#     return es_palindromo(palabra[1:-1])
# 
# palabra_usuario = input("Ingrese un texto sin espacios ni tildes: ")
# if es_palindromo(palabra_usuario):
#     print(f'"{palabra_usuario}" es un palíndromo.')
# 
###########################################################################
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# 
# def suma_digitos(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + suma_digitos(n // 10)
# 
# numero_usuario = int(input("Ingrese un número entero positivo: "))
# if numero_usuario < 0:
#     print("El número debe ser entero positivo.")
# else:   
#     resultado = suma_digitos(numero_usuario)
#     print(f'La suma de los dígitos de {numero_usuario} es: {resultado}')
# 
###########################################################################
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# 
# def contar_bloques(n):
#     if n <= 0:
#         return 0
#     else:
#         return n + contar_bloques(n - 1)
# 
# numero_bloques = int(input("Ingrese el número de bloques en el nivel más bajo: "))
# total_bloques = contar_bloques(numero_bloques)
# print(f'El total de bloques necesarios para construir la pirámide es: {total_bloques}')
# 
###########################################################################
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# 
# def contar_digito(numero, digito):
#     if numero == 0:
#         if digito == 0:
#             return 1
#         else:
#             return 0
#     else:
#         if numero % 10 == digito:
#             return 1 + contar_digito(numero // 10, digito)
#         else:
#             return contar_digito(numero // 10, digito)
# 
# numero_usuario = int(input("Ingrese un número entero positivo: "))
# digito_usuario = int(input("Ingrese un dígito (entre 0 y 9): "))
# resultado = contar_digito(numero_usuario, digito_usuario)
# print(f'El dígito {digito_usuario} aparece {resultado} veces en el número {numero_usuario}.')
# 
###########################################################################