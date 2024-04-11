'''Realizar una calculadora que pueda sumar, restar, dividir y multiplicar a peticion del usuario:
Mostrar un menu de opciones con las operaciones soportadas
De acuerdo a lo que seleccione el usuario: 
solicitar valor 1 y valor 2
Mostrar el resultado de la operacion
Finalizar el programa'''

print('\tMUENU''\nS:sumar''\nR:restar''\nM:multiplicar''\nD:dividir')

flag=True
#opcion= str(input('Seleccione una opcion de menu: ')).lower()

while flag == True:
  opcion= str(input('Seleccione una opcion de menu: ')).lower()

  if opcion == 'salir':
    break

  if opcion == 's':
    num1=float(input('Digite el primer numero: '))
    num2=float(input('Digite el segundo numero: '))
    suma = num1+num2
    print(suma)

  if opcion == 'r':
    num1=float(input('Digite el primer numero: '))
    num2=float(input('Digite el segundo numero: '))
    resta = num1-num2
    print(resta)

  if opcion == 'm':
    num1=float(input('Digite el primer numero: '))
    num2=float(input('Digite el segundo numero: '))
    multiplicacion = num1*num2
    print(multiplicacion)

  if opcion == 'd':
    num1=float(input('Digite el primer numero: '))
    num2=float(input('Digite el segundo numero: '))
    divicion = num1/num2
    print(divicion)
