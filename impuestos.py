'''Crea un script en python que le permita al usuario saber el valor de su fatura permitiendole
introducir el valor de su compra y el porcentaje de impuesto '''

compra = float(input('Cuanto pago en su compra: $'))
impuesto = int(input('Porcentage de impuesto: %'))/100

valor = compra*impuesto

print(f'El valor de impestos es de {valor:.2f}')