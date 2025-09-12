from  lista_de_contactos import ListaEncadenada
def menu():
    op=int(input("""
                 Menu de Opciones
    [0] Salir
    [1] Insetar Contacto (error si ya existe)
    [2] Eliminar Contacto
    [3] Buscar Contacto      
    [4] Mostrar la lista                                
    --->"""))
    return op
if __name__ == '__main__':
    GL = ListaEncadenada()
    opcion = menu()
    while opcion!=0:
        if(opcion==1):
           GL.inciso_1()
        elif(opcion==2):
            GL.inciso_2()
        elif(opcion==3):
            GL.inciso_3()
        elif(opcion==4):
            GL.recorrer()
        else:
            print("Opcion invalida")
        opcion=menu()


"""
1
Santiago Vilchez
10000
1
Antonio Ortiz
20000
1
Pablo Torrent
30000
"""