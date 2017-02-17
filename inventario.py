print ("Bienvenido")
opc=(input("quiere comprar 1.si  2.no "))
inventario={}

while opc=="si":
	producto=(input("ingrese pruducto: "))
	cantidad=int(input("ingrese numero: "))
	opc=(input("desea continuar 1. si 2. no")) 
	inventario[producto] = cantidad
	if opc=="no":
		for  productos in inventario:
			print (productos, inventario[productos])