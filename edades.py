'''crear un programa en python que te permita guardar 10 "edades"
una ves dadas estas edades te mustre por pantalla cuantas son mayores
de edad y cuantas son menores de edad'''

mayor=[]
menor=[]
mayorp=0
menorp=0

for i in range (10):
    edad=int(input('Digita tu edad: '))

    if edad <= 17:
        menor.append(edad)
        
    elif edad >= 18 :
        mayor.append(edad)
    else:
        print('Digite una edad correcta')
        

for i in mayor:
    mayorp += 1

print(f'Total mayores de edad {mayorp}')

for i in menor:
    menorp += 1

print(f'Total menores de edad {menorp}')