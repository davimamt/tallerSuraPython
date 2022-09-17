

contador=0
salpicon=[]
while (contador<5):
    frutas={}
    print(f'Ingresa la fruta #{contador+1}')
    frutas['nombre']=input("Ingrese el nombre de la furta: ")
    frutas['color']=input("Ingrese el color de la furta: ")
    frutas['precio']=int(input("Ingrese el precio de la furta: "))
    salpicon.append(frutas)
    contador=contador+1


print(salpicon)