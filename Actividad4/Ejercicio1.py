rango_inicial = int(input("Ingrese el rango inicial: "))
rango_final = int(input("Ingrese el rango final: "))
numero = int(input("Ingrese un número: "))
if(numero >= rango_inicial and numero <= rango_final):
    print("El número está dentro del rango.")
else:
    print("El número está fuera del rango.")