from arbol import Arbol
def menu():
    op=int(input("""
                 Menu de Opciones
    [0] Salir
    [1] Insetar Nodo
    [2] Mostrar InOrden
    [3] Mostrar el nodo padre y hermano de un nodo ingresado     
    [4] Mostrar la cantidad de nodos de un arbol
    [5] Mostrar la altura del arbol
    [6] Mostrar los sucesores de un nodo ingresado                              
    --->"""))
    return op
if __name__ == '__main__':
    arbol = Arbol()
    opcion = menu()
    while opcion!=0:
        if(opcion==1):
            try:
                insertado = int(input("Ingrese el valor a cargar en el arbol: "))   
                arbol.insertar(insertado)           
            except ValueError:
                print("!!ERROR EL VALOR INSERTADO DEBE SER UN NUMERO!!")
        elif(opcion==2):
            arbol.mostrar(arbol.raiz())
        elif(opcion==3):
            try:
                valor = int(input("Ingrese el valor para ver su padre y hermano: "))   
                padre,hermano=arbol.Padre_hermano(valor)
                if padre != None:
                    print(f"El padre es {padre}")
                    print(f"El hermano es {hermano if hermano!= None else "No tiene"}")
                else:
                    print("El valor ingresado no se encuentra en el arbol")       
            except ValueError:
                print("!!ERROR EL VALOR INSERTADO DEBE SER UN NUMERO!!")
        elif(opcion==4):
            print(f"La cantidad de nodos del arbol es: {arbol.cantidadNodos()}")
        elif(opcion==5):
            print(f"La altura del arbol es: {arbol.altura()}")
        elif(opcion==6):
            try:
                sucesor = int(input("Ingrese el valor para ver sus sucesores: "))   
                arbol.sucesores(sucesor)    
            except ValueError:
                print("!!ERROR EL VALOR INSERTADO DEBE SER UN NUMERO!!")
        else:
            print("Opcion invalida")
        opcion=menu()


"""
1
10
1
5
1
15
1
2
1
20
1
12

"""