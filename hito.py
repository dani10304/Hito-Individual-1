import pandas as pd

#creamos variables para registrar los datos del usuario
nombre=input('dime tu nombre: ')
DNI=int(input('dime tu DNI: '))
telefono=int(input('dime tu numero de telefono: '))
ciudad=input('dime tu ciudad: ')
correo=input('dime tu correo: ')
contraseña=input('dime tu contraseña: ')

print('usuario registrado')

productos=['pantalones', 'zapatillas', 'chaqueta', 'camisetas', ' gorras']
precio=[27.35, 67.30, 15.99, 28.75, 5.08]

d={'col1': ['pantalones', 'zapatillas', 'chaqueta', 'camisetas', ' gorras'], 'col2': [27.35, 67.30, 15.99, 28.75, 5.08]}
df=pd.DataFrame(data=d)
print(df)


#creamos un diccionario llamado cesta
cesta = {}
continuar = True
#utilizamos while para que hasta que no digamos que 'no' podemos seguir anunciando productos
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"

#le damos valor a la cesta
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)

pagos=input('si desea pagar con tarjeta pulse "T":  si desea pagar en efectivo pulse "E": ')
if pagos=='E':
    print('Recogemos el efectivo y le damos las vueltas si se diera el caso')
    print('la factura se da en el momento')
elif pagos=='T':
    print('Metemos la tarjeta y accedemos a cobrale por medio del datafono')
    print('la factura ha sido mandada al correo indicado')


print('el seguimiento de su compra se ha enviado via SMS o via correo electronico')