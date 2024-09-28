def productos(v1,v2,*lista):
    producto=v1*v2
    for x in range(len(lista)):
        producto=producto+lista[x]
    return producto
cuadrado = int(input("Ingrese el Valor a Elevar al cuadrado: "))
print("El cuadrado es: ", cuadrado * cuadrado),
v1 = int(input("Ingrese el primer Valor a multiplicar: "))
v2 = int(input("Ingrese el segundo Valor a multiplicar: "))
print("el producto es: ", productos (v1,v2))