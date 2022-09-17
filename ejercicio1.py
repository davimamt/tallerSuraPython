numeros = []
contNegativos=0
contPositivos=0

while ((contPositivos+contNegativos)<10):
    n= int(input("Indique un numero: "))
    numeros.append(n)
    if (n>0):
        contPositivos=contPositivos+1;
    elif (n<0):
        contNegativos=contNegativos+1;
    else:
        print("Ingrese un numero");



for observador in numeros:
    print(observador);

print(f'En la lista hay {contNegativos} numeros negativos')
print(f'En la lista hay {contPositivos} numeros positivos')


