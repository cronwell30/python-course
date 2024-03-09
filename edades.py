'''crear un programa en python que te permita guardar 10 "edades"
una ves dadas estas edades te mustre por pantalla cuantas son mayores
de edad y cuantas son menores de edad'''

mayor=[]
menor=[]

for i in range (10):
    edad=int(input('Digita tu edad: '))
    if edad <= 17:
        menor.append(edad)
        print(menor)
    elif edad >= 18:
        mayor.append(edad)
        print(mayor)

mayorp=0
for i in mayor:
    mayorp += 1
    print(f'Promedio mayor {mayorp}')

menorp=0
for i in menor:
    menorp += 1
    print(f'Promedio menor {menorp}')