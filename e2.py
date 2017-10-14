print("Datos de la primera persona")

# Cargar por teclado una cadena de caracteres con input

nom1 = input("Ingresar nombre 1:")
pre1 = int(input("Ingresar precio 1:"))
nom2 = input("Ingresar nombre 2:")
pre2 = int(input("Ingresar precio 2:"))

# Constante

BONIFICACION = 20

# Sumar dos precios
precioTotal = pre1 + pre2

# Comprobar si el precio1 es mayor o igual al precio2
comparar = pre1 >= pre2
logico = (pre1 < pre2 and pre1 == pre2)

cabezera = "Resultados del producto {0} y del producto {1}:"

print(cabezera.format(nom1,nom2))
print("El precio del primer valor es mayor o igual al precio del segundo valor:")
print(comparar)

print("La suma de los dos productos es:" + str(precioTotal))
print("Precio1 < Precio2 and Precio1 == Precio2")
print(logico)

precioTotal += BONIFICACION
print("Al precio total le incrementamos su valor de bonificacion:" + str(precioTotal))