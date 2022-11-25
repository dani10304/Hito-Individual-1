#creamos variables para registrar los datos del usuario
nombre=input('dime tu nombre: ')
DNI=int(input('dime tu DNI: '))
telefono=int(input('dime tu numero de telefono: '))
ciudad=input('dime tu ciudad: ')
correo=input('dime tu correo: ')
contraseña=input('dime tu contraseña: ')

print('usuario registrado')

#creamos una clase llamada producto donde almacenamos todos los valores

class Producto:
    def __init__(self,producto,unidades,precios,) -> None: #metemos las variables del cliente
        self.producto=producto
        self.unidades=unidades
        self.precios=precios
    
    def mostrarDetalle(self):
        print(f'el producto {self.producto}, tiene un precio de {self.precios} y hay un total de {self.unidades} unidades') #llamamos a una funcion para mostrar detalles de los productos
 
#creamos varios productos distintos
 
producto1=Producto('pantalon','100',27)
producto2=Producto('camisetas','150',37)
producto3=Producto('zapatillas','200',67)
producto4=Producto('chaqueta','60',47)
 
#llamamos a los productos para que nos muestre el detalle de esos productos
 
producto1.mostrarDetalle()
producto2.mostrarDetalle()
producto3.mostrarDetalle()
producto4.mostrarDetalle()

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
    print('Calculamos el precio y le damos las vueltas si se diera el caso')
    print('la factura ha sido mandada al correo indicado')
elif pagos=='T':
    print('Metemos la tarjeta y accedemos a cobrale por medio del datafono')
    print('la factura ha sido mandada al correo indicado')


print('el seguimiento de su compra se ha enviado via SMS o via correo electronico')