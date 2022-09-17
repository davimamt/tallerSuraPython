
contador=3

print("**** opciones tienda ****")
print("1. Agregar datos de los productos")
print("2. Mostrar datos de produtos ingresados")
print("0. Salir")

inventario=[]

while (contador !=0):
    producto={}
    contador= int(input ("Ingresa tu opcion: "))
    if (contador==1):
        print("INGRESA TU PRODUCTO")
        producto['nombre']= input("ingresa el nombre de tu prodcuto: ")
        producto['color']= input("ingresa el color de tu prodcuto: ")
        producto['precio']= int(input("ingresa el precio de tu prodcuto: "))
        inventario.append(producto)

    elif(contador==2):
        print("TUS PRODUVTOS SON: ")
        print(inventario)
    elif(contador==0):
        print("SALIR")
        break
    else:
        print("INGRESA UNA OPCION VALIDA")


