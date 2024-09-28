def conta(cadena):
    x=cadena.count("a")
    y=cadena.count("A")
    return "La cantidad de 'a' es ",x , "La cantidad de 'A' es ",y

print("La oracion Tiene A y a:")
cadena=input("Ingrese palabra o frase : ")
retur= conta(cadena)
print(retur)
