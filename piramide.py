'''Escribir un programa que le solicite al usuario un numero entero al usuario
y genere la siguiente figura en consola con tantos renglones cocmo el ususario
haya seleccionado:  1
                    1 1
                    1 1 1
                    1 1 1 1 '''

n = int(input('Digita un numero entero: '))
for i in range(n):
    print('1'*(i+1))