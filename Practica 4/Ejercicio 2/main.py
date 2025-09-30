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
            arbol.inOrden()
        elif(opcion==3):
            pass
        elif(opcion==4):
            print(f"La cantidad de nodos del arbol es: {arbol.cantidadNodos()}")
        elif(opcion==5):
            print(f"La altura del arbol es: {arbol.altura()}")
        elif(opcion==6):
            pass
        else:
            print("Opcion invalida")
        opcion=menu()

