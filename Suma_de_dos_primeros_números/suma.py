

print("Programa para dados 3 numeros enteros, la suma de los dos primeros es igual al tercero")
# Input
a= int(input("Ingrese el primer número: "))
b= int(input("Ingrese el segundo número: "))
c= int(input("Ingrese el tercer número: "))

d= (a+b)

if d==c:
    print("la suma de los dos primeros números " + str((a, b)) + ", es igual al tercero: "+ str(c))

else:
    print("La suma de los dos primeros números no da el tercero.")
