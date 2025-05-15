'''Crea un script en python en la cual en una lista esten almaceneados una cerie de numeros
y acontinuacio le permita al usuarioconsultar si un numero de su eleccion se encuenntra
en la lista'''

#Creando liosta
lista_numeros = [12,8,55,32,44,56,76]
#variable 
numero = int(input('Digitge un numero para consultar en la lista: '))
#opcion para consultar numero
if numero in lista_numeros:
    print('Tu numero se encuentra en la lista felicidades')

else:
    print('Tu numero no se encuentra en nuestra lista lo siento')
