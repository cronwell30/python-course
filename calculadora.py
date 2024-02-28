'''Realizar una calculadora que pueda sumar, restar, dividir y multiplicar a peticion del usuario:
Mostrar un menu de opciones con las operaciones soportadas
De acuerdo a lo que seleccione el usuario: 
solicitar valor 1 y valor 2
Mostrar el resultado de la operacion
Finalizar el programa'''

print('\tMENU\nS:sumar \nR:restar \nM:multiplicar \nD:dividir')
opcion=str(input('Selecione una upcion de menu: '))

num1=float(input('Digite el primer numero: '))
num2=float(input('Digite el segundo numero:'))

if opcion=='s':
  reusltado=num1+num2
  print(f'La respuesta es {reusltado}')
elif opcion=='r':
  reusltado=num1-num2
  print(f'La respuesta es {reusltado}')
elif opcion=='m':
  reusltado=num1*num2
  print(f'La respuesta es {reusltado}')
elif opcion=='d':
  reusltado=num1/num2
  print(f'La respuesta es {reusltado}')
  